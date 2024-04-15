#Operadores lógicos
#and (e) or (ou) not (não)
#and - Todas as condições precisam ser verdadeiras
#são considerados falso
#0 0.0 '' False
#tambem existe o none que é usado para representar um não valor


entrada = input('Entrar ou sair? ')
senha = input('senha: ')
senha_permitida = '1234'

if (entrada == 'e' or entrada == 'E') and senha == senha_permitida:
    print('entrou')
else:
    print('saiu')

print(True and False and True)
print()
