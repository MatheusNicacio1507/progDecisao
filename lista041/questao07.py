'''
Desenvolver um programa que pergunte um valor inteiro positivo ou negativo, e exiba como resposta o módulo
deste valor, ou seja, o número lido como sendo positivo.
'''

num = int(input("Informe um valor numérico positivo ou negativo: "))

if(num > 0):
    print(f"{num}")
else:
    num2 = num * -1
    print(f"{num2}")