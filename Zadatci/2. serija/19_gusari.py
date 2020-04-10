x=int(input('Unesite broj gusara:'))
kokos=x
for i in range(x):
    kokos+=1
    kokos*=x
print('Najmanji potrebni broj kokosa je {}.'.format(kokos+1))