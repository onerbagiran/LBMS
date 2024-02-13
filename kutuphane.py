class Library:
    def __init__(self):
        self.file=open("books.txt","a+")
        
    def kitap_listele(self):
        self.file.seek(0)
        books=self.file.read().splitlines()
        if not books:
            print("Henüz girilmiş kitap yok")
        else:
                for book in books:
                    Kitap_adi,Yazar_adi,Tarih,Sayfa_sayisi=book.split(",")
                    print(f"Kitap Adi: {Kitap_adi}, Yazar : {Yazar_adi}, Çıkış Tarihi: {Tarih}, Sayfa Sayısı: {Sayfa_sayisi}")
                    
    def kitap_ekle(self):
        Kitap_adi=input("Kitap adını giriniz:")
        Yazar_adi=input(Kitap_adi+"kitabının yazar adını giriniz:")
        Tarih=input(Kitap_adi+"kitabının çıkış tarihini giriniz:")
        Sayfa_sayisi=input(Kitap_adi + "kitabının sayfa sayisini giriniz:") 
        Kitabin_kunyesi=f"{Kitap_adi},{Yazar_adi},{Tarih},{Sayfa_sayisi}\n"
        self.file.write(Kitabin_kunyesi)
        print("Kitap bilgileri yüklendi")
        
        
                