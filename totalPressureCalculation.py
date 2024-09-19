"""
Programa que calcula la presion total de la mezcla de dos gases en un contenedor
"""
def calcular_presion_total(M1, M2, m1, m2, V, T_celsius):
    R = 0.082  # Constante de los gases en dm^3·atm·K^−1·mol^−1
    T_kelvin = T_celsius + 273.15  # Convertir temperatura a Kelvin
    # Calcular los moles de cada gas
    moles_gas_1 = m1 / M1
    moles_gas_2 = m2 / M2
    # Sumar los moles de ambos gases
    moles_totales = moles_gas_1 + moles_gas_2
    # Calcular la presión total
    P_total = (moles_totales * R * T_kelvin) / V
    return P_total
M1 = 18  # g/mol   #EJEMPLO DE USO
M2 = 44  # g/mol
m1 = 10  # g
m2 = 20  # g
V = 10  # dm^3
T = 25  # °C
presion = calcular_presion_total(M1, M2, m1, m2, V, T)
print(f"La presión total es: {presion:.2f} atm")
