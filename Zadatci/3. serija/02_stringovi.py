def slova(a,b):
    slova=''
    for x in a:
        if x in b and not(x in slova):
            slova+=x
            print(x)