for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                if d*1000+c*100+b*10+a==4*(a*1000+b*100+c*10+d):
                    print('To su brojevi {}{}{}{} i {}{}{}{}.'.format(a,b,c,d,d,c,b,a))