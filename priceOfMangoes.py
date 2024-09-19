"""
Programa para saber cuantas ofertas de 3x2 recibe un cliente
por la cantidad de mangos que comprara y cuantos mangos quedaran fuera de
promocion
"""
def calcular_ofertas_3x2(cantidad_mangos):
    # Calcular cuántas ofertas de 3x2 se aplican
    ofertas = cantidad_mangos // 3
    # Calcular cuántos mangos adicionales quedan fuera de las ofertas
    mangos_sueltos = cantidad_mangos % 3
    return ofertas, mangos_sueltos

# Ejemplo de uso
cantidad_mangos = int(input("¿Cuántos mangos llevas?: "))
ofertas, mangos_sueltos = calcular_ofertas_3x2(cantidad_mangos)

print(f"Se aplican {ofertas} ofertas de 3x2.")
if mangos_sueltos > 0:
    print(f"Te quedan {mangos_sueltos} mangos fuera de la oferta.")
else:
    print("Todos los mangos entran en la oferta.")
