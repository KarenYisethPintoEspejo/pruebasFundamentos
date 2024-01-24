vol1 = float(input("Ingrese el primer voltaje: "))
vol2 = float(input("Ingrese el segundo voltaje: "))
vol3 = float(input("Ingrese el tercer voltaje: "))
vol4 = float(input("Ingrese el cuarto voltaje: "))
vol5 = float(input("Ingrese el quinto voltaje: "))

prom = ((vol1+vol2+vol3+vol4+vol5)/5)
if prom > 220:
    print("ALTO VOLTAJE")
else:
    print("VOLTAJE CORRECTO")
    