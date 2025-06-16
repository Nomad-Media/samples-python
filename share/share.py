from nomad_media_pip.src.nomad_sdk import Nomad_SDK
from config import config

nomad_sdk = Nomad_SDK(config)

import json

def get_input(prompt, required):
    return input(f"Enter {prompt}: ") if required or input(f"Do you want to add {prompt} (y/n): ") == "y" else None

def get_bool(prompt):
    return True if input(f"{prompt} (y/n): ") == "y" else False

def get_dict(prompt, keys, required):
    return {key: input(f"Enter {prompt} {key}: ") for key in keys} if required or input(f"Do you want to add {prompt} (y/n): ") == "y" else None

def get_list(prompt, keys=None, required=False):
    items = []
    if required or input(f"Do you want to add {prompt} (y/n): ") == "y":
        while True:
            if keys:
                items.append(get_dict(prompt, keys, True))
            else:
                items.append(input(f"{prompt}: "))
            if input(f"Do you want to add another {prompt} (y/n): ") == "n":
                break
    return items if len(items) > 0 else None

def share():
    try:
        id = get_input("share id", False)
        name = get_input("name", False)
        shared_contents = get_list("shared content", required=False)
        shared_duration = get_dict("shared duration", ["id"], False)
        shared_permissions = get_list("shared permission", ["id", "description"], False)
        shared_type = get_dict("shared type", ["id", "description"], False)
        shared_status = get_dict("shared status", ["id", "description"], False)
        shared_duration_in_hours = get_input("shared duration in hours", False)
        shared_link = get_input("shared link", False)
        owner_id = get_input("owner id", False)
        expiration_date = get_input("expiration date", False)
        nomad_users = get_list("nomad user", ["id", "description"], False)

        response = nomad_sdk.share(
            id,
            name,
            shared_contents,
            shared_duration,
            shared_permissions,
            shared_type,
            shared_status,
            int(shared_duration_in_hours) if shared_duration_in_hours else None,
            shared_link,
            owner_id,
            expiration_date,
            nomad_users
        )
        print(json.dumps(response, indent=4))
    except Exception as e:
        raise e

def get_share():
    try:
        share_id = get_input("share id", True)
        response = nomad_sdk.get_share(share_id)
        print(json.dumps(response, indent=4))
    except Exception as e:
        raise e

def delete_share():
    try:
        share_id = get_input("share id", True)
        response = nomad_sdk.delete_share(share_id)
        print(json.dumps(response, indent=4))
    except Exception as e:
        raise e

def update_share():
    try:
        share_id = get_input("share id", True)
        id = get_input("id", False)
        name = get_input("name", False)
        shared_contents = get_list("shared content", required=False)
        shared_duration = get_dict("shared duration", ["id"], False)
        shared_permissions = get_list("shared permission", ["id", "description"], False)
        shared_type = get_dict("shared type", ["id", "description"], False)
        shared_status = get_list("shared status", ["id", "description"], False)
        shared_duration_in_hours = get_input("shared duration in hours", False)
        shared_link = get_input("shared link", False)
        owner_id = get_input("owner id", False)
        expiration_date = get_input("expiration date", False)
        nomad_users = get_list("nomad user", ["id", "description"], False)

        response = nomad_sdk.update_share(
            share_id,
            id,
            name,
            shared_contents,
            shared_duration,
            shared_permissions,
            shared_type,
            shared_status,
            int(shared_duration_in_hours) if shared_duration_in_hours else None,
            shared_link,
            owner_id,
            expiration_date,
            #nomad_users
        )
        print(json.dumps(response, indent=4))
    except Exception as e:
        raise e

def share_expire():
    try:
        share_id = get_input("share id", True)
        nomad_sdk.share_expire(share_id)
        print("Share expired successfully.")
    except Exception as e:
        raise e

def share_notification():
    try:
        share_id = get_input("share id", True)
        nomad_users = get_list("nomad user", ["id"], False)
        external_users = get_list("external user", ["id"], False)
        #nomad_sdk.share_notification(share_id, nomad_users, external_users=external_users)
        print("Share notification sent successfully.")
    except Exception as e:
        raise e

functions = {
    "1": share,
    "2": get_share,
    "3": delete_share,
    "4": update_share,
    "5": share_expire,
    "6": share_notification
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