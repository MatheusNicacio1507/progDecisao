'''
Fazer um algoritmo que peça um número de 1 a 7, e ao final, informe o dia da semana (por extenso)
correspondente ao número que foi inserido. Informar também a mensagem “número inválido” quando o
número inserido não corresponder à um dia da semana.
'''

num = int(input("Insira um número de 1 a 7: "))

if(num == 1):
    print("Segunda-feira")

elif(num == 2):
    print("Terça-feira")

elif(num == 3):
    print("Quarta-feira")

elif(num == 4):
    print("Quinta-feira")

elif(num == 5):
    print("Sexta-feira")

elif(num == 6):
    print("Sábado")

elif(num == 7):
    print("Domingo")

else:
    print("Número inválido")
