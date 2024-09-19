"""
Programa para adaptar el tamaño de una resolucion "x" a una equivalente en
aspecto 16:9
"""
import math
def convert_to_16_9(x, y):
    # Calcula la nueva resolución X' manteniendo el valor de Y
    new_x = math.ceil((16 / 9) * y)
    return new_x, y

# Prueba del programa
x, y = 1440, 1080  # Resolución arbitraria
new_x, new_y = convert_to_16_9(x, y)
print(f"La nueva resolución con aspecto 16:9 es: {new_x}x{new_y}")
