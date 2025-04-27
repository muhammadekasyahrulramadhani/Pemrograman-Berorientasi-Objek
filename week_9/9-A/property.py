class MataKuliah:
    def __init__(self, nama, sks):
        self.nama = nama
        self.sks = sks

    @property
    def total_jam(self):
        return self.sks * 2

matkul = MataKuliah("Pemrograman Python Berorientasi Objek", 2)
print(f"Mata Kuliah     : {matkul.nama}")
print(f"Jumlah SKS      : {matkul.sks}")
print(f"Total Jam SKS   : {matkul.total_jam} jam")