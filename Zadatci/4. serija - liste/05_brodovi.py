from random import randint
brodovi = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
s = 0
count = 0
orient = randint(1,2)
x = range(1,4)
y = range(1,5)
if orient == 1:
    pozy = randint(0,3)
    brodovi[pozy][0]='X'
    brodovi[pozy][1]='X'
    brodovi[pozy][2]='X'
else:
    pozx = randint(0,2)
    pozy = randint(0,1)
    brodovi[pozy][pozx]='X'
    brodovi[pozy+1][pozx] = 'X'
    brodovi[pozy+2][pozx] = 'X'
#print(*brodovi, sep = '\n')
while s < 3:
    try:
        tryy = int(input('Unesite redak:'))
        tryx = int(input('Unesite stupac:'))
    except ValueError:
        print("Ono što ste unijeli nije broj!")
        continue
    if tryx in x and tryy in y and brodovi[tryy-1][tryx-1] == 'X':
        brodovi[tryy-1][tryx-1] == ' '
        print('Bravo, potopili ste jedan dio broda!')
        s+=1
    elif tryx not in x or tryy not in y:
        print('Ilegalan pokret. Pokušajte ponovno.')
    else:
        print('Niste pogodili brod. Pokušajte opet.')
    count+=1
print('Bravo! Potopili ste cijeli brod u {} pokušaja.'.format(count))