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
#prueba 1
get_kit_body1 = { "name": "a"}
#prueba 2
get_kit_body2 = { "name": '''Abcdabcdabcdabcdabcdabcdabcdabcdabcdab'''
                 '''cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc'''
                 '''dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab'''
                 ''''cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda'''
                 '''bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab'''
                 '''cdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabc'''
                '''dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab'''
                 '''cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda'''
                 '''bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd'''
                 '''abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC'''}
#prueba 3
get_kit_body3 = { "name": "" }