import random

def embaralhar(texto):
    texto = input('ensira uma palavra ')
    lista = list(texto)
    random.shuffle(lista)
    return ''.join(lista)

palavra = "Python"
resultado = embaralhar(palavra)

print(resultado)
