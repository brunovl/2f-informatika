from random import randint
max=1000
min=1
count=0
while True:
    guess=randint(min,max)
    print('Računalo pogađa: {}.'.format(guess))
    ans=input('Je li pogodak točan?' 
              '(Unesite p ako je točno, v ako je traženi broj veći ili m ako je traženi broj manji.):')
    if ans=='p':
        break
    elif ans=='v':
        min=guess+1
    elif ans=='m':
        max=guess-1
    count += 1
print('Kraj!')