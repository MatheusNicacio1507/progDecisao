'''
Fazer um algoritmo que peça um número, e ao final, informe se o número digitado está acima de 1000 ou
abaixo de 1000.
'''

num = int(input("Insira um número: "))

if(num > 1000):
    print("O número está acima de 1000")

else:
    if (num < 1000):
        print("O número está abaixo de 1000")
    else:
         print("O número é 1000")