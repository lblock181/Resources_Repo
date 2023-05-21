from os import getenv
from requests import Request

class Controller():
    def __init__(self) -> None:
        self.apikey = getenv('FLASK_APIK_KEY')

    def validate_apikey(self, req_api_key:str) -> bool:
        return True if req_api_key == self.apikey else False
    
    def parse_user_request(self, user_req:Request) -> dict:
        return {}