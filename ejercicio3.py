vol1 = float(input("Ingrese el primer voltaje: "))
vol2 = float(input("Ingrese el segundo voltaje: "))
vol3 = float(input("Ingrese el tercer voltaje: "))

prom = ((vol1+vol2+vol3)/3)

if prom < 115:
    print("VOLTAJE CORRECTO.")
elif prom >115 and prom <220:
    print("ALTO VOLTAJE.")
elif prom >220:
    print("¡PELIGRO!")