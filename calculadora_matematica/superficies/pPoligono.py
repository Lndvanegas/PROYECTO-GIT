def pPoligono(longitud, lados):
    return longitud * lados
longitud = float(input("Ingrese el valor de la longitud de un lado : "))
lados = float(input("Ingrese el numero de lados: "))
p = longitud * lados
print(f"El perímetro del poligono es: {p:.1f} cm")