from collections import namedtuple

# Mendefinisikan namedtuple untuk Buku
Mata_kuliah = namedtuple("Matkul", "nama pengajar sks")

# Membuat beberapa instance Buku
matkul1 = Mata_kuliah("Matematika", "Dr. Ahmad", 3)
matkul2 = Mata_kuliah("Fisika", "Dr. Budi", 4)
matkul3 = Mata_kuliah("Kimia", "Dr. Citra", 3)

# Menyimpan buku dalam list
daftar_matkul= [matkul1, matkul2, matkul3]

for Matkul in daftar_matkul:
    print(f" Matkul   : {Matkul.nama}")
    print(f" Pengajar : {Matkul.pengajar}")
    print(f" Sks      : {Matkul.sks}")
