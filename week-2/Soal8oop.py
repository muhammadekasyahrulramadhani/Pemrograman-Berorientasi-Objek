class hewan:
    def __init__(self, nama, jenis): 
        self.nama = nama
        self.jenis = jenis
        
    def tampilkan_data(self):
        print(f"Nama :  {self.nama}") 
        print(f"Jenis :  {self.jenis}")

nama = input("Masukkan nama Hewan : ")
jenis = input("Masukkan jenis hewan : ")

Hewan = hewan(nama, jenis)
Hewan.tampilkan_data()
    
