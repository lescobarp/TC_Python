nota = float(input("Ingrese la nota del estudiante (0-20): "))
if nota < 0 or nota > 20:
    print("Nota inválida. Por favor ingrese una nota entre 0 y 20.")
else:
    if nota == 20:
        print("¡Excelente!")
    elif nota >= 11:
        print("Aprobado")
    else:
        print("Desaprobado")
