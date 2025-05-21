import configuration
import data
import requests

#create new user
def post_create_user():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json = data.user_body,
                         headers = data.headers)

#create kit with dictionary copy and token
def post_create_new_kit(name):
    response = post_create_user().json()
    new_header = data.header_kit.copy()
    new_header['Authorization'] = "Bearer " + response["authToken"]
    new_body = modify_body(name)
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json = new_body,
                         headers= new_header)


def modify_body(name):
    body = data.kit_body.copy()
    body['name'] = name
    return body

