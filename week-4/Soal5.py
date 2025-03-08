class Orang:
    def __init__(self, nama_depan, nama_belakang, nomer_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomer_id = nomer_id

    def tampilkan_info(self):
        print(f"Nama: {self.nama_depan} {self.nama_belakang}")
        print(f"Nomer ID: {self.nomer_id}")

class Mahasiswa(Orang):
    SARJANA = "Sarjana"
    MASTER = "Master"
    DOKTOR = "Doktor"

    def __init__(self, jenjang, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.jenjang = jenjang
        self.matkul = []  

    def enroll(self, mata_kuliah):
        self.matkul.append(mata_kuliah)
    
    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Jenjang: {self.jenjang}")
        print(f"Mata Kuliah: {', '.join(self.matkul) if self.matkul else 'Belum mengambil mata kuliah'}")

class Karyawan(Orang):
    TETAP = "Tetap"
    TIDAK_TETAP = "Tidak Tetap"

    def __init__(self, *args, status_karyawan, **kwargs):
        super().__init__(*args, **kwargs)  
        self.status_karyawan = status_karyawan

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Status Karyawan: {self.status_karyawan}")

class Dosen(Karyawan):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  
        self.matkul_diajar = []  

    def mengajar(self, matkul):
        self.matkul_diajar.append(matkul)  

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Mata Kuliah yang Diajarkan: {', '.join(self.matkul_diajar) }")

bowo = Mahasiswa(Mahasiswa.SARJANA, "Bowo", "Nugroho", "987654")
bowo.enroll("Basis Data")
bowo.tampilkan_info()