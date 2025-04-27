class MataKuliah:
    sks_per_jam = 2

    def __init__(self, nama, sks):
        self.nama = nama
        self.sks = sks
    
    @staticmethod
    def total_jam_belajar (sks):
        return sks * MataKuliah.sks_per_jam

# Contoh penggunaan
matkul = MataKuliah("Pemrograman Python", 2)
total_jam = MataKuliah.total_jam_belajar(matkul.sks)
print(f"Mata Kuliah     : {matkul.nama}")
print(f"Jumlah SKS      : {matkul.sks}")
print(f"Total Jam SKS   : {total_jam} jam")