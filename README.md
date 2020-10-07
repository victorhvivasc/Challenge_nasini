# Challenge_nasini
Aplicación sencilla para evaluación en proceso de reclutamiento

## python version 3.8.3
## pyrofex==0.3.0

# Ejemplo de consulta:

promt$python challenge.py DOOct20 -u NOMBRE_USUARIO -p CONTRASEÑA -a CUENTA

### parametros:
#### XXXxxXX: Tipo de instrumento
#### -u: Nombre de usuario
#### -p: Contraseña
#### -a: Cuenta

#### Nota: debe respetarse el orden de los parametros a suministrar, en caso contrario se desencadenan errores y posibles soluciones

# Respuesta positiva esperada:

## Iniciando sesión en Remarkets
## Consultando simbolo:   DOOct20
## Ultimo precio operado: $78.86
## Consultando BID
## Precio de BID: $78.85
## Ingresando orden a: $78.84
## Cerrando sesión en Remarkets

# Respuestas negativa esperada:

## - Error:  Simbolo invalido: Implica que fue mal suministrado el tipo de documento.
## - El primer parametro debe ser el tipo de instrumento: Implica que el primer parametro suministrado correspondia a uno de usuario, contraseña, cuenta.
## - Por favor configure el comando con el siguiente formato: >>>python challenge.py INSTRUMENTO -u NOMBRE_USUARIO -p CONTRASEÑA -a CUENTA: Significa que aunque el primer parametro es posiblemente un documento el resto de los parametros estan incompletos.
## - Ingrese el usuario por favor: Significa que el usuario fue ingresado de forma erronea y ofrece solventar la situación reingresando el correcto.
## - Ingrese la contraseña por favor: Significa que la contraseño fue ingresada de forma erronea y ofrece solventar la situación reingresando la correcta.
## - Ingrese la cuenta a utilizar por favor: Significa que la cuenta fue ingresada de forma erronea y ofrece solventar la situación reingresando la correcta.
## - No se pudo concretar la orden, fallo en la cuenta suministrada: Indica que el tipo de cuenta suministrado fue rechazado por el servidor.
## - Error: Authentication fails. Incorrect User or Password: Implica que el usuario o la contraseña suministrada fue rechazada por el servidor.




