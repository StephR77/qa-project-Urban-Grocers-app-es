#create a user
headers = {"Content-Type": "application/json"}

user_body ={
    "firstName": "Max",
    "phone": "+10005553535",
    "address": "8042 Lancaster Ave.Hamburg, NY"
}

#create a new kit
header_kit = {
    "Content-Type": "application/json"}

kit_body = {
    "name": "New Kit",
    "cardId": 1
}

characters_one = { "name" : "a"}

characters_511 = {"name" :'Abcdabcdabcdabcdabcdabcdabcdabcda'
'bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc'
'dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab'
'cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab'
'cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc'
'dabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcd'
'abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab'
'cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd'
'abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc'
'dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC'}

cero_characters = {"name": ""}

characters_512 = {"name" :'Abcdabcdabcdabcdabcdabcdabcdabcda'
'bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc'
'dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab'
'cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab'
'cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc'
'dabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcd'
'abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab'
'cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd'
'abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc'
'dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcA'}

special_characters = {"name": "№%@,"}

space_in_between = {"name": "A Aaa"}

numbers = {"name": "123"}

no_character = {"name":{}}

not_allowed = {"name": "123"}
