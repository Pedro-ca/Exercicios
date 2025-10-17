tamanho = int(input('informe o tamanho do arquivo '))
velocidade = int(input('informe a velocidade da conexão em mbps '))

op1 = tamanho / velocidade / 60

print(f'irá demorar {op1} minutos ')
