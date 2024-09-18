while True:
    print("------MENU------\n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n5.Salir")
    opcion = int(input("Que operacion quieres realizar: "))

    if opcion == 1:
        num1 = input("ingresa un numero: ")
        num1 = float(num1)
        num2 = input("ingresa otro numero: ")
        num2 = float(num2)
        suma = num1 + num2
        print(f"la suma es {suma}")
    elif opcion == 2:
        num1 = input("ingresa un numero: ")
        num1 = float(num1)
        num2 = input("ingresa otro numero: ")
        num2 = float(num2)
        resta = num1 - num2
        print(f"la resta es {resta}")     
    elif opcion == 3:
        num1 = input("ingresa un numero: ")
        num1 = float(num1)
        num2 = input("ingresa otro numero: ")
        num2 = float(num2)
        multiplicacion = num1 * num2
        print(f"la multiplicacion es {multiplicacion}")
    elif opcion == 4:
        num1 = input("ingresa un numero: ")
        num1 = float(num1)
        num2 = input("ingresa otro numero: ")
        num2 = float(num2)
        division = num1 / num2
        print(f"la division es {division}")
    elif opcion == 5:
        print(f"hasta luego")
        break
    else:
        print("el numero ingresado no pertenece al menu")
          



