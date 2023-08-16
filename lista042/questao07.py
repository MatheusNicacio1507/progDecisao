'''
Fazer um algoritmo que pergunte 2 números, e ao final, exiba como resposta na tela qual é o maior e qual é
o menor, ou ainda, se ambos são iguais.
'''

num1 = int(input("Insira um número: "))
num2 = int(input("Insira outro número: "))

if(num1 > num2):
    print(f"O número {num1} é o maior e o número {num2} o menor")

elif(num2 > num1):
    print(f"O número {num2} é maior e o número {num1} o menor")

else:
    print("Os números são iguais")