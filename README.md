# Proyecto Urban Grocers 
Yury Stefany Rodriguez R, grupo 29, sprint 7

PROYECTO URBAN GROCERS

Primero se tiene que abrir una archivo llamado configuration.py para alojar las URL del servidor, la dirección API para crear un usuario y la dirección API para crear un kit.

Luego en otro archivo llamado data.py vamos a alojar los parámetros requeridos para la creación de un usario que los requerimientos son: un encabezado en "content-Type" y un diccionario con los datos del usuario, por lo que los datos mínimos son: firstname, phone, address. Además de esto, se necesitan los requerimientos para crear un kit que son: "obligatorio pasar el encabezado Authorisation O el parámetro cardId, para crear la kit".

En seguida, debemos abrir un archivo llamado sender_stand_request.py para importar los datos del archivo configuration, data y requests de python para luego asi poder correr los tests.

En este archivo se empiezan a diseñar las funciones para crear un usuario y dentro de este crear un kit, de la misma manera se crea la copia de un diccionario para realizar las pruebas negativas y positivas de la aplicación de Urban Grocers.

Para crear un usuario se necesita traer la información desde el archivo configuration.py con la URL del servidor y el end point de API para crearlo, de esta manera como el requerimiento es que el usuario contenga un content-type y un encabezado, alli lo mencionamos con las variables json y headers para que no nos de un error.

Luego para crear un kit dise;amos una función con el nombre de post_create_new_kit y dentro de esta llamamos a la función de crear un usuario con la variable 'response', para que podamos conseguir el autotoken, a continuación para la creación de un kit se necesita un content-type y un authoken que el usario no los da al ser una respuesta positiva, de esta manera comprobamos la creacion del kit. Luego le decimos a la función de post_create_new_kit que retorne esta información desde la pagina configuración URL y la API kits_path.

Para poder empezar a realizar los tests de comprobación, se creó una función a parte para poder modificar el kit con los diferentes parámetros propuestos por la aplicación llamada modify_body la cual, se inserta tambien en la función post_create_new_kit llamandola con la variable new_body y json para las pruebas positivas y negativas de nuestro kit.  

Luego de tener casi todo listo, en el archivo create_kit_name_kit_test.py definimos las funciones de positive_assert y negative_assert en donde empezaremos a realizar los tests de las comprobaciones. Para estas dos funciones le decimos que retome la información del kit que se quiere modificar desde sender_stand_request.post_create_new_kit y le decimos que el assert sea un codigo 201 si es positivo o 400 si es negativo.

Finalmente, al correr las pruebas, se tiene aún fallos en el programa con respecto al test 3 (kit con número de caracteres menor a uno), test 4 (kit con 512 caracteres), test 8 (kit con no caracteres) y test 9 (kit con números) pues nos da un resultado 201 y este debería reflejar un error 400.

Para finalizar este archivo junto con los demás (configuration.py, data.py, sender_stand_request.py, create_kit_name_kit_test.py, README.md, y .gitignore) estarán guardados en git.hub por medio de la clonación en el terminal de Cmder.
