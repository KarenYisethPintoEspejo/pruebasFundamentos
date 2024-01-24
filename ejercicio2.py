base = float(input("Ingrese la base del triangulo: "))
altura = float(input("Ingrese la altura del triangulo: "))
area = (base*altura)/2

if area > 1000:
    print ("DATOS NO VALIDOS.")

elif base == altura:
    print(f"El area del triangulo equilatero es de: {area}")
else:
    print ("No es triangulo equilatero.")