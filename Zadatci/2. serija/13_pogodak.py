from random import randint
x=randint(1,1000)
y=x-1
s=0
while y!=x:
    y=int(input('Pokušajte pogoditi:'))
    if y < x:
        print('Broj je veći!')
    elif y > x:
        print('Broj je manji!')
    s+=1
print('Pogodak! Broj pokušaja je {}.'.format(s))