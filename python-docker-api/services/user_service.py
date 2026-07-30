import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_endpoint = os.getenv("BACKENDAPIENDPOINT")


def get_all_users():

    response = requests.get(api_endpoint + "/users")
    response.raise_for_status()

    return response.json()


def get_user_by_id(user_id):

    response = requests.get(api_endpoint + "/users/" + str(user_id))
    response.raise_for_status()

    return response.json()


def get_user_company(user_id):

    response = requests.get(api_endpoint + "/users/" + str(user_id))
    response.raise_for_status()

    user = response.json()

    return user["company"]


def get_user_address(user_id):

    response = requests.get(api_endpoint + "/users/" + str(user_id))
    response.raise_for_status()

    user = response.json()

    return user["address"]


def get_user_bank(user_id):

    response = requests.get(api_endpoint + "/users/" + str(user_id))
    response.raise_for_status()

    user = response.json()

    return user["bank"]


def get_user_hair(user_id):

    response = requests.get(api_endpoint + "/users/" + str(user_id))
    response.raise_for_status()

    user = response.json()

    return user["hair"]


def get_user_crypto(user_id):

    response = requests.get(api_endpoint + "/users/" + str(user_id))
    response.raise_for_status()

    user = response.json()

    return user["crypto"]