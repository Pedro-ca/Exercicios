tamanho = int(input('qual o tamanho a ser pintado em metros quadrados '))

litros_usados = 0.3 * tamanho
latas = 18.0 * litros_usados
preço = float(80.00) / latas
Valor = preço * latas

print(f'{Valor} reais {litros_usados} m²')
