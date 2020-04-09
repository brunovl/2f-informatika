from random import random
from math import sqrt
numstrel=int(input('Unesite broj pokušaja:'))
count=0
for i in range(numstrel):
    x=random()
    y=random()
    dist=sqrt(x**2+y**2)
    if dist<1:
        count+=1
pi=(4*count)/numstrel
print(pi)