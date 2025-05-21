
import configuration
import data
import requests
import sender_stand_request
from sender_stand_request import modify_body


def positive_assert():
    response = sender_stand_request.post_new_client_kit()
    assert response.status_code == 201


def negative_assert(dict):
    response = sender_stand_request.post_new_client_kit(dict)
    assert response.status_code == 400

# prueba 1 El número permitido de caracteres (1):

def test1_with_one_character():
    positive_assert("a")

# { "name": " A Aaa " }
def test6_create_kit_with_space_name():
    positive_assert("A Aaa")

def test_prueba ():
    negative_assert("@#")




''''

#	Prueba 2: El número permitido de caracteres (511):

def _get_kit_body():
    response = sender_stand_request.post_new_user().json()
    #print(response)
    new_header = data.header_kit.copy()
    new_header['Authorization'] = "Bearer " + response["authToken"]
    #print(new_header)
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=data.get_kit_body2,
                         headers=new_header)




# Prueba 3:El número de caracteres es menor que la cantidad permitida (0):

def _get_kit_body():
    response = sender_stand_request.post_new_user().json()
    new_header = data.header_kit.copy()
    new_header['Authorization'] = "Bearer " + response["authToken"]
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=data.get_kit_body3,
                         headers=new_header)



def check_characters():
    #response = sender_stand_request.post_new_client_kit().json()
    response = get_kit_body()
    assert test_get_kit_body().json()["name"] == ""
    assert response['code'] == 201

#positive_answer = check_characters()


def negative_assert():
    response = data.get_kit_body3
    assert response.status_code == 400

'''





