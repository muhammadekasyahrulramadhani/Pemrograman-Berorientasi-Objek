class MataKuliah:
    jam_per_sks = 2

    def __init__(self, nama, sks):
        self.nama = nama
        self.sks = sks

    @classmethod
    def hitung_total_jam_belajar(cls, sks):
        return sks * cls.jam_per_sks

# Contoh penggunaan
matkul = MataKuliah("Pemrograman Python", 2)
total_jam = MataKuliah.hitung_total_jam_belajar(matkul.sks)
print(f"Mata Kuliah     : {matkul.nama}")
print(f"Jumlah SKS      : {matkul.sks}")
print(f"Total Jam SKS   : {total_jam}")