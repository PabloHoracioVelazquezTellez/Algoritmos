def extrapolate_ppg(ppg, mpg):
    # Si PPG o MPG es 0, el resultado es 0
    if mpg == 0:
        return 0
    # Extrapolación de PPG a 48 minutos
    ppg_48 = (ppg / mpg) * 48
    # Redondear a un decimal
    return round(ppg_48, 1)

# Ejemplo de uso
ppg = float(input("Introduce los puntos por juego (PPG): "))
mpg = float(input("Introduce los minutos por juego (MPG): "))
print(f"Puntos extrapolados a 48 minutos: {extrapolate_ppg(ppg, mpg)}")
