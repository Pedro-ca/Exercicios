while True:
    nome = input('me dê seu nome ')
    idade = int(input('me dê sua idade '))
    salario = int(input('me dê seu salario '))

# aprovações

    if idade >= 0 and idade <= 150:
        print('idade aceita')
    
    if salario != 0:
        print('salario aceito')

    if len(nome) > 3:
        print('nome valido')


# reprovações
    
    if idade < 0 and idade > 150:
        print('idade invalida')
    
    if salario == 0:
        print('salario invalido')

    if len(nome) <= 3:
        print('nome invalido')


    break
