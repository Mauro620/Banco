import transactions.trx as modelo
import usuarios.usuario as pack

class Acciones:
    def transar(self, ingreso):
        remitente = ingreso[4]
        monto = float(input("Ingresa el valor a enviar: "))
        destiny = input("Indgresa la cuenta de destino: ")
        descripcion = input("Descripción: ")

        des = [destiny]
        u = modelo.Trx('', '', '', des, '').identificarDest()
        if u[4] == destiny:
            trans = modelo.Trx('' , remitente, monto, destiny, descripcion)
            enviar = trans.enviar()

            if enviar[0] >= 1:
                print(f"Transacción hecha correctamente por {enviar[1].monto} COP")

            nsaldo2 = u[1] + monto
            
            nsaldo = ingreso[1] - monto
            pack.Usuario(ingreso[0], nsaldo, '', '', '','').updateSaldo()
            pack.Usuario(u[0], nsaldo2, '', '', '','').updateSaldo()
            
        else:
            print("No se pudo encontrar el destinatario")
        

    def search(self, user):
        remitente = [user[4]]

        trans = modelo.Trx('' , remitente, '', '', '')
        f = trans.consultar()

        for i in f:
            print(i)




        