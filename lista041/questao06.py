'''
Desenvolver um programa que pergunte dois valores numéricos inteiros e apresente o valor da diferença entre o
maior valor e o menor valor lido.
'''

num1 = int(input("Informe um valor numérico: "))
num2 = int(input("Informe um valor numérico: "))

if(num1 > num2):
    print(f"O valor da diferença entre {num1} e {num2} é = {num1-num2}")
else:
    print(f"O valor da diferença entre {num2} e {num1} é = {num2 - num1}")