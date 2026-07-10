# Ejercicio: Verificación de acceso
USUARIO_CORRECTO = "admin"
CLAVE_CORRECTA = "12345"
usuario_ingresado = input("Introduce tu nombre de usuario: ")
clave_ingresada = input("Introduce tu contraseña: ")
if usuario_ingresado == USUARIO_CORRECTO and clave_ingresada == CLAVE_CORRECTA:
    print("¡Acceso concedido! Bienvenido al sistema.")
else:
    print("Acceso denegado. Usuario o contraseña incorrectos.")