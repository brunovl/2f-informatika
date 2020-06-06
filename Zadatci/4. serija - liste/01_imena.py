i = 0
ime = []
while True:
    x = input('Unesite ime prijatelja:')
    if x == '':
        break
    else:
        ime.append(x)
    i += 1
ime.sort()
for x in ime:
    print(x)
