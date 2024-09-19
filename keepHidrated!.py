def keep_hidrated(horas):
    import math
    litros=math.floor(horas*0.5)
    return litros
x=float(input("¿Cuantas horas hiciste ciclismo?"))
print("Debes de beber al menos ",keep_hidrated(x),  "litros de agua D:")