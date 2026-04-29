peso = float(input("Ingrese su peso (kg): "))
altura = float(input("Ingrese su altura en m: "))

if 5 <= peso <= 450:
    if 0.6 <= altura <= 2.5:
        imc = peso / (altura ** 2)
        print("Tu IMC es:", imc)

        if imc < 18.5:
            print("Su diagnóstico es Bajo Peso")
        elif 18.5 <= imc <= 24.9:
            print("Su diagnóstico es Peso Normal")
        elif 25 <= imc <= 29.9:
            print("Su diagnóstico es Sobrepeso")
        elif imc >= 30:
            print("Su diagnóstico es Obesidad")
    else:
        print("Altura no válida")
else:
    print("Peso no válido")
