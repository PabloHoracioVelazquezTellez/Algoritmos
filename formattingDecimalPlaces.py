from math import trunc
def redondeo(n):
    x=n
    y=f"{x:.2f}"
    return print(x," es redondeado a ",y)
a=float(input("Ingrese un numero con multiples decimales: "))
redondeo(a)