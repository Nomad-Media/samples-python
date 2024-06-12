from nomad_media_pip.src.nomad_sdk import Nomad_SDK
from config import config

nomad_sdk = Nomad_SDK(config)

import json

LIVE_OUTPUT_PROFILES = nomad_sdk.get_live_output_profiles()
LIVE_OUTPUT_TYPES = nomad_sdk.get_live_output_types()

def get_live_output_profile_groups():
    profile_groups = nomad_sdk.get_live_output_profile_groups()
    print(json.dumps(profile_groups, indent=4))

def get_live_output_profile_group():
    PROFILE_GROUP_ID = input("Enter the profile group ID: ")

    RESULT = nomad_sdk.get_live_output_profile_group(PROFILE_GROUP_ID)
    print(json.dumps(RESULT, indent=4))

def create_live_output_profile_group():
    print(f"Available live output profiles: {"\n".join([f"{PROFILE['id']}: {PROFILE['name']}" for PROFILE in LIVE_OUTPUT_PROFILES])}")

    NAME = input("Enter the name of the new profile group: ")
    IS_ENABLED = input("Do you want to enable the profile group? (y/n): ") == "y"
    MANIFEST_TYPE = input("Enter the manifest type: (HLS, DASH, or BOTH): ")
    IS_DEFAULT_GROUP = input("Do you want to set this as the default group? (y/n): ") == "y"
    OUTPUT_TYPE_DESCRIPTION = input(f"Enter the output type: ") if input("Do you want to use the default output type? (y/n): ") == "n" else None
    ARCHIVE_LIVE_OUTPUT_PROFILE_DESCRIPTION = input(f"Enter the archive live output profile: ") if input("Do you want to add an archive live output profile? (y/n): ") == "y" else None
    LIVE_OUTPUT_PROFILES_INPUT = []
    while True:
        LIVE_OUTPUT_PROFILE = input(f"Enter a live output: ")
        LIVE_OUTPUT_PROFILES_INPUT.append(next(OUTPUT_PROFILE for OUTPUT_PROFILE in LIVE_OUTPUT_PROFILES if LIVE_OUTPUT_PROFILE == OUTPUT_PROFILE['name']))
        if input("Do you want to add another live output profile? (y/n): ") == "n":
            break

    OUTPUT_TYPE = next((OUTPUT_TYPE for OUTPUT_TYPE in LIVE_OUTPUT_TYPES if OUTPUT_TYPE['description'] == OUTPUT_TYPE_DESCRIPTION), None)
    ARCHIVE_LIVE_OUTPUT_PROFILE = next((PROFILE for PROFILE in LIVE_OUTPUT_PROFILES if PROFILE['name'] == ARCHIVE_LIVE_OUTPUT_PROFILE_DESCRIPTION), None)

    RESULT = nomad_sdk.create_live_output_profile_group(NAME, IS_ENABLED, MANIFEST_TYPE, 
        IS_DEFAULT_GROUP, OUTPUT_TYPE, ARCHIVE_LIVE_OUTPUT_PROFILE, LIVE_OUTPUT_PROFILES_INPUT)
    
    print(json.dumps(RESULT, indent=4))

def update_live_output_profile_group():
    print(f"Available live output profiles: {"\n".join([f"{PROFILE['id']}: {PROFILE['name']}" for PROFILE in LIVE_OUTPUT_PROFILES])}")

    PROFILE_GROUP_ID = input("Enter the profile group ID: ")
    NAME = input("Enter the name of the new profile group: ") if input("Do you want to update the name? (y/n): ") == "y" else None
    IS_ENABLED = input("Do you want to enable the profile group? (y/n): ") == "y" if input("Do you want to update the enabled status? (y/n): ") == "y" else None
    MANIFEST_TYPE = input("Enter the manifest type: (HLS, DASH, or BOTH): ") if input("Do you want to update the manifest type? (y/n): ") == "y" else None
    IS_DEFAULT_GROUP = input("Do you want to set this as the default group? (y/n): ") == "y" if input("Do you want to update the default group status? (y/n): ") == "y" else None
    if input("Do you want to update the output type? (y/n): ") == "y":
        OUTPUT_TYPE_DESCRIPTION = input(f"Enter the output type: ") if input("Do you want to use the default output type? (y/n): ") == "n" else None
    else:
        OUTPUT_TYPE_DESCRIPTION = None 
    ARCHIVE_LIVE_OUTPUT_PROFILE_DESCRIPTION = input(f"Enter the archive live output profile: ") if input("Do you want to update the archive live output profile? (y/n): ") == "y" else None
    LIVE_OUTPUT_PROFILES_INPUT = []
    if input("Do you want to update the live output profiles? (y/n): ") == "y":
        while True:
            LIVE_OUTPUT_PROFILE = input(f"Enter a live output: ")
            LIVE_OUTPUT_PROFILES_INPUT.append(next(OUTPUT_PROFILE for OUTPUT_PROFILE in LIVE_OUTPUT_PROFILES if LIVE_OUTPUT_PROFILE == OUTPUT_PROFILE['name']))
            if input("Do you want to add another live output profile? (y/n): ") == "n":
                break

    OUTPUT_TYPE = next((OUTPUT_TYPE for OUTPUT_TYPE in LIVE_OUTPUT_TYPES if OUTPUT_TYPE['description'] == OUTPUT_TYPE_DESCRIPTION), None)
    ARCHIVE_LIVE_OUTPUT_PROFILE = next((PROFILE for PROFILE in LIVE_OUTPUT_PROFILES if PROFILE['name'] == ARCHIVE_LIVE_OUTPUT_PROFILE_DESCRIPTION), None)

    RESULT = nomad_sdk.update_live_output_profile_group(PROFILE_GROUP_ID, NAME, IS_ENABLED, MANIFEST_TYPE, 
        IS_DEFAULT_GROUP, OUTPUT_TYPE, ARCHIVE_LIVE_OUTPUT_PROFILE, LIVE_OUTPUT_PROFILES_INPUT)
    
    print(json.dumps(RESULT, indent=4))

def delete_live_output_profile_group():
    PROFILE_GROUP_ID = input("Enter the profile group ID: ")

    nomad_sdk.delete_live_output_profile_group(PROFILE_GROUP_ID)

functions = {
    "1": get_live_output_profile_groups,
    "2": get_live_output_profile_group,
    "3": create_live_output_profile_group,
    "4": update_live_output_profile_group,
    "5": delete_live_output_profile_group
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
