import requests
from requests.auth import HTTPBasicAuth

import json

# Configuration
# Replace with your openEHR server URL
BASE_URL = "http://localhost:8080/ehrbase/rest/openehr/v1/ehr"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}
USERNAME = 'ehrbase-user'
PASSWORD = 'SuperSecretPassword'

# Function to create a new EHR


def create_ehr():
    url = f"{BASE_URL}"
    body = {
        "archetype_node_id": "openEHR-EHR-EHR_STATUS.generic.v1",
        "name": {
            "value": "EHR status"
        },
        "_type": "EHR_STATUS",
        "uid": {
            "_type": "OBJECT_VERSION_ID",
            "value": "8849182c-82ad-4088-a07f-48ead4180515::openEHRSys.example.com::1"
        },
        "subject": {
            "_type": "PARTY_SELF"
        },
        "is_queryable": True,
        "is_modifiable": True
    }
    headers = {**HEADERS, "Prefer": "return=representation"}
    response = requests.post(
        url, headers=headers, auth=HTTPBasicAuth(
            USERNAME, PASSWORD), json=body)
    if response.status_code == 201:
        print(f"EHR created: {json.dumps(response.json(), indent=2)}")
        return response.json()["ehr_id"]
    else:
        print(
            f"Failed to create EHR {response} {response.content} {response.headers} {response.status_code}")
        print(f"{response.headers['Location']}")
        return None

# Function to get EHR details by EHR ID


def get_ehr(ehr_id: str):
    print(f"get_ehr: {ehr_id}")
    url = f"{BASE_URL}/{ehr_id}"
    response = requests.get(
        url, headers=HEADERS, auth=HTTPBasicAuth(
            USERNAME, PASSWORD))
    if response.status_code < 300:
        print(f"EHR details: {json.dumps(response.json(), indent=2)}")
    else:
        print(
            f"Failed to get EHR {response} {response.content} {response.headers} {response.status_code}")

# Main function to run the script


def main():
    # Create a new EHR
    print("Creating a new EHR...")
    ehr_id = create_ehr()

    # If EHR creation was successful, retrieve the details
    if ehr_id:
        print("Getting EHR details...")
        get_ehr(ehr_id["value"])


if __name__ == "__main__":
    main()
