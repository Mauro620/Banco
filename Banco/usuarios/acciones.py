import usuarios.usuario as modelo
from os import system
import transactions.acciones as trx


class Acciones:
    def registro(self):
        print("EXCELENTE, VAMOS A REGISTRARTE \n")

        id = input("¿Cual es tu numero de documento?:\n ")
        nombre = input("¿Cual es tu nombre?: \n")
        apellidos = input("¿Cuales son tus apellidos?: \n")
        email = input("¿Cual es tu email?: \n")
        password = input("Introduce una contraseña: ")

        # Le paso todos los datos ingresados por consola al modelo usuario
        usuario = modelo.Usuario(id, "", nombre, apellidos, email, password)
        # registrar es la funcion que me carga todos los datos a la base de datos
        registro = usuario.registrar()

        if registro[0] >= 1:
            system("clear")
            print(
                f"\n PERFECTO {registro[1].nombre} TE HAS REGISTRADO CON EL EMAIL {registro[1].email}"
            )

        else:
            print(
                "PARECE QUE ALGO HA SALIDO MAL, VALIDA TUS DATOS E INTENTA NUEVAMENTE"
            )

    def login(self):
        print("Vamos a ingresar \n")

        email = input("¿Cual es tu email?: \n")
        password = input("Introduce tu contraseña: \n")

        user = modelo.Usuario("", None, "", "", email, password)
        ingreso = user.identificar()

        if email == ingreso[4]:
            # system("clear")
            print(f"BIENVENIDO {ingreso[2]}, HAS INGRESADO CON EL EMAIL {ingreso[4]}")
            self.nextAction(ingreso)

        """
        try:
        except Exception as e:
            print(type(e))
            print(type(e))
            print("¡OH! PARECE QUE ALGO HA SALIDO MAL, VALIDA TUS DATOS E INTENTA NUEVAMENTE")
"""

    def nextAction(self, ingreso):
        print(
            """
        ¿Que deseas hacer?
            -Ver saldo (saldo)
            -Realizar transacción (trx)
            -Ver todas las transacciones(ver)
            -Cerrar sesión (salir)
        """
        )

        accion = input("Ingresa la acción: \n")

        haz = trx.Acciones()

        if accion == "saldo":
            print(f"\n TU SALDO ES: {ingreso[1]} \n")
            self.nextAction(ingreso)

        elif accion == "trx":
            print("vamos a transar")
            haz.transar(ingreso)
            self.nextAction(ingreso)

        elif accion == "ver":
            print("vamos a transar")
            haz.search(ingreso)
            self.nextAction(ingreso)

        elif accion == "salir":
            print(f"ADIOS {ingreso[2]}")
            exit()
        else:
            print("Ingrese una orden valida")
        return None
