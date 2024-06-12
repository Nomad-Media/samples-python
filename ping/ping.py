import sys, os
sys.path.append(os.path.realpath('./nomad-samples'))

from nomad_media_pip.src.nomad_sdk import Nomad_SDK
from config import config

nomad_sdk = Nomad_SDK(config)

import json

def ping():
    try:
        APPLICATION_ID = input("Enter the application id: ") if input("Do you want to enter an application id? (y/n): ") == "y" else None
        USER_SESSION_ID = input("Enter the user session id: ") if input("Do you want to enter a user session id? (y/n): ") == "y" else None

        print(json.dumps(nomad_sdk.ping(APPLICATION_ID, USER_SESSION_ID), indent=4))
    except Exception as e:
        print(e)
    
def ping_auth():
    try:
        APPLICATION_ID = input("Enter the application id: ") if input("Do you want to enter an application id? (y/n): ") == "y" else None
        USER_SESSION_ID = input("Enter the user session id: ") if input("Do you want to enter a user session id? (y/n): ") == "y" else None

        print(json.dumps(nomad_sdk.ping_auth(APPLICATION_ID, USER_SESSION_ID), indent=4))
    except Exception as e:
        print(e)
    
functions = {
    "1": ping,
    "2": ping_auth
}

if __name__ == "__main__":
    print("Which function do you want to run?")
    for key, value in functions.items():
        
        print(f"{key}: {value.__name__}")

    while True:
        USER_INPUT = input("Enter the number of the function you want to run: ")

        if USER_INPUT in functions:
            functions[USER_INPUT]()
            break
        else:
            print("Invalid input")