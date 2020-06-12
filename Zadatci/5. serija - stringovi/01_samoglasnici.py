a = input('Unesite riječ:')
i = 1
for x in a:
    if x in 'aeiouAEIOU':
        print('Samoglasnik {} je na poziciji {}.'.format(x, i))
    i += 1
