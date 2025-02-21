#Peça ao usuário para inserir um número e, em seguida, insira outro número.
#Some esses dois números e pergunte se ele quer adicionar outro número.
#Se ele digitar “ s ", diga para inserir outro número e continuar adicionando números e somando até que ele não respondam “ s ".
#Depois que o loop for interrompido, exiba o total.
print("Isabella Carolina de Souza")
numero1= float(input("Digite um numero: "))
numero2= float(input("Digite outro numero: "))
soma = numero1 + numero2
print("A soma dessses numeros é de ",soma)
resposta = print("Você deseja adicionar outro numero: ")
while resposta == "s":
    numero= float(input("Digite outro numero: "))
    soma += numero
    resposta= input("você que adicionar mais um numero? ")
print("A soma destes numeros e de ", soma)
    