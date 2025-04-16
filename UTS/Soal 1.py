class Konversi:
    def __init__(self, mil):
        self.mil = mil

    def konversi_mil_ke_kilometer(self):
        return self.mil * 1.60934

# Input dari pengguna dengan satuan mil
mil_input = float(input("Masukkan angka dalam satuan mil: "))

# Membuat objek dari kelas Konversi
konversi_objek = Konversi(mil_input)

# Mengkonversi mil ke kilometer dan menampilkan output
kilometer_output = konversi_objek.konversi_mil_ke_kilometer()
print(f"{mil_input} mil = {kilometer_output} kilometer")