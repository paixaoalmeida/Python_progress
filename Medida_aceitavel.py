aceitavel_peca = 90 #tamanho aceitavel da peça
sair = str("sair")

peca = float(input("Digite a dimensão da peça: "))  #digite a dimensao da peca

if peca > aceitavel_peca:
    print("O tamanho aceitavel é abaixo de ",aceitavel_peca,"!")       #se a dimensão for aceitavel, OK
    dimensao_aceitavel = float(input("Digite uma dimensão aceitavel abaixo de 90: ")) #Se nao for aceitavel, digite outra
    if dimensao_aceitavel <= aceitavel_peca:
        print("Medida válida!")  #Medida válida
        sair_programa = str(input("Digite sair para encerrar o programa! "))  #se digitar sair, sai do programa
        if sair_programa == sair:
            exit()
    else:
        print("Medida inválida! Medidas aceitas apenas abaixo de 90!")

