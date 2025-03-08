class Orang:
    def __init__(self, nama_depan, nama_belakang, nomer_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomer_id = nomer_id

    def tampilkan_info(self):
        print(f"Nama: {self.nama_depan} {self.nama_belakang}")
        print(f"Nomer ID: {self.nomer_id}")

        