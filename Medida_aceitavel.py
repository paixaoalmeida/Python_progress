def numeros():
    lista = []
    numero = int(input("Digite os números: "))
    contador = 0
    soma = 0

    while numero >= 0:
        if numero == 0:
          exit()
        contador = contador + 1                #Contador, a cada numero adiciona na quantidade e soma
        soma = soma + numero
        numero = int(input("Outro número: "))
        lista.append(numero)                    #Adicionando os números inseridos numa lista


    print(f"A quantidade de números digitado foi {contador}")   #quantidade de numeros
    media = soma / contador
    print(f"A média dos números digitados é {media}")  #media
    maior_num = print(f"O maior número digitado foi", max(lista)) #maior numero
    print(f"O menor número digitado foi", min(lista)) #menor número
    print("A média dos números pares é")


numeros()
