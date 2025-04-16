# Parent Class
class Rekening:
    def __init__(self, nama, no_rekening, saldo):
        self.nama = nama
        self.no_rekening = no_rekening
        self.saldo = saldo

# Child Class
class Nasabah(Rekening):
    def tampilkan_data(self):
        print(f"Nama        : {self.nama}")
        print(f"No. Rekening: {self.no_rekening}")
        print(f"Saldo       : {self.saldo:,.2f}")  # Format saldo dengan 2 desimal dan pemisah ribuan

# Membuat objek dari class Nasabah
nasabah1 = Nasabah("Budi", 5555, 500000)
nasabah2 = Nasabah("Wati", 6666, 2000000)

# Menampilkan data nasabah
print("Data Nasabah 1   :")
nasabah1.tampilkan_data()
print("\nData Nasabah 2 :")
nasabah2.tampilkan_data()