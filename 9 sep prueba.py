capacidad_max = 250.0
masa_total = 0
contador = 0
sobrecarga = False

peso = float(input("Escriba el peso del saco (0 para finalizar): "))

while masa_total < 250.0 and peso != 0.0 and sobrecarga == False:
    if masa_total + peso > capacidad_max:
        sobrecarga = True
        print("La tolva está llena, el saco no fue aceptado.")
    else:
        masa_total += peso
    contador += 1
    if masa_total < 250.0 and sobrecarga == False:
        peso = float(input("Escriba el peso del saco (0 para finalizar): "))
porcentaje = (masa_total/capacidad_max) * 100

print("\n-Reporte Final:")
print("Cantidad de sacos ingresados:", contador)
print("Masa final cargada:", masa_total, "kg")
print("Porcentaje de capacidad utilizado:", porcentaje, "%")