class Pelajar:
    def __init__(self):
        self.matkul = []
    
    def enrol(self, mata_kuliah): 
        self.matkul.append(mata_kuliah) 
        return f"{mata_kuliah} berhasil ditambahkan ke daftar mata kuliah."
    def daftar_matkul (self):
        if self.matkul: 
            return f"Mata kuliah yang diambil: {', '.join(self.matkul)}"
        else: 
            return "Tidak ada mata kuliah yang diambil."

pelajar1 = Pelajar()
print(pelajar1.enrol("Matematika"))
print(pelajar1.enrol("Fisika"))
print(pelajar1.daftar_matkul())