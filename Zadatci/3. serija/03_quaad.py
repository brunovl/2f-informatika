def kvad(a,b,c):
    from cmath import sqrt
    if a==0 and b==0 and c==0:
        print('Jednadžba ima beskonačno mnogo rješenja.')
    else:
        if a==0:
            rje=(c*(-1))/b
            print('Jednadžba ima jedno rješenje, {}.'.format(rje))
        elif b==0:
            rje=sqrt((c*(-1))/a)
            print('Jednadžba ima jedno rješenje, {}.'.format(rje))
        elif c==0:
            rje=(b*(-1))/a
            print('Jednadžba ima dva rješenja, 0 i {}.'.format(rje))
        elif a==0 and b==0:
            print('Jednadžba nema rješenja.')
        elif a==0 and c==0 or b==0 and c==0:
            print('Jednadžba ima jedno rješenje, 0.')
        else:
            d=b**2-4*a*c
            print('D je',d)
            rjea=(b*(-1)+sqrt(d))/(2*a)
            rjeb=(b*(-1)-sqrt(d))/(2*a)
            if d > 0:
                print('Jednadžba ima dva rješenja, {} i {}.'.format(rjea,rjeb))
            elif d == 0:
                print('Jednadžba ima jedno dvostruko rješenje, {}.'.format(rjea))
            elif d < 0:
                print('Jednadžba ima dva rješenja, {} i {}.'.format(rjea,rjeb))
a=float(input('Unesite a:'))
b=float(input('Unesite b:'))
c=float(input('Unesite c:'))
kvad(a,b,c)