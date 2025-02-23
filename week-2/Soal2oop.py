class pasien:
    def __init__ (self, Nama, Id,):
        self.Nama = Nama 
        self.Id = Id
        
    def tampilkan_data(self):
        print("Nama : " + self.Nama) 
        print("ID  : " + str(self.Id))
        
pasien1 = pasien("Syahrul", 2025001)

pasien1.tampilkan_data()