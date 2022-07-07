n1 = int(input("Que ano você nasceu: "))
ida = int(2022 - n1)

print(f"Estamos em 2022, então você tem {ida} anos!\n")

if ida < 18:
    fal = 18 - ida
    print(f"Ainda falta {fal} para você servir!")
elif ida == 18:
    print(f"{ida} anos! Você já pode servir!")
elif ida > 18:
    pas = ida - 18
    print(f"Já passou {pas} anos da hora de você servir, passou do prazo! ")

#leia o ano de nascimento | fale a idade de acordo com 2022 | quanto tempo falta para o alistamento (18 anos)
#fale o ano que será o alistamento da pessoa
