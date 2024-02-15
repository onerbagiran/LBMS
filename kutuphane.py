# class Library:
#     def __init__(self):
#         self.file=open("books.txt","a+")
        
#     def kitap_listele(self):
#         self.file.seek(0)
#         books=self.file.read().splitlines()
#         if not books:
#             print("Henüz girilmiş kitap yok")
#         else:
#                 for book in books:
#                     Kitap_adi,Yazar_adi,Tarih,Sayfa_sayisi=book.split(",")
#                     print(f"Kitap Adi: {Kitap_adi}, Yazar : {Yazar_adi}, Çıkış Tarihi: {Tarih}, Sayfa Sayısı: {Sayfa_sayisi}")
                    
#     def kitap_ekle(self):
#         Kitap_adi=input("Kitap adını giriniz:")
#         Yazar_adi=input(Kitap_adi+"kitabının yazar adını giriniz:")
#         Tarih=input(Kitap_adi+"kitabının çıkış tarihini giriniz:")
#         Sayfa_sayisi=input(Kitap_adi + "kitabının sayfa sayisini giriniz:") 
#         Kitabin_kunyesi=f"{Kitap_adi},{Yazar_adi},{Tarih},{Sayfa_sayisi}\n"
#         self.file.write(Kitabin_kunyesi)
#         print("Kitap bilgileri yüklendi")


#     def kitap_silme(self):
#         Kitap_adi_remove=input("Silmek istediğiniz kitap adını giriniz:")
        
             
                
class Library:
    def __init__(self):
        self.file=open("books.txt","a+")

        self.kitap_ekle()
        self.kitap_listele()
        self.kitap_silme()
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
        Yazar_adi=input(Kitap_adi+ " kitabının yazar adını giriniz:")
        Tarih=input(Kitap_adi+ " kitabının çıkış tarihini giriniz:")
        Sayfa_sayisi=input(Kitap_adi + " kitabının sayfa sayisini giriniz:") 
        Kitabin_kunyesi=f"{Kitap_adi},{Yazar_adi},{Tarih},{Sayfa_sayisi}\n"
        self.file.write(Kitabin_kunyesi)
        print("Kitap bilgileri yüklendi")
    def kitap_silme(self):
        silinecek_kitap=input("silmek istediğiniz kitap adını giriniz ")
        self.file.seek(0)
        books=self.file.read().splitlines()
        new_books=[]
        silindi=False
        for kitap in books:
            if silinecek_kitap not in kitap:
                new_books.append(kitap)
            else:
                silindi=True
        if silindi:
            self.file.seek(0)  
            self.file.truncate()  
            for kitap in new_books:
                self.file.write(kitap + "\n")
            print(silinecek_kitap+ " başarıyla silindi.")
        else:
            print("Kitap bulunamadı.")        




if __name__ == "__main__":
    Library()
        
