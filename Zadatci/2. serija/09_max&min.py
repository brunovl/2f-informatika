tri=0
x=float(input('Unesite broj:'))
max=x
min=x
if x%3==0:
    tri+=1
for i in range(9):
    x = float(input('Unesite broj:'))
    if x > max:
        max=x
    elif x < min:
        min=x
    if x % 3 == 0:
        tri += 1
print('Najveći broj je {}, najmanji {}, a {} je brojeva djeljivo s 3.'.format(max,min,tri))