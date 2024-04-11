from typing import Any, List
import pyrebase
from flet import *
from datetime import *

config = {
    "apiKey": "AIzaSyB7Z1S_rqs3mKel9HG2td-emPP_KdoO0es",
    "authDomain": "foodie---food-delivery.firebaseapp.com",
    "projectId": "foodie---food-delivery",
    "storageBucket": "foodie---food-delivery.appspot.com",
    "messagingSenderId": "312660170224",
    "appId": "1:312660170224:web:afbcf58de4226d6627b935",
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
        
    
    
    
    
    
    