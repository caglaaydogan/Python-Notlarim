#meyveler adında bir liste oluştur
meyveler=["elma","erik","çilek","muz","üzüm"]

#oluşturduğun listedeki elemanları for döngüsü ile ekrana bastır
for i in meyveler:
    print(i)

print("2.eleman:",meyveler[1])

meyveler[3] = "karpuz"
print(meyveler)

meyveler.append("kiraz")
print(meyveler)

for i in meyveler:
    if type(i) == str:
        print("Eleman tipi: string")

#meyveler listesinin uzunluğunu ekrana bastıran bir fonksiyon yaz
def uzunluk(liste):
    print("Listenin uzunluğu:", len(liste))

uzunluk(meyveler)

#range() fonksiyonunu kullanarak iç içe iki adet for döngüsü oluştur, ilk for döngüsü 20 ye kadar saysın, ikinci for döngüsünün değeri ilk for döngüsünde bulunan i değeri olsun, eğer ikinci for döngüsünün j değeri çift ise ekrana "sayı çifttir yazdırsın"
for i in range(20):
    for j in range(i):
        if j % 2 == 0:
            print("Sayı çifttir")
