#Faça um programa que leia os números digitados pelo usuario,
# a cada número digitado ele deve ser somado ao anterior digitado e a cada soma exibida na tela,
# quando a soma for superior a 50 deve exibir a mensagem “ O total é... [total] ” e parar o programa.
print("Isabella Carolina de Souza")
total = 0
while total <=50:
    numero = int (input("Digite um numero: "))
    total +=numero
    if total > 50:
        print("o total e {}".format(total))
        break