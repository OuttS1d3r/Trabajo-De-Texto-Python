#2)Escribir un algoritmo que solicite ingresar un numero entero. De
#acuerdo al numero ingresado, imprime si es negativo, positivo o igual a cero
#el algoritmo continua solicitando numeros hasta que el usuario
#Ingrese (*) a=int(input("Ingrese un valor entero: "))
salir="*"
a=None

while a!=salir:
    a=input("Ingrese un valor entero: ")
    print("(para salir ingrese '*')")
    if a==salir:
        print("Has salido del programa.")
        break
    try:
        a=int(a)
        if a<0:
            print("Es negativo")
        elif a>0:
            print("Es positivo")
        else:
            print("El número es igual a cero")
    except ValueError:
        print("Entrada inválida. Debes ingresar un número entero.")
    