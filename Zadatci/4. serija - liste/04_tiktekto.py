status = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
player = ['X','O']
nastavi = 1



def check(x,y):
    if x[0][0]==y and x[0][1]==y and x[0][2]==y:
        return(1)
    elif x[1][0]==y and x[1][1]==y and x[1][2]==y:
        return(1)
    elif x[2][0]==y and x[2][1]==y and x[2][2]==y:
        return(1)
    elif x[0][0]==y and x[1][0]==y and x[2][0]==y:
        return(1)
    elif x[0][1]==y and x[1][1]==y and x[2][1]==y:
        return(1)
    elif x[0][2]==y and x[1][2]==y and x[2][2]==y:
        return(1)
    elif x[0][0]==y and x[1][1]==y and x[2][2]==y:
        return(1)
    elif x[2][0]==y and x[1][1]==y and x[0][2]==y:
        return(1)
    else:
        return(0)

while nastavi == 1:
    for i in range(2):
        while True:
            print('Na redu je igrač {}.'.format(player[i]))
            try:
                pomakx = int(input('Unesite redak:'))
                pomaky = int(input('Unesite stupac:'))
            except ValueError:
                print("Ono što ste unijeli nije broj!")
            if pomakx > 0 and pomakx < 4 and pomaky > 0 and pomaky < 4 and status[pomakx - 1][pomaky - 1] == '-':
                status[pomakx - 1][pomaky - 1] = player[i]
                break
            else:
                print('Igrač je napravio ilegalan pokret, pokušaj ponovno!')
        if check(status, player[i]):
            print('Pobijedio je igrač {}.'.format(player[i]))
            nastavi = 0
            break
        print(*status, sep = '\n')