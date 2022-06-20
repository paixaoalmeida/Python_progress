import random

NUM = [0, 1, 2, 3, 4, 5]                #array com números de 0 a 5

sele = str(random.choice(NUM))          #converti a array para string

perg = str(input("Qual número o computador pensou? "))      #numero que o usuário tentou

if sele[0] == perg:                    #index 0 (o número)
    print("Acertou!")
else:
    print("Não acertou!")

print(f"O número que o computador pensou foi {sele} ")
#Faça o computador pensar num número (0-5), tente adivinhar, se acertar printe "ganhou" e se perder print "perdeu"
