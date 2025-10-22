lista = 'abcdefghij'
vogais = 'aeiou'
consoantes = "bcdfghjklmnpqrstvwxyz"

l_vogais = [char for char in lista if char in vogais]
l_consoantes = [char for char in lista if char in consoantes]

print(f'vogais: {len(l_vogais)} e consoantes: {len(l_consoantes)}')
