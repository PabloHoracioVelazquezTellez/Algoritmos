"""
Programa para convertir el valor de dolares en yenes redondeando el valor a
solo dos decimales
"""
def usd_cny(x):
    y=x*6.75 #Para convertir el valor
    return f"{y:.2f} Yenes chinos"
usd = int(input("Ingresa la cantidad en dólares "))
conv= usd_cny(usd)
print(conv) #Para mostrar la conversion