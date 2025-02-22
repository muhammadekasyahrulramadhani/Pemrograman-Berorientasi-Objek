class manusia : 
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
        
    def tampilkan_data(self):
        print(f"Nama :  {self.nama}") 
        print(f"Umur :  {self.umur}")

nama = input("Masukkan nama Anda : ")
umur = int(input("Masukkan umur Anda : "))

Manusia = manusia(nama, umur)
Manusia.tampilkan_data()
        