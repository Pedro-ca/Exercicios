from itertools import permutations

def eh_quadrado_magico(numeros):

    a, b, c, d, e, f, g, h, i = numeros

    return (
        (a + b + c == 15) and
        (d + e + f == 15) and
        (g + h + i == 15) and
        (a + d + g == 15) and
        (b + e + h == 15) and
        (c + f + i == 15) and
        (a + e + i == 15) and
        (c + e + g == 15)
    )

def gerar_quadrados_magicos():
    numeros = [1,2,3,4,5,6,7,8,9]
    contador = 0

    for p in permutations(numeros):
        if eh_quadrado_magico(p):
            contador += 1
            print(f"\nQuadrado mágico {contador}:")
            print(f"{p[0]} {p[1]} {p[2]}")
            print(f"{p[3]} {p[4]} {p[5]}")
            print(f"{p[6]} {p[7]} {p[8]}")

    print(f"\nTotal encontrado: {contador}")

gerar_quadrados_magicos()
