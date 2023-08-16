'''
Fazer um algoritmo que pergunte o nome do aluno, e as notas das provas 1 e 2. Deverá ser exibida na tela
como resposta a média do aluno, e se ele está aprovado, reprovado ou em prova final. Estas condições
devem seguir as regras da tabela abaixo:

    Média           Situação

Abaixo de 3,0     Reprovado
Entre 3,0 e 6,9   Prova Final
A partir de 7,0   Aprovado
'''

aluno = input("Qual o seu nome? ")

nota1 = float(input("Qual a sua nota da prova 1? "))
nota2 = float(input("Qual a sua nota da prova 2? "))

media = (nota1 + nota2) / 2

if(media < 3.0):
    print(f"Olá, {aluno}!")
    print(f"Sua média é {media}")
    print(f"Você está REPROVADO!")

elif(media >= 3.0 and media <= 6.9):
    print(f"Olá, {aluno}!")
    print(f"Sua média é {media}")
    print("Você está de PROVA FINAL!")

else:
    print(f"Olá, {aluno}!")
    print(f"Sua média é {media}")
    print("Você está APROVADO!")