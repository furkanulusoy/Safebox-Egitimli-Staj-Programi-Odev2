class Giris:
    def __init__(self):
        self.kullanici_adi = input("Kullanıcı adınızı girin: ")
        self.sifre = input("Şifrenizi girin: ")

    def kullanici_girisi(self):
        with open("kullanici_bilgileri.txt", "r") as dosya:
            for satir in dosya:
                kullanici, sifre_ = satir.strip().split(",")
                if kullanici == self.kullanici_adi and sifre_ == self.sifre:
                    print("Giriş yapıldı.")
                    return

        print("Kullanıcı adı veya şifre hatalı.")

giris = Giris()
giris.kullanici_girisi()