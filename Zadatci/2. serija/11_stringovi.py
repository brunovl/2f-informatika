a=input('Unesite prvu riječ:')
b=input('Unesite drugu riječ:')
slova = ''
for x in a:
    if x in b and not (x in slova):
        slova += x
        print(x)
