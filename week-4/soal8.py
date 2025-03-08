class Pengajar:
    def __init__(self):
        self.matkul_diajar = []

    def mengajar (self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)

    def __str__(self):
        return f"Mata Kuliah yang diajar: {', '.join(self.matkul_diajar) if self.matkul_diajar else 'Tidak ada mata kuliah yang diajar'}"
    
pengajar1 = Pengajar()
pengajar1.mengajar ("Statistik")
pengajar1.mengajar ("Pemrograman")
print(pengajar1)