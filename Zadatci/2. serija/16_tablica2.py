x=int(input('Unesite broj:'))
for i in range(1,x):
    for j in range(1,x):
        print('|{:^10}'.format(j*i),end='')
    print('|')