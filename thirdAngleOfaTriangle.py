"""
Programa para calcular el valor de un angulo X de un triangulo
haciendo uso del valor de sus otros dos angulos
"""
def tercer_angulo(x,y):
    if x >0 and y>0 and x+y <180:
        z=180-(x+y) #La suma de los angulos de un triangulo siempre da 180 grados como resultado
    else:
        z= False
    return z
a1=int(input("Ingresa el valor de tu primer angulo:"))
a2=int(input("Ingresa el valor de tu segundo angulo:"))
a3=tercer_angulo(a1,a2)
if a3:
    print("El tercer ángulo es igual a", a3, "grados.")
else:
    print("Los ángulos proporcionados no son válidos.")