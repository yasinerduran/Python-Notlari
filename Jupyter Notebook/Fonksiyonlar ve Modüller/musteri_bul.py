def kullanici_bul(kullanici_id):
    kullanicilar = {
        "1": {
            "ad-soyad":"Yasin Erduran",
            "eposta":"yasinerduran@uludag.edu.tr"
        },
        "2": {
            "ad-soyad":"Hacer Göçer",
            "eposta":"gocerhacer@art.de"
        },
        "3": {
            "ad-soyad":"Ertuğrul Uzun",
            "eposta":"ertugruluzun@uludag.edu.tr"
        },
        "4": {
            "ad-soyad":"Eda Sönmez",
            "eposta":"edasonmez@uludag.edu.tr"
        },
        "5": {
            "ad-soyad":"Erhan Sonkaya",
            "eposta":"erhanlastrock@rock.do"
        },
        "6": {
            "ad-soyad":"Dilek Uzun",
            "eposta":"uzundilek@gmail.gov"
        },
    }
    if kullanici_id in kullanicilar.keys():
        return kullanicilar[kullanici_id]["ad-soyad"], kullanicilar[kullanici_id]["eposta"]
    else:
        return "Müşteri adı bulunamadı", "Müşteri eposta bulunamadı"
