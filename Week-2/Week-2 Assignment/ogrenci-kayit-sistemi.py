ogrenciler = []

def ogrenci_ekle():
    ad = input("Öğrenci adını girin: ")
    soyad = input("Öğrenci soyadını girin: ")
    ogrenciler.append(ad + " " + soyad)

def ogrenci_sil():
    ad = input("Silmek istediğiniz öğrencinin adını girin: ")
    soyad = input("Silmek istediğiniz öğrencinin soyadını girin: ")
    ogrenci = ad + " " + soyad
    if ogrenci in ogrenciler:
        ogrenciler.remove(ogrenci)
    else:
        print("Öğrenci listede yok.")

def coklu_ogrenci_ekle():
    n = int(input("Kaç öğrenci eklemek istiyorsunuz? "))
    for i in range(n):
        ogrenci_ekle()

def ogrencileri_goster():
    for ogrenci in ogrenciler:
        print(ogrenci)

def ogrenci_numarasi_bul():
    ogrenci = input("Öğrenci adını ve soyadını girin: ")
    if ogrenci in ogrenciler:
        numara = ogrenciler.index(ogrenci) + 1
        print("Öğrenci numarası:", numara)
    else:
        print("Öğrenci listede yok.")

def coklu_ogrenci_sil():
    n = int(input("Kaç öğrenci silmek istiyorsunuz? "))
    for i in range(n):
        ogrenci_sil()

while True:
    print("""
    Öğrenci Kayıt Sistemi
    1- Öğrenci Ekle
    2- Öğrenci Sil
    3- Çoklu Öğrenci Ekle1
    4- Öğrencileri Göster
    5- Öğrenci Numarası Bul
    6- Çoklu Öğrenci Sil
    0- Çıkış
    """)

    secim = input("Seçiminiz: ")

    if secim == "1":
        ogrenci_ekle()
    elif secim == "2":
        ogrenci_sil()
    elif secim == "3":
        coklu_ogrenci_ekle()
    elif secim == "4":
        ogrencileri_goster()
    elif secim == "5":
        ogrenci_numarasi_bul()
    elif secim == "6":
        coklu_ogrenci_sil()
    elif secim == "0":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim!")
