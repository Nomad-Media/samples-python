from nomad_media_pip.src.nomad_sdk import Nomad_SDK
from config import config

nomad_sdk = Nomad_SDK(config)

import json

def get_input(prompt, required):
    return input(f"Enter {prompt}: ") if required or input(f"Do you want to add {prompt} (y/n): ") == "y" else None

def get_dict(prompt, keys, required):
    return {key: input(f"Enter {prompt} {key}: ") for key in keys} if required or input(f"Do you want to add {prompt} (y/n): ") == "y" else {}

def get_list(prompt, keys, required):
    items = []
    if required or input(f"Do you want to add {prompt} (y/n): ") == "y":
        while True:
            items.append({key: input(f"Enter {prompt} {key}: ") for key in keys})
            if not required or input(f"Do you want to add another {prompt} (y/n): ") == "n":
                break
    return items

def get_bool(prompt):
    return True if input(f"{prompt} (y/n): ") == "y" else False

def create_job():
    try:
        bucketName = get_input("bucket name", True)
        objectKey = get_input("object key", True)
        notificationCallbackUrl = get_input("notification callback url", True)
        externalId = get_input("external id", True)
        replaceExistingJob = get_bool("replace existing job")
        assetUrl = get_input("asset url", False)
        requestedTasks = get_list("requested task", ["task"], False)
        requestedTranscodeProfiles = get_list("requested transcode profile", ["profile"], False)

        created_job = nomad_sdk.create_job(
            bucketName,
            objectKey,
            notificationCallbackUrl,
            externalId,
            replaceExistingJob,
            assetUrl=assetUrl,
            requestedTasks=requestedTasks,
            requestedTranscodeProfiles=requestedTranscodeProfiles
        )
        
        print(json.dumps(created_job, indent=4))
    except Exception as e:
        raise e

def create_job_id():
    try:
        asset_id = get_input("asset id", True)
        job_results_url = get_input("job results url", True)
        externalId = get_input("external id", False)
        
        nomad_sdk.create_job_id(
           #asset_id,
           #job_results_url,
           #externalId=externalId
        )
        
        print("Job created successfully")
    except Exception as e:
        raise e

functions = {
    "1": create_job,
    "2": create_job_id
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