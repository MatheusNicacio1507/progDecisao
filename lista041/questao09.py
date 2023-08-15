'''
Desenvolver um programa que pergunte um número e exiba a informação de que ele é positivo, negativo ou
nulo.
'''

num = int(input("Informe um número: "))

if(num > 0):
    print("O número é positivo")

elif(num < 0):
        print("O número é negativo")

elif(num == 0):
        print("O número é nulo")