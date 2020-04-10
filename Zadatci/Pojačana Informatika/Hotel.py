from random import randint
def changeStatus(pop,kat,soba):
        katstat=pop[kat-1]
        katlist=list(katstat)
        katlist[soba-1]='1'
        katappend=''.join(katlist)
        pop[kat-1]=katappend
def findEmpty(pop,numkat):
    find = ['', '']
    for x in range(numkat):
        for y in range(len(pop[x])):
            if pop[x][y] == '0':
                find=['',int(y)+1]
                break
        if find[1]!='':
            find[0]=int(x)+1
            return(find)
            break
pop=[]
app='0'
numkat = int(input('Unesite broj katova: '))
numsob = int((numkat * (numkat + 1)) / 2)
print('Broj soba je {}.'.format(numsob))
for i in range(numkat):
    pop.append(app)
    app+='0'
print('Popunjenost hotela izgleda ovako: \n{}'.format(pop))
numgost = int(input('Unesite broj gostiju: '))
while numgost > 0:
    kat=randint(1,numkat)
    soba=randint(1,kat)
    #print('Probavam kat {} i sobu {} čiji je status {}.'.format(kat, soba, pop[kat-1][soba-1]))
    if pop[kat-1][soba-1]=='0':
        changeStatus(pop, kat, soba)
        numgost-=1
        numsob-=1
print('Broj preostalih soba je {}.'.format(numsob))
print('Sobe su popunjene na sljedeći način: \n{}'.format(pop))
while numsob>0:
    ask = int(input('Želite li dodati još jednog gosta? Ako da upišite broj 1, ako ne upišite broj 0.'))
    if ask==1:
        find=findEmpty(pop,numkat)
        changeStatus(pop, find[0], find[1])
        print('Novi gost smješten je u sobu {} na katu {}.'.format(find[1],find[0]))
        numsob-=1
    elif ask==0:
        break
else:
    print('Ponestalo je soba.')
print('Na kraju raspored popunjenosti je: \n{}'.format(pop))
print('Doviđenja!')