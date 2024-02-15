from usuarios.conexion import *
from datetime import datetime
import hashlib

class Usuario:
    #Crear el metodo constructor para inciar los metodos necesarios
    def __init__(self, id,saldo, nombre, apellido, email, password):
        self.id = id
        self.saldo = saldo
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password

    #Cargar los datos que ya le pasamos en el formulario (acciones) a la base de datos
    def registrar(self):
        fecha = datetime.now()

        cifrado = hashlib.sha1()
        cifrado.update(self.password.encode('utf8'))


        sql = "INSERT INTO usuario VALUES(%s, DEFAULT, %s, %s, %s, %s, %s)"
        usuario = (self.id, self.nombre, self.apellido, self.email, cifrado.hexdigest(), fecha)

        
        try:
            cursor.execute(sql, usuario)
            database.commit()

            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result

    
    def identificar(self):
        sql = "SELECT * FROM usuario WHERE email = %s and passwd = %s"
        
        #cifrado de contraseñas
        cifrado = hashlib.sha1()
        cifrado.update(self.password.encode('utf8'))

        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result


    def updateSaldo(self):
        sql = "UPDATE `usuario` SET `saldo`=%s WHERE id = %s"
        d = (self.saldo, self.id)
        
        cursor.execute(sql, d)
        database.commit()

        return [cursor.rowcount, self]
    
    