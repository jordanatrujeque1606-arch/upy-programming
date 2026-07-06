#problema9
Usuario_correcto= "admi"
contraseña_correcta= "1234"
Usuario_ingresado=input("ingrese el usuario")
contraseña_ingresada=input("ingrese la contraseña")
if Usuario_ingresado==Usuario_correcto:    
    if contraseña_ingresada==contraseña_correcta:
        print("bienvenido")
    else:    
            print("contraseña incorrecta")
else:
    print("usuario desconocido")