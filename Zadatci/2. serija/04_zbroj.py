sum=0
com=1
for i in range(10):
    x=float(input('Unesite broj:'))
    if x<0:
        continue
    elif x==0:
        print('Game Over')
        break
    else:
        sum+=x
else:
    print('Zbroj brojeva je {}.'.format(sum))
print('Kraj!')