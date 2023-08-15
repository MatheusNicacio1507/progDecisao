'''
Desenvolver um programa que pergunte um número, e apresente como resposta se o referido número é par ou
é ímpar.
'''

num = int(input("Insira um número: "))

resto = num % 2

if(resto == 0):
    print(f"O número {num} é PAR!")
else:
    print(f"O número {num} é ÍMPAR!")