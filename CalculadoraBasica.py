print("Calculadora Básica")
print("Menú de Operaciones")
print("1 = Suma")
print("2 = Resta")
print("3 = Multiplicación")
print("4 = División")
print()

a = float(input("Ingrese primer número: "))
b = float(input("Ingrese segundo número: "))
opc = int(input("Ingrese su opción: "))

if opc == 1:
    resultado = a + b
    print("Resultado de la suma:", resultado)
elif opc == 2:
    resultado = a - b
    print("Resultado de la resta:", resultado)
elif opc == 3:
    resultado = a * b
    print("Resultado de la multiplicación:", resultado)
elif opc == 4:
    if b != 0:
        resultado = a / b
        print("Resultado de la división:", resultado)
    else:
        print("Error: La división entre 0 es indefinida.")
else:
    print("Opción inválida. Debe elegir entre 1 y 4.")
