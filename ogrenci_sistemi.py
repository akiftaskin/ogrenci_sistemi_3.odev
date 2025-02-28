#Öğrenciler listesi oluşturuldu.
ogrenciler = [
    {"numara": 72, "ad": "Akif", "soyad": "Taşkın", "bolum": "Bilgisayar Mühendisliği", "ortalama": 2.70},
    {"numara": 102, "ad": "Emir", "soyad": "Şen", "bolum": "YBS", "ortalama": 2.80}
]

#Öğrenci bilgilerini alıp listeye ekleyen fonksiyon budur.
def ogrenci_ekle():
    numara = int(input("Öğrenci numarası: "))
    ad = input("Adı: ")
    soyad = input("Soyadı: ")
    bolum = input("Bölümü: ")
    ortalama = float(input("Not Ortalaması: "))

    yeni_ogrenci = {"numara": numara, "ad": ad, "soyad": soyad, "bolum": bolum, "ortalama": ortalama}
    ogrenciler.append(yeni_ogrenci)
    print("Öğrenci başarıyla eklendi.\n")

#Listedeki tüm öğrencileri ekrana yazdıran fonksiyon. Eğer öğrenci listede yoksa bunu belirtiyor.
def ogrencileri_listele():
    if not ogrenciler:
        print("Kayıtlı öğrenci bulunmamaktadır.\n")
        return
    
    for ogrenci in ogrenciler:
        print(f"Numara: {ogrenci['numara']}, Ad: {ogrenci['ad']} {ogrenci['soyad']}, Bölüm: {ogrenci['bolum']}, Ortalama: {ogrenci['ortalama']}")
    print()

#Kullanıcıdan öğrenci numarası alıp o öğrencinin bilgilerini ekrana yazdıran fonksiyon.
def ogrenci_goruntule():
    numara = int(input("Görüntülemek istediğiniz öğrencinin numarasını girin: "))
    for ogrenci in ogrenciler:
        if ogrenci["numara"] == numara:
            print(f"Numara: {ogrenci['numara']}, Ad: {ogrenci['ad']} {ogrenci['soyad']}, Bölüm: {ogrenci['bolum']}, Ortalama: {ogrenci['ortalama']}\n")
            return
    print("Öğrenci bulunamadı.\n")

#Öğrenci numarasına göre bilgileri güncelleyebileceğimiz fonksiyon.
def ogrenci_guncelle():
    numara = int(input("Güncellemek istediğiniz öğrencinin numarasını girin: "))
    for ogrenci in ogrenciler:
        if ogrenci["numara"] == numara:
            ogrenci["ad"] = input("Yeni Adı: ")
            ogrenci["soyad"] = input("Yeni Soyadı: ")
            ogrenci["bolum"] = input("Yeni Bölümü: ")
            ogrenci["ortalama"] = float(input("Yeni Not Ortalaması: "))
            print("Öğrenci bilgileri güncellendi.\n")
            return
    print("Öğrenci bulunamadı.\n")

#Öğrenci numarasına göre listeden öğrenciyi kaldıran fonksiyon.
def ogrenci_sil():
    numara = int(input("Silmek istediğiniz öğrencinin numarasını girin: "))
    for ogrenci in ogrenciler:
        if ogrenci["numara"] == numara:
            ogrenciler.remove(ogrenci)
            print("Öğrenci silindi.\n")
            return
    print("Öğrenci bulunamadı.\n")

#Kullanıcının işlemleri seçebileceği bir menü yapısı oluşturuyoruz. Bu şekilde terminal üzerinden tüm işlemleri görüntüleyebiliriz. Daha pratik ve kolay bir kullanım sağlıyor.
def menu():
    while True:
        print("1 - Öğrenci Ekle")
        print("2 - Tüm Öğrencileri Listele")
        print("3 - Öğrenci Bilgilerini Görüntüle")
        print("4 - Öğrenci Güncelle")
        print("5 - Öğrenci Sil")
        print("6 - Çıkış")
        
        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            ogrenci_ekle()
        elif secim == "2":
            ogrencileri_listele()
        elif secim == "3":
            ogrenci_goruntule()
        elif secim == "4":
            ogrenci_guncelle()
        elif secim == "5":
            ogrenci_sil()
        elif secim == "6":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.\n")

menu()


