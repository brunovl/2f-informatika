i = 0
brojevi = []
while True:
    x = input('Unesite neki broj:')
    if x == '':
        break
    elif x == '?':
        if len(brojevi) == 0:
            print('Lista je prazna!')
        else:
            print(brojevi.pop(0))
    else:
        try:
            y = float(x)
            brojevi.append(y)
        except ValueError:
            print("Ono što ste unijeli nije broj!")
    i += 1