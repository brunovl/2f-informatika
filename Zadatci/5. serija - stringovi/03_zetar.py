string = 'Zetar Zetru zlete zetlju'
string2 = string.split()
zet = [string2[0]+' '+string2[1],string2[2]+' '+string2[3]]
zet1 = zet[0].replace('Z','P')
zet2 = zet[1].replace('z','p')
print(zet1+' '+zet2)