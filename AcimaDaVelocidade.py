#leia velocidade de um carro, se ultrapassar 80km, ele será multado, a multa custa R$ 7.00 por cada km acima do limite

vel = int(input("Qual a velocidade do seu carro? "))

if vel < 80:
    print("Você está na velocidade permitida!")

cont = 80   #contador a partir do 80
mul = 0     #multa a partir de 0

while vel > 80:           #quando estiver acima da velocidade, adicione + 1 ao contador de vel. e mais 7 ao contador de mul.
    cont = cont + 1       #quando o contador de vel for igual ao dado pelo usuário, break no loop e mostre o resultado final
    mul = float(mul + 7)
    if cont == vel:
        print(f"Acima da velocidade! Sua multa é de R${mul:.2f}")
        break






