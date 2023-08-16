'''
Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final,
informe na tela se o estado inserido está ou não na região Sudeste.
'''

uf = input("Escreva a sigla de algum estado(em maiúsculo): ")

if(uf == "MG" or uf == "RJ" or uf == "SP" or uf == "ES"):
    print("Este estado faz parte da região Sudeste")

else:
    print("Este estado NÃO faz parte da região Sudeste")