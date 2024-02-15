from usuarios import acciones
from os import system

#Acciones disponibles para que el usuario ingrese 
print("""---------BIENVENIDO-----------
Acciones:
    -ingresar
    -registrar
    -salir
""")

validar = True
#Modelado de preguntas registro y login
while validar == True:
    accion = input("\n --------¿QUÉ DESEAS HACER?----------- \n").lower()

    #Hacer el llamado a la clase para ejecutar las funciones
    haz= acciones.Acciones()

    if accion == "registrar":
        haz.registro()

    elif accion == "ingresar":
        validar = False
        haz.login()
    
    elif accion == "salir":
        validar = False
        print("HASTA PRONTO")

    else:
        print("\n ¡Vaya! parece que no te entendi por favor ingresa una accion valida: \n")