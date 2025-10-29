print ("program mengurutkan data dari yang terkecil \nDengan 3 variabel")
a = int(input("masukkan bilangan pertama :"))
b = int(input("masukkan bilangan kedua :"))
c = int(input("masukkan bilangan ketiga :"))

if a<=b and a<=c:
    if b<=c:
        u=a,b,c
    else:
        u=a,c,b
elif b<=a and b<=c:
    if a<=c:
        u=b,a,c
    else:
        u=b,c,a
else:
    if a<=b:
        u=c,a,b
    else:
        u=c,b,a

print("urutan bilangan:",end=' ')
for i in u :
    print(i,end=' ')
