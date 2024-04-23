#operador lógico "not"
#usado para inverter expressões
#not True = False
#not False = True

senha = input('Senha: ')

if senha != '123456':
    print('senha incorreta')
else:
    print('entrou')

if not senha:
    print('nada foi digitado')
else:
    print('entrou')

print(not 0)
print(not 1)
