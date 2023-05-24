from firebase_admin import credentials, firestore, initialize_app, auth
import pyrebase
import json
from typing import Callable

class AuthGuard():
    def __init__(self) -> None:
        self.fb_auth = auth
        self.default_app=initialize_app(credentials.Certificate("./dev_only/utepils-cooler-removals-firebase-adminsdk-e1dr9-ca851aa555.json"))
        self.db = firestore.client()
        self.todo_ref=self.db.collection('todos')  #sample collections
        self.pb_auth = pyrebase.initialize_app(json.load(open('./dev_only/fb_config.json'))).auth()

    def get_firebase_user(self, user_local_id:str) -> dict:
        return self.fb_auth.get_user(user_local_id)

    def send_verification_email(self, user_id_token: str) -> None:
        self.pb_auth.send_email_verification(user_id_token)

    def firebase_sign_in_email_password(self, email:str, password:str) -> dict:
        return self.pb_auth.sign_in_with_email_and_password(email, password)

    def generate_session_cookie(self, user_id_token: str) -> bytes:
        return self.fb_auth.create_session_cookie(user_id_token, 600)

    def validate_session_cookie(self, s_cookie:str) -> bool:
        try:
            d = self.fb_auth.verify_session_cookie(session_cookie=s_cookie, check_revoked=True)
            return True
        except:
            return False


'''
on the api/app side, to add the session cookie to the response
        resp = make_response(render_template(return_template))
        resp.set_cookie("session", session_cookie)
	return resp

'''