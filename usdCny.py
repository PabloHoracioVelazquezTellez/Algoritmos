def usd_cny(x):
    y=x*6.75 #Para convertir el valor
    return f"{y:.2f} Yuanes chinos"
usd = int(input("Ingresa la cantidad en dólares "))
conv= usd_cny(usd)
print(conv) #Para mostrar la conversion