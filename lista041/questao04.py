'''
Desenvolver um programa que pergunte um valor numérico inteiro e faça a exibição desse valor caso seja
divisível por 4 e 5. Não sendo divisível por 4 e 5, o programa deverá exibir a mensagem “Valor não é divisível por
4 e 5”.
'''

num = int(input("Informe um valor numérico: "))

resto5 = num % 5
resto4 = num % 4

if(resto5 == 0 and resto4 == 0):
    print(f"O número inserido foi {num}")
else:
    print("Valor não é divisível por 4 e 5")