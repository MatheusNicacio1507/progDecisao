'''
Desenvolver um programa que pergunte um número inteiro qualquer e verifique se ele está na faixa de 1 a 10.
'''

num = int(input("Insira um número inteiro: "))

if(num >= 1 and num <= 10):
    print("O número está na faixa de 1 a 10")
else:
    print("O número não está na faixa de 1 a 10")
