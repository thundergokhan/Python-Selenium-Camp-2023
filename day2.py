faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

#bir stringi int olarak dönüştürüyoruz.
print(int(vade) + 12)
#print(int(krediAdi)) => bu hatalıdır çünkü str içerisinde harf temelli olursa dönüşemez.
faiz = str(faiz)
print(type(faiz))

vade = int(input("Lütfen istediğiniz vade sayısını  giriniz: "))
print(type(vade))
vade = vade + 12

# string interpolation
#Sçtiğiniz vade sonucu ortaya çıkan vade:
print("Seçtiğiniz vade sonucu ortaya çıkan vade: " + str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi = vade))
print(f"Seçtiğiniz vade sonucu ortaya çıkan vade: {vade}")

isim = "Halit"
metin = "Merhaba {name}".format(name = "Samet")
print(metin)


# f-string
metin = f"Hoşgeldiniz {1 + 1}"
print(metin)


# listeler
# döngüler
# fonksiyonlar 