#Peça ao usuário para inserir um número.
#Continue perguntando até que ele insira CINCO números,
#em seguida, exibam a mensagem “ O último número que você digitou foi um [número] " e pare o programa.
print("Isabella Carolina de Souza")
total = 0
while total < 5:
    numero = int (input("Digite um numero: "))
    total +=1
    ultimo_numero=numero
print("o ultimo numero digitado foi {}".format(ultimo_numero))
