'''
Desenvolver um programa que pergunte um número. Se este número for maior que 20, então ele deverá exibir a
metade deste número, senão, ele deverá exibir o número sem alterações.
'''

num = float(input("Insira um número: "))

if(num > 20):
    div = num/2
    print(f"A metade de {num} é = {div}")
else:
    print(f"O número inserido foi {num}")