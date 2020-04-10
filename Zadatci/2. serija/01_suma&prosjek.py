x = float(input('Unesite broj (broj nula prekida unos):'))
sum=0
count=0
while x!=0:
    count+=1
    sum+=x
    x=float(input('Unesite broj (broj nula prekida unos):'))
print('Zbroj brojeva je {}, a prosjek {}.'.format(sum,sum/count))