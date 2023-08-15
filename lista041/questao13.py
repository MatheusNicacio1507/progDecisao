'''

'''

a = int(input("Informe um valor para a: "))
b = int(input("Informe um valor para b: "))
c = int(input("Informe um valor para c: "))

# 1- a tem que ser menor que b

if(a > b):
    aux = a
    a = b
    b = aux

#garantido até aqui, que entre a e b, o menor está em a

# 2- a tem que ser menor que c

if(a > c):
    aux = a
    a = c
    c = aux

# garantido até aqui, que a é o menor dos três

# necessário garantir que b seja menor que c

# agora é preciso garantir que b seja menor que c
if(b > c):
    aux = b
    b = c
    c = aux

# garantido que entre b e c, o b é menor, ou seja, o cé o maior de todos

print(f"Ordem crescente: {a},{b} e {c}")