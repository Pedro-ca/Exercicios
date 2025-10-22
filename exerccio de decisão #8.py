num_1 = int(input('me dê três produtos '))
num_2 = int(input())
num_3 = int(input())

if num_1 < num_2 < num_3:
    print('você deveria comprar o primeiro produto')

if num_1 > num_2 < num_3:
    print('você deveria comprar o segundo produto')

if num_1 > num_2 > num_3:
    print('você deveria comprar o terceiro produto')
