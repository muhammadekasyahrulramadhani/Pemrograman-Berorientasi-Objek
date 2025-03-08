class Orang:
    def __init__(self, nama_depan, nama_belakang, nomer_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomer_id = nomer_id

    def tampilkan_info(self):
        print(f"Nama: {self.nama_depan} {self.nama_belakang}")
        print(f"Nomer ID: {self.nomer_id}")

class Pelajar:
    def __init__(self):
        self.matkul = []
    
    def enrol(self, mata_kuliah): 
        self.matkul.append(mata_kuliah) 
        return f"{mata_kuliah} berhasil ditambahkan ke daftar mata kuliah."
    
    def daftar_matkul(self):
        if self.matkul: 
            return f"Mata kuliah yang diambil: {', '.join(self.matkul)}"
        else: 
            return "Tidak ada mata kuliah yang diambil."

class Pengajar:
    def __init__(self):
        self.matkul_diajar = []

    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)

    def __str__(self):
        return f"Mata Kuliah yang diajar: {', '.join(self.matkul_diajar) if self.matkul_diajar else 'Tidak ada mata kuliah yang diajar'}"

class Asdos(Orang, Pelajar, Pengajar):
    def __init__(self, nama_depan, nama_belakang, nomer_id):
        Orang.__init__(self, nama_depan, nama_belakang, nomer_id)
        Pelajar.__init__(self)
        Pengajar.__init__(self)
