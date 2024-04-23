#operadores in e not in
#strings são iteraveis
# 0 1 2 3 4 5
# f e l i p e
# 6 5 4 3 2 1

nome = 'Felipe'

print(nome[2])#retorna o valor do indice, letra L
print('i' in nome)#checa se é verdade
print('a' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite oque deseja encontrar: ')

if encontrar in nome:
    print('existe')
else:
    print('não existe')