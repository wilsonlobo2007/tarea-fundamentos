# Curso: Fundamentos de Tecnología Digitales
# Profesor: Adonis Aleman G.
# Estudiante: Wilson Jafeth Lobo Mora

provincia = input("su paquete se dirige a: ")
peso = float(input("¿Cual es el peso de su paquete?: "))

if provincia == "alajuela":
    if peso > 3:
        if peso <= 5:
            print("el precio a pagar es 15$")
        else:
         print("el precio a pagar es 21$")
    else:
        print("el precio a pagar es 5$")
else:
    if provincia == "heredia":
        if peso > 3:
            if peso <= 5:
                print("el precio a pagar es 21$")
        else:
            print("el precio a pagar es 35$")
    else:
        print("el precio a pagar es 15$")