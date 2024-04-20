isim="Cagla"
soyisim=input("Soyadınızı Giriniz: ")
yas=26

print("İsim:", isim)
print("Soyisim:", soyisim)
print("Yaş:", yas)

print("İsim:", isim, "Soyisim:", soyisim, "Yaş:", yas)

print("İsim:", isim, "\nSoyisim:", soyisim, "\nYaş:", yas)

def isim_harfler():
    print("ismin bas harfi:",isim[0])
    print("ismin son harfi:",isim[-1])

def soyisim_harfler():
    print("soyismin bas harfi:",soyisim[0])
    print("soyismin son harfi:",soyisim[-1])

isim_harfler()
soyisim_harfler()
