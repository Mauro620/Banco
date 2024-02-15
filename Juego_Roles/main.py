from mounstros import *

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