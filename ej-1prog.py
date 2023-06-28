#1) contar el numero de ocurrencias de cada una de las letras del afabeto que contiene
#una frase que ingrese el usuario por teclado
alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letra_repetida={}
x=False
while x==False:
    frase_usuario=input("Frase: ")
    for letra in frase_usuario:
        if letra.isalpha():
            if letra in letra_repetida:
               letra_repetida[letra] += 1
            else:
                letra_repetida[letra] = 1
    print(frase_usuario)
    for letra, frecuencia in letra_repetida.items():
        print(f"{letra}:{frecuencia}")
    a=int(input("Desea ingresar otra frase? Si(1),No(0)\n"))
    while a not in [1,0]:
        a=int(input("Valor incorrecto. Ingrese 1 para SI, y 0 para NO\n"))
    if a==0:
        print("Saliendo")
        x=True
    frase_usuario=""
    letra_repetida={}
        



