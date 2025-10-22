meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
media = 25
temperatura = []

for i in range(12):
    temp = int(input('insira as temperaturas '))
    temperatura.append(temp)

media_anual = sum(temperatura) / 12

print(' resultados')
print(f'Média anual das temperaturas:{media_anual}')

for i in range(12):
    if temperatura[i] > media:
        print(f'{i+1} - {meses[1]}: {temperatura[i]:.2f}')
