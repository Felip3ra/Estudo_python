primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if float(primeiro_valor) > float(segundo_valor):
    print('primeiro_valor={} é maior do que o segundo_valor={}'.format(primeiro_valor,segundo_valor))
elif float(primeiro_valor) < float(segundo_valor):
    print('segundo_valor={} é maior do que o primeiro_valor={}'.format(segundo_valor,primeiro_valor))
else:
    print('ambos iguais')
