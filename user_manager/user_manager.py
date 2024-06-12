from nomad_media_pip.src.nomad_sdk import Nomad_SDK
from config import config

nomad_sdk = Nomad_SDK(config)

import json

USER_CONTENT_DEFINITION_ID = "b42cb50a-1664-4b68-a8f8-2272b9b13e7c"

def get_input(prompt, required):
    return input(f"{prompt}: ") if required or input(f"Do you want to add {prompt} (y/n): ") == "y" else None

def get_dict(prompt, keys, required):
    return {key: input(f"{prompt} {key}: ") for key in keys} if required or input(f"Do you want to add {prompt} (y/n): ") == "y" else None

def get_list(prompt, keys, required):
    items = []
    if required or input(f"Do you want to add {prompt} (y/n): ") == "y":
        while True:
            items.append({key: input(f"{prompt} {key}: ") for key in keys})
            if not required or input(f"Do you want to add another {prompt} (y/n): ") == "n":
                break
    
    return items

def create_user():
    try:
        PROPERTIES = {}
        PROPERTIES["firstName"] = get_input("First Name", False)
        PROPERTIES["lastName"] = get_input("Last Name", False)
        PROPERTIES["email"] = get_input("Email", True)
        PROPERTIES["userStatus"] = get_dict("User Status", ["id", "description"], False)
        PROPERTIES["organization"] = get_input("Organization", False)
        PROPERTIES["title"] = get_input("Title", False)
        PROPERTIES["phone"] = get_input("Phone", False)
        PROPERTIES["phoneExt"] = get_input("Phone Ext", False)
        PROPERTIES["mobilePhone"] = get_input("Mobile", False)
        PROPERTIES["address"] = get_input("Address", False)
        PROPERTIES["address2"] = get_input("Address2", False)
        PROPERTIES["city"] = get_input("City", False)
        PROPERTIES["stateId"] = get_dict("State", ["id", "description"], False)
        PROPERTIES["postalCode"] = get_input("Postal Code", False)
        PROPERTIES["country"] = get_dict("Country", ["id", "description"], False)
        PROPERTIES["assignedSecurityGroups"] = get_list("Security Group", ["id", "description"], False)
        PROPERTIES["role"] = get_dict("System Role", ["id", "description"], False)

        USER_ID = nomad_sdk.create_content(USER_CONTENT_DEFINITION_ID, None)

        nomad_sdk.update_content(USER_ID["contentId"], USER_CONTENT_DEFINITION_ID, PROPERTIES, None)

        print(f"User ID: {USER_ID['contentId']}")

    except Exception as e:
        print(e)

def get_user():
    try:
        USER_ID = input("Enter User ID: ")

        USER = nomad_sdk.get_content(USER_ID, USER_CONTENT_DEFINITION_ID, None)
        print(json.dumps(USER, indent=4))

    except Exception as e:
        print(e)

def update_user():
    try:
        USER_ID = input("Enter User ID: ")

        PROPERTIES = {}
        FIRST_NAME = get_input("First Name", False)
        if FIRST_NAME: PROPERTIES["firstName"] = FIRST_NAME

        LAST_NAME = get_input("Last Name", False)
        if LAST_NAME: PROPERTIES["lastName"] = LAST_NAME

        EMAIL = get_input("Email", False)
        if EMAIL: PROPERTIES["email"] = EMAIL

        USER_STATUS = get_dict("User Status", ["id", "description"], False)
        if USER_STATUS: PROPERTIES["userStatus"] = USER_STATUS

        ORGANIZATION = get_input("Organization", False)
        if ORGANIZATION: PROPERTIES["organization"] = ORGANIZATION

        TITLE = get_input("Title", False)
        if TITLE: PROPERTIES["title"] = TITLE

        PHONE = get_input("Phone", False)
        if PHONE: PROPERTIES["phone"] = PHONE

        PHONE_EXT = get_input("Phone Ext", False)
        if PHONE_EXT: PROPERTIES["phoneExt"] = PHONE_EXT

        MOBILE_PHONE = get_input("Mobile", False)
        if MOBILE_PHONE: PROPERTIES["mobilePhone"] = MOBILE_PHONE

        ADDRESS = get_input("Address", False)
        if ADDRESS: PROPERTIES["address"] = ADDRESS

        ADDRESS2 = get_input("Address2", False)
        if ADDRESS2: PROPERTIES["address2"] = ADDRESS2

        CITY = get_input("City", False)
        if CITY: PROPERTIES["city"] = CITY

        STATE_ID = get_dict("State", ["id", "description"], False)
        if STATE_ID: PROPERTIES["stateId"] = STATE_ID

        POSTAL_CODE = get_input("Postal Code", False)
        if POSTAL_CODE: PROPERTIES["postalCode"] = POSTAL_CODE

        COUNTRY = get_dict("Country", ["id", "description"], False)
        if COUNTRY: PROPERTIES["country"] = COUNTRY

        ASSIGNED_SECURITY_GROUPS = get_list("Security Group", ["id", "description"], False)
        if ASSIGNED_SECURITY_GROUPS: PROPERTIES["assignedSecurityGroups"] = ASSIGNED_SECURITY_GROUPS

        ROLE = get_dict("System Role", ["id", "description"], False)
        if ROLE: PROPERTIES["role"] = ROLE

        nomad_sdk.update_content(USER_ID, USER_CONTENT_DEFINITION_ID, PROPERTIES, None)

    except Exception as e:
        print(e)

def delete_user():
    try:
        USER_ID = input("Enter User ID: ")

        nomad_sdk.delete_content(USER_ID, USER_CONTENT_DEFINITION_ID)

    except Exception as e:
        print(e)

functions = {
    "1": create_user,
    "2": get_user,
    "3": update_user,
    "4": delete_user
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

