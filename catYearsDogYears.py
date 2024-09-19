"""
Programa que calcula la edad de un gato
y un perro con respecto a los años humanos
"""
def calculate_pet_years(humanYears):
    dogYears=0
    catYears=0
    if humanYears == 1:
        catYears = 15
        dogYears = 15
    elif humanYears == 2:
        catYears = 15 + 9
        dogYears = 15 + 9
    else:
        catYears = 15 + 9 + (humanYears - 2) * 4
        dogYears = 15 + 9 + (humanYears - 2) * 5
    return {'Edad Humana': humanYears,
            'Edad en gatos': catYears,
            'Edad en perros': dogYears}
#Para probar el programa
humanYears = 10  # Para cambiar los resultados de la funcion
print(calculate_pet_years(humanYears))
print(type(calculate_pet_years(humanYears)))
print("Primer cambio al codigo :DDD")