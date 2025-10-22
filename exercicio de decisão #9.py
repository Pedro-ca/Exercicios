num_1 = int(input('me dê três numeros '))
num_2 = int(input('    '))
num_3 = int(input('    '))

ordem1 = [num_1, num_2, num_3]
ordem2 = [num_2, num_1, num_3]
ordem3 = [num_1, num_3, num_2]

if num_1 < num_2 < num_3:
    ordem1.reverse()
    print(ordem1)

if num_3 < num_2 < num_1:
    print(ordem1)

if num_2 < num_3 < num_1:
    print(ordem3)

if num_1 < num_3 < num_2:
    ordem3.reverse()
    print(ordem3)

if num_2 < num_1 < num_3:  
    print(ordem2)

if num_3 < num_1 < num_2:  
    ordem2.reverse()
    print(ordem2)

