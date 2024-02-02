import time
import os
import ast


def anamenu():
    print("╔═════════════════════════════╗")
    print("║ MustiZone Rehber Uygulaması ║")
    print("║                             ║")
    print("║ 1- Kişi Ekle                ║")
    print("║ 2- Kişileri Listele         ║")
    print("║ 3- Kişi Ara                 ║")
    print("║ 4- Kişi Sil                 ║")
    print("║ 5- Kişi Kaydını Düzenle     ║")
    print("║ 6- Uygulamadan Çıkış Yap    ║")
    print("║                             ║")
    print("╚═════════════════════════════╝")
    print()
    secim=input("Lütfen seçiminizin başındaki sayıyı giriniz: ")
    if secim=="1":
        kisiekle()
        anamenu()

    elif secim=="2":
        kisilistele()
        anamenu()

    elif secim=="3":
        kisiara()
        anamenu()

    elif secim=="4":
        kisisil()
        anamenu()

    elif secim=="5":
        kisiduzenle()
        anamenu()

    elif secim=="6":
        print("Programdan 3 saniye içerisinde çıkış yapılacaktır.")
        time.sleep(3)
        sys.exit(0)

    else:
        print("Lütfen menüde bulunan geçerli bir sayı giriniz.")
        anamenu()

def kisiekle():
    ad=input("Lütfen Ad-Soyad bilgisiniz giriniz: ")
    numara=input("Lütfen telefon numarasını giriniz: ")
    girdi={"Ad Soyad":ad,"Numara":numara}

    if len(numara)<10:
        print("Eksik numara girdiniz, lütfen tekrar deneyiniz.")
        return kisiekle()
    
    else:
        try:
            with open("telefon_rehberi.txt", "a", encoding="utf-8") as dosya:
                dosya.write(f"{girdi},")
                time.sleep(1)
                print("\nKişi başarıyla eklendi.\n")
                time.sleep(1)
        except:
                print("Dosya hatası")

    secim=input("Başka işlem yapmak ister misiniz? E/H ").lower()

    if secim=="e":
        kisiekle()

    elif secim=="h":
        anamenu()

def kisilistele():
    try:
        with open("telefon_rehberi.txt", "r", encoding="utf-8") as dosya:
            rehber = dosya.read()
            print(f"Kişiler:\n{rehber}")
            
    except FileNotFoundError:
        print("Rehber dosyası bulunamadı.")

def kisiara():
    with open("telefon_rehberi.txt", "r", encoding="utf-8") as dosya:
        okuma_sonucu = dosya.read()

    aranan_isim = input("Lütfen aranacak ismi giriniz: ")

    try:
        cevirilen = ast.literal_eval(okuma_sonucu)
        bulunan = 0
        for a in cevirilen:
            if a["Ad Soyad"] == aranan_isim:
                print(a)
                print(f'Telefon Numarası: {a["Numara"]}')
                bulunan = 1
                break
        if bulunan == 0:
            print(f"\n{aranan_isim} diye bir kayıt bulunamadı")
    except FileNotFoundError:
        print("Dosya bulunamadı.")
    except (SyntaxError, ValueError):
        print("Dosya geçerli bir Python veri yapısı içermiyor.")

        secim=input("Başka işlem yapmak ister misiniz? E/H ").lower()

    if secim=="e":
        kisiara()

    elif secim=="h":
        anamenu()

def kisisil():
    with open("telefon_rehberi.txt", "r", encoding="utf-8") as dosya:
        okuma_sonucu = dosya.read()
    cevirilen = ast.literal_eval(okuma_sonucu)
    aranan_isim = input("Lütfen silinecek ismi giriniz: ")

    with open("telefon_rehberi.txt","w") as dosya:
        for a in cevirilen:
            if a["Ad Soyad"] != aranan_isim:
                dosya.write(f"{str(a)},")

    secim=input("Başka işlem yapmak ister misiniz? E/H ").lower()

    if secim=="e":
        kisisil()

    elif secim=="h":
        anamenu()

def kisiduzenle():
    try:
        with open("telefon_rehberi.txt", "r", encoding="utf-8") as dosya:
            okuma_sonucu = dosya.read()
    except FileNotFoundError:
        print("Dosya bulunamadı.")
        return

    aranan_isim = input("Lütfen numarasını düzenlemek istediğiniz kişinin adını giriniz: ")
    
    try:
        cevirilen = ast.literal_eval(okuma_sonucu)
        bulunan = False
        for kisi in cevirilen:
            if kisi["Ad Soyad"] == aranan_isim:
                yeni_numara = input("Lütfen yeni numarayı giriniz: ")
                kisi["Numara"] = yeni_numara
                bulunan = True
                break
        
        if bulunan:
            with open("telefon_rehberi.txt", "w", encoding="utf-8") as dosya:
                dosya.write(str(cevirilen))
            print("Numara başarıyla güncellendi.")
        else:
            print(f"{aranan_isim} adında bir kişi bulunamadı.")
    
    except (SyntaxError, ValueError):
        print("Dosya geçerli bir Python veri yapısı içermiyor.")

    secim=input("Başka işlem yapmak ister misiniz? E/H ").lower()

    if secim=="e":
        kisiduzenle()

    elif secim=="h":
        anamenu()



anamenu()