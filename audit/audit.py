from nomad_media_pip.src.nomad_sdk import Nomad_SDK
from config import config

nomad_sdk = Nomad_SDK(config)

import json

def get_audit():
    try:
        ID = input("Enter id: ")

        AUDIT = nomad_sdk.get_audit(ID)

        print(json.dumps(AUDIT, indent=4))
    except:
        raise Exception()
    
if __name__ == "__main__":
    get_audit()