# Python'da Veri Tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklamalar yazınız.

int (integer): Tam sayıları ifade etmek için kullanılan veri tipidir. Örneğin, 5, -3, 0 gibi tam sayılar int veri tipine örnektir.

float: Ondalıklı sayıları ifade etmek için kullanılan veri tipidir. Örneğin, 3.14, -0.5 gibi ondalıklı sayılar float veri tipine örnektir.

str (string): Metinleri ifade etmek için kullanılan veri tipidir. Örneğin, <code>Hello, World!</code>, "Python programlama dili" gibi metinler str veri tipine örnektir.

bool (boolean): Sadece iki değer alabilen bir veri tipidir: True (doğru) ve False (yanlış). Koşul ifadeleri ve karar yapıları gibi yerlerde kullanılır.

list: Birden fazla değeri aynı anda tutmak için kullanılan veri tipidir. Değerler virgülle ayrılarak köşeli parantez içinde gösterilir. Örneğin, [1, 2, 3], ["elma", "armut", "portakal"] gibi.

tuple: Listelerle benzer bir yapıda olup, ancak değiştirilemez (immutable) bir veri tipidir. Parantez içinde gösterilir. Örneğin, (1, 2, 3), ("elma", "armut", "portakal") gibi.

set: Birçok benzersiz (unique) elemanın aynı anda saklanmasını sağlayan bir veri tipidir. Elemanlar süslü parantez içinde gösterilir. Örneğin, {1, 2, 3}, {"elma", "armut", "portakal"} gibi.

dict (dictionary): Anahtar-değer (key-value) çiftlerinin saklanmasını sağlayan bir veri tipidir. Anahtarlar ve değerler iki nokta üst üste işaretiyle ayrılır ve çift tırnak içinde gösterilir. Örneğin, {"isim": "Ahmet", "yaş": 25} gibi.

# Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.

Kullanıcı adı (str):
<code> username = "kodlama_io" </code>

Şifre (str):
<code>password = "sifrem123"</code>

Doğum tarihi (str):
<code>birthdate = "23/04/1990"</code>

Yaş (int):
<code>age = 32</code>

Puan (float):
<code>score = 8.5</code>

Ders notları (list):
<code>grades = [75, 85, 90, 95]</code>

Öğrenci bilgileri (dictionary):
<code>student = {"ad": "Gökhan", "soyad": "Yıldırım", "yaş": 23, "bölüm": "Yönetim Bilişim Sistemleri"}</code>

Kurs listesi (set):
<code>courses = {"Python Programlama", "Web Geliştirme", "Veritabanı Yönetimi"}</code>

# Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.

Kodlama.io sitesinde şart blokları, genellikle kullanıcı girişlerinin doğruluğunu kontrol etmek, hata mesajları vermek veya bazı işlemleri belirli koşullara bağlamak için kullanılmaktadır. Örnekler şu şekildedir:

Kullanıcının girdiği şifre doğru mu kontrolü:

<code>
password = "1234"

if password == "1234":
print("Şifre doğru.")
else:
print("Şifre yanlış.")
</code>

Kullanıcının girdiği sayının pozitif, negatif ya da sıfır olduğunu belirleme:

<code>
number = int(input("Bir sayı giriniz: "))

if number > 0:
print("Girdiğiniz sayı pozitif.")
elif number < 0:
print("Girdiğiniz sayı negatif.")
else:
print("Girdiğiniz sayı sıfır.")
</code>
