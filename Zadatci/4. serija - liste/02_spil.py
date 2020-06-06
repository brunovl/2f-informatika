spil = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'dečko', 'dama', 'kralj', 'as']
tipovi = ['srce', 'karo', 'tref', 'pik']
def miks(karte, tipovi):
    from random import randint
    miks = []
    while len(miks)<52:
        x = randint(0,3)
        y = randint(0,12)
        if x == 1:
            ap = karte[y] + ' - ' + tipovi[x]
        elif x == 2:
            ap = karte[y] + ' - ' + tipovi[x]
        elif x == 3:
            ap = karte[y] + ' - ' + tipovi[x]
        else:
            ap = karte[y] + ' - ' + tipovi[x]
        if karte[y] != '' and ap not in miks:
            miks.append(ap)
    print(miks)
miks(spil, tipovi)