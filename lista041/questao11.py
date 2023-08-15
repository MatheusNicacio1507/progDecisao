'''
Desenvolver um programa que pergunte um número inteiro de 3 algarismos e apresente como resultado
somente o algarismo das centenas.
'''
num = int(input("Insira um algarismo inteiro de 3 algarismos: "))

if(num > 99 and num <= 999):
    resp = num//100
    print(f"O algarismo das centenas é = {resp}")
else:
    print("O número inserido NÃO possui três algarismos")