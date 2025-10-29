#Buat program sederhada dengan input 4 buah bilangan, kemudian tentukan bilangan terbesar dari kedua bilangan tersebut menggunakan statement if.

a = int(input("masukkan bilangan pertama :"))
b = int(input("masukkan bilangan kedua :"))
c = int(input("masukkan bilangan ketiga :"))
d = int(input("masukkan bilangan keempat :"))

print("=================")

if a>b and a>c and a>d:
    print("Bilangan pertama adalah yang terbesar \nNilai nya yaitu: ",a)
elif b>a and b>c and b>d:
    print("Bilangan kedua adalah yang terbesar \nNilai nya yaitu: ",b)
elif c>a and c>b and c>d:
    print("Bilangan ketiga adalah yang terbesar \nNilai nya yaitu: ",c)
elif d>a and d>b and d>c:
    print("Bilangan keempat adalah yang terbesar \nNilai nya yaitu: ",d)
else:
    print("Semua bilangan bernilai sama")
