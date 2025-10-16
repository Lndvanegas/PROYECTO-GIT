def area_poligono(lados, apotema):
    return (lados * apotema) / 2

lados=int(input("Ingrese el numero de lados del polígono: "))
apotema=float(input("Ingrese la longitud del apotema en centimetros: "))
print("El área del poligono regular es:", area_poligono(lados, apotema), "cm²")