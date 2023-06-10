from os import getenv
from uuid import uuid4
from typing import List, Union
from datetime import datetime
from packages.utility import get_db_cert
from firebase_admin import firestore, initialize_app, credentials
from google.cloud.firestore_v1.base_query import FieldFilter, BaseCompositeFilter

class FirestoreDb():
    
    def __init__(self, db_coll_name:str) -> None:
        self.app=initialize_app(credentials.Certificate(get_db_cert()))
        self.db = firestore.client()
        self.db_coll=self.db.collection(db_coll_name)
        self.mandatory_config_keys = []
        self.mandatory_submission_keys = []
        self.deny_list = []

    def validate_submission_dict(self, raw_dict:dict) -> dict:
        ## validate that raw dictionary has all required keys & values with correct data types
        raw_dict = self.__doc_submission_schema__(raw_dict)
        return raw_dict

    def __doc_submission_schema__(self, raw_dict: dict) -> dict:
        ## return modified version with additional backend fields
        schema_dict = raw_dict
        return schema_dict

    def __doc_config_schema__(self, raw_dict: dict) -> dict:
        ## return modified version with additional backend fields
        schema_dict = raw_dict
        return schema_dict

    def update_config_doc(self, new_config_dict:dict, bypass:bool = False) -> None:
        try:
            if bypass:
                new_config = new_config_dict
            else:
                new_config = self.__doc_config_schema__(new_config_dict)

            upd_config = self.__update_document__(getenv("CONFIG_DOC_ID"), new_config)
            update_success = True
        except KeyError as ke:
            raise Exception(f"Error in new config - {str(ke)}")
            update_success = False
        except Exception as e:
            raise e
            update_success = False
        finally:
            return update_success

    def create_new_doc(self,doc_details: dict) -> dict:
        return self.db_coll.document(str(uuid4())).set(doc_details)

    def read_doc(self, doc_id: str) -> dict:
        doc = self.db_coll.document(doc_id).get()
        return doc.to_dict()

    def read_doc_collection(self, *args:Union[str,List]) -> list:
        """Gets collection of documents based on the provided arguments

        Raises:
            TypeError: Raised when args provided are not a list or string

        Returns:
            list: results of query
        """        
        if len(args) == 0:
            return self.__read_doc_collection_all_docs__()
        elif 2 < len(args) <= 3:
            return self.__read_doc_collection_single_query__(*args)
        elif isinstance(args[0], list):
            return self.__read_doc_collection_multi_query__(args[0])
        else:
            raise TypeError("Provided args not list or string values")

    def __read_doc_collection_all_docs__(self) -> list:
        return [ doc for doc in self.db_coll.stream() ]

    def __read_doc_collection_single_query__(self, filter_field: str, operator: str, val: str) -> list:
        docs = self.db_coll.where(filter=FieldFilter(filter_field, operator, val)).stream()
        return [ doc.to_dict() for doc in docs ]

    def __read_doc_collection_multi_query__(self, filter_list: List[tuple]) -> list:
        for tup in filter_list:
            if len(tup) != 3:
                raise Exception("Invalid number of values in tuple. Required number is 3 to unpack")
        docs = self.db_coll.where(filter=BaseCompositeFilter(
            "AND", [FieldFilter(*f) for f in filter_list]
        )).stream()
        return [ doc.to_dict() for doc in docs ]

    def __update_document__(self, doc_id:str, new_values:dict) -> dict:
        doc_ref = self.db_coll.document(doc_id).update(new_values)
        return doc_ref
    
    def __delete_document__(self, doc_id:str) -> bool:
        try:
            self.db_coll.document(doc_id).delete()
            return True
        except:
            return False

    def __delete_field__(self, doc_id:str, field_to_delete:str) -> bool:
        try:
            doc_ref = self.db_coll.document(doc_id)
            doc_ref.update({
                field_to_delete: firestore.DELETE_FIELD
            })
            return True
        except:
            return False

    def __delete_multiple_docs__(self, filter_field:str, operator:str, val: str) -> bool:
        try:
            docs = self.db_coll.where(filter_field, operator, val).stream()
            for doc in docs:
                doc.delete()
            return True
        except:
            return False