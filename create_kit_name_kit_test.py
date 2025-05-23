import data
import sender_stand_request


def positive_assert(name):
    response = sender_stand_request.post_create_new_kit(name)
    if response.status_code == 201:
        print(f'successfully created {response.status_code}')


def negative_assert(name):
    response = sender_stand_request.post_create_new_kit(name)
    assert response.status_code == 400

# prueba 1 El número permitido de caracteres (1):

def test1_with_one_character():
    positive_assert(data.characters_one)


# prueba 2 el número permitido de caracteres (511)
def test2_with_511_characters():
    positive_assert(data.characters_511)

# prueba 3 el número de caracteres es menor a (cero)
def test3_with_cero_character():
    negative_assert(data.cero_characters)

#prueba 4 mayor numero de caracteres permitido
def test4_with_512_characters():
    negative_assert(data.characters_512)

# prueba 5 se permiten caracteres especiales
def test5_with_special_characters ():
    positive_assert(data.special_characters)

# prueba 6 espacios entre el nombre
def test6_name_with_space_in_between():
    positive_assert(data.space_in_between)

# prueba 7 se permiten números
def test7_with_numbers():
    positive_assert(data.numbers)

# prueba 8 el caracter no se pasa en la solicitud
def test8_no_characters():
    negative_assert(data.no_character)

# prueba 9 no se permiten números
def test9_numbers_not_allowed():
    negative_assert(data.not_allowed)




