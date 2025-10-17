tamanho = int(input('qual o tamanho a ser pintado em metros quadrados '))
compra = input('compra em galões ou latas? ')


litros_usados = 0.16 * tamanho
galão = 3.6
latas = 18.0 / litros_usados
preço_galão = 25.00 / galão
valor_gal = preço_galão * galão
preço = 80.00 / latas
Valor = preço * latas


if compra == 'lata':
    print(f'Valor: {Valor} e {latas} litros usados')


if compra == 'galao':
    print(f'Valor: {valor_gal} e {galão} litros usados')
