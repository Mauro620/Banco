import random

class Monstruo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ataque = random.randint(0, 5000)
        self.defensa = random.randint(0, 5000)
        self.salud = 6000

    def atacar(self, otro_monstruo):
        dano = self.ataque - otro_monstruo.defensa
        if random.random() < 0.1:  # 10% de probabilidad de golpe crítico
            dano *= 2
            print("¡Golpe crítico!")
        otro_monstruo.salud -= dano
        if otro_monstruo.salud < 0:
            otro_monstruo.salud = 0
        print(f"{self.nombre} ataca a {otro_monstruo.nombre} y le hace {dano} puntos de daño.")
        print(f"{otro_monstruo.nombre} tiene {otro_monstruo.salud} puntos de salud restantes.")

# Crear los monstruos
monstruo1 = Monstruo("Asesino de gallinazos")
monstruo2 = Monstruo("Devorador de butifarras")

# Pelea por turnos
while monstruo1.salud > 0 and monstruo2.salud > 0:
    # Turno del monstruo 1
    monstruo1.atacar(monstruo2)
    if monstruo2.salud <= 0:
        break

    # Turno del monstruo 2
    monstruo2.atacar(monstruo1)
    if monstruo1.salud <= 0:
        break

# Resultado de la pelea
print("\n¡La pelea ha terminado!")
if monstruo1.salud > monstruo2.salud:
    print(f"{monstruo1.nombre} ha ganado la pelea.")
elif monstruo2.salud > monstruo1.salud:
    print(f"{monstruo2.nombre} ha ganado la pelea.")
else:
    print("¡Ha sido un empate!")
