a = input('Unesite neku rečenicu:')
c = [0,0,0,0,0]
for i in a:
    if i in 'aA':
        c[0]+=1
    if i in 'eE':
        c[1]+=1
    if i in 'iI':
        c[2]+=1
    if i in 'oO':
        c[3]+=1
    if i in 'uU':
        c[4]+=1
print('U rečenici ima {} slova a, {} slova e, {} slova i, {} slova o i {} slova u.'.format(c[0],c[1],c[2],c[3],c[4]))