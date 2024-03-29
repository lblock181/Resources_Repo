import json
import pyrebase
from typing import Union
from firebase_admin import auth
from requests.exceptions import HTTPError
from os import getenv

class AuthGuard():
    def __init__(self) -> None:
        self.fb_auth = auth
        self.pb_auth = pyrebase.initialize_app(self.__get_firebase_config__()).auth()

    def __get_firebase_config__() -> dict:
        return {
            "apiKey": getenv("apiKey"),
            "authDomain": getenv("authDomain"),
            "databaseURL": getenv("databaseURL"),
            "projectId": getenv("projectId"),
            "storageBucket": getenv("storageBucket"),
            "messagingSenderId": getenv("messagingSenderId"),
            "appId": getenv("appId")
        }

    def get_firebase_user(self, user_local_id:str) -> dict:
        return self.fb_auth.get_user(user_local_id)

    def send_verification_email(self, user_id_token: str) -> None:
        self.pb_auth.send_email_verification(user_id_token)

    def firebase_sign_in_email_password(self, email:str, password:str) -> dict:
        try:
            return self.pb_auth.sign_in_with_email_and_password(email, password)
        except HTTPError as http_error:
            raise HTTPError(self.handle_auth_exception(http_error.strerror))
        except Exception as e:
            return f"Authentication Failed\n {str(e)}"

    def generate_session_cookie(self, user_id_token: str) -> bytes:
        return self.fb_auth.create_session_cookie(user_id_token, 600)

    def validate_session_cookie(self, s_cookie:str) -> bool:
        try:
            d = self.fb_auth.verify_session_cookie(session_cookie=s_cookie, check_revoked=True)
            return True
        except:
            return False
        
    def handle_auth_exception(self, auth_error:Union[str, dict]) -> str:
        auth_error = json.loads(auth_error) if isinstance(auth_error, str) else auth_error
        auth_msg = auth_error['error']['message'].split(" : ")
        if len(auth_msg) > 1:
            return auth_msg[1]
        match auth_msg[0]:
            case "INVALID_EMAIL" | "INVALID_PASSWORD" | "EMAIL_NOT_FOUND":
                return "Invalid email or password"
            case "USER_DISABLED":
                return "User ID has been disabled. Contact developer to re-enable account"
            case _:
                return "Unauthorized - ErrorCode 500"

'''
on the api/app side, to add the session cookie to the response
        resp = make_response(render_template(return_template))
        resp.set_cookie("session", session_cookie)
    return resp

'''