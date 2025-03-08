class Orang:
    def __init__(self, namadepan, namabelakang, nomer_id):
        self.namadepan = namadepan
        self.namabelakang = namabelakang
        self.nomer_id = nomer_id

    def tampilkan_info(self):
        print(f"Nama: {self.namadepan} {self.namabelakang}")
        print(f"Nomer ID: {self.nomer_id}")

class Karyawan(Orang):
    TETAP = "Tetap"
    TIDAK_TETAP = "Tidak Tetap"

    def __init__(self, *args, status_karyawan, **kwargs):
        super().__init__(*args, **kwargs)  
        self.status_karyawan = status_karyawan

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Status Karyawan: {self.status_karyawan}")
