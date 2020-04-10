x=int(input('Unesite broj za koji želite znati je li prosti ili ne: '))
for i in range(2,x):
    if x%i==0:
        print('Broj nije prost!')
        break
else:
    print('Broj je prost!')