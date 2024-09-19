def rango_edades(edad):
    if edad>=1 and edad<=100:
        if edad<=14:
            print("Las ecuaciones no funcionan para tu edad, intenta en unos años.")
            return None
        else:
            minimo=int(edad/2)+7
            maximo=int(edad-7)*2
    else:
        print("Edad Invalida.")
        return None
    return minimo,maximo
x=int(input("Ingrese el valor de la edad: "))
print(rango_edades(x))