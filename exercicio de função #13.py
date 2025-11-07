def desenhar_retangulo(linhas=1, colunas=1):
    if linhas < 1:
        linhas = 1
    elif linhas > 20:
        linhas = 20

    if colunas < 1:
        colunas = 1
    elif colunas > 20:
        colunas = 20

    print('+' + '-' * colunas + '+')

    for _ in range(linhas):
        print('|' + ' ' * colunas + '|')

    print('+' + '-' * colunas + '+')

desenhar_retangulo(3, 5)
