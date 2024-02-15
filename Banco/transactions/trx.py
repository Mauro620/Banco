import usuarios.conexion as conexion
from datetime import datetime


class Trx:
    def __init__(self,reference,remitente, monto, destiny, descripcion):
        self.reference = reference
        self.remitente = remitente
        self.monto = monto
        self.destiny = destiny
        self.descripcion = descripcion

    def enviar(self):
        fecha = datetime.now()
        sql = "INSERT INTO transaction VALUES(null, %s, %s, %s, %s, %s)"
        transaccion = (self.monto, self.remitente, self.destiny, self.descripcion, fecha)

        conexion.cursor.execute(sql, transaccion)
        conexion.database.commit()

        result = [conexion.cursor.rowcount, self]

        return result
        

    def consultar(self):
        sql = "SELECT * FROM transaction WHERE remitente = %s"
        d = (self.remitente)

        conexion.cursor.execute(sql, d)
        result = conexion.cursor.fetchall()

        print(self.remitente)

        return result

    def identificarDest(self):
        sql = "SELECT * FROM usuario WHERE email = %s"
        usuario = (self.destiny)

        conexion.cursor.execute(sql, usuario)

        result = conexion.cursor.fetchone()
        return result
    