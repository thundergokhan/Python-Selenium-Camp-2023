# Liste ve Döngüler

# Listenin tanımlanması
krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan alanlara özel", "Mutlu emekli ihtiyaç kredisi"]

# Listenin yazdırılması ve elemanlara erişim
print(krediler)
print(krediler[0])
print(krediler[1])
print(krediler[2])

# Listenin uzunluğunun yazdırılması
print(len(krediler))

# Listenin bir elemanının değiştirilmesi ve tekrar yazdırılması
krediler[0] = "Çabuk Kredi"
print(krediler)

# Belirli bir elemana erişim ve yazdırılması
print(krediler[2])

# Döngü kullanımı - örnek 1
for kredi in krediler:
    print("<option>" + kredi + "</option>")

# Döngü kullanımı - örnek 2
for i in range(len(krediler)):
    print(krediler[i])

# Döngü kullanımı - örnek 3
for i in range(3, 10): # 3'ten başla, 10'a kadar (10 dahil değil)
    print(i)

# Döngü kullanımı - örnek 4
for i in range(0, 11, 2): # 0'dan başla, 11'e kadar (11 dahil değil), 2'şer artır
    print(i)