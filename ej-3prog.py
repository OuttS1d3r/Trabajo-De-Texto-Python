#3)Escribir un algoritmo que solicite al usuario ingresar numeros enteros, 
#hasta que el usuario ingrese un cero. Guardar los numeros 
#ingresados en una lista y calcular la sumatoria y el promedio de los valores que contiene dicha lista
lista=[]
a=None
while a!=0:
    a=int(input("Ingrese un valor entero(0 para salir):"))
    if a!=0:
        lista.append(a)
suma=0
for num in lista:
    suma+=num
print(f"Sumatoria:{suma}\nPromedio: {suma/len(lista)}")
