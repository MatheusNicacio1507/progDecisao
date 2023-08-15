'''
Desenvolver um programa que pergunte dois números inteiros, e apresente como resultado se o segundo
número informado é ou não um divisor do primeiro número informado.
'''

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

div = num1 % num2

if(div == 0):
    print("O segundo número é divisor do primeiro número")
else:
    print("O segundo número não é divisor do primeiro número")
