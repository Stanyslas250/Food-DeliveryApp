from typing import Any, List
import pyrebase
from flet import *
from datetime import *

config = {
    "apiKey": "AIzaSyBbxwOZpVhI6oSa-hplK1mcsHDst0qiZ2Q",
    "authDomain": "foodie-app-25aed.firebaseapp.com",
    "projectId": "foodie-app-25aed",
    "storageBucket": "foodie-app-25aed.appspot.com",
    "messagingSenderId": "26355075263",
    "appId": "1:26355075263:web:0ae986db63b583e4e05e0a",
    "databaseURL": ""
    }

# initialize firebase
firebase = pyrebase.initialize_app(config)

# set up authentification manager
auth = firebase.auth()



def restart_state(e):
    e.control.error_text = None
    e.control.update()

def validate_required_fied(e):
    if e.control.value == "":
        e.control.error_text = "The field is required"
        e.control.update()

#Function for user sign in
def sign_in_user(email:str,password:str):
    try:
        user = auth.sign_in_with_email_and_password(
            email=email,password=password
        )
        
        info = auth.get_account_info(user["idToken"])
        
        data = ["createdAt","lastLoginAt"]
        
        for key in info:
            if key == 'users':
                for item in data:
                    print(
                        item 
                    ) 
        
        return True       
    
    except Exception as e:
        print(e)

#Function for user registration
def register_user(email:str,password:str):
    try:
        auth.create_user_with_email_and_password(
            email=email,
            password=password
        ) 
        return True  
        
    except Exception as e:
        print(e)
        
    
    
    
    
    
    