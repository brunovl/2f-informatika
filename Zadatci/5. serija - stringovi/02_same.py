a = input('Unesite prvu rečenicu:')
b = input('Unesite drugu rečenicu:')
for i in range(min(len(a),len(b))):
    if a[i]==b[i]:
        print(a[i])