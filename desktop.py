import os
from functools import wraps

# Dekorasyon deseni (Decoration Pattern)
def log_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} fonksiyonu calistiriliyor...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} fonksiyonu tamamlandi.")
        return result
    return wrapper

@log_time
def bilgisayardaki_uygulamalari_bul():
    uygulama_listesi = []
    toplam_boyut = 0

    for root, dirs, files in os.walk("C:\\Program Files"):
        for file in files:
            uygulama_yolu = os.path.join(root, file)
            boyut = os.path.getsize(uygulama_yolu)
            toplam_boyut += boyut
            uygulama_listesi.append({"uygulama": uygulama_yolu, "boyut": boyut})

    return uygulama_listesi, toplam_boyut

# Ana program
if __name__ == "__main__":
    uygulamalar, toplam_boyut = bilgisayardaki_uygulamalari_bul()

    print("Bilgisayarinizdaki Toplam Uygulama Sayisi:", len(uygulamalar))
    print("Toplam Yer Kaplayan Boyut:", toplam_boyut / (1024 * 1024), "MB")

    for uygulama in uygulamalar[:10]:  # İlk 10 uygulamayı göster
        print(f"Uygulama: {uygulama['uygulama']}, Boyut: {uygulama['boyut'] / (1024 * 1024):.2f} MB")
