# Parent Class
class Rekening:
    def __init__(self, nama, no_rekening, saldo):
        self.nama = nama
        self.no_rekening = no_rekening
        self.saldo = saldo

    def setor_tunai(self, nominal_setor_tunai):
        self.saldo += nominal_setor_tunai
        print(f"{self.nama} setor tunai: {nominal_setor_tunai:,.2f}. Saldo sekarang: {self.saldo:,.2f}")

    def tarik_tunai(self, nominal_tarik_tunai):
        if nominal_tarik_tunai <= self.saldo:
            self.saldo -= nominal_tarik_tunai
            print(f"{self.nama} tarik tunai: {nominal_tarik_tunai:,.2f}. Saldo sekarang: {self.saldo:,.2f}")
        else:
            print(f"{self.nama} gagal tarik tunai: Nominal saldo tidak mencukupi.")

    def transfer(self, penerima, nominal_transfer):
        if nominal_transfer <= self.saldo:
            self.saldo -= nominal_transfer
            penerima.saldo += nominal_transfer
            print(f"Transfer sebesar {nominal_transfer:,.2f} dari rekening {self.no_rekening} ke rekening {penerima.no_rekening} berhasil.")
        else:
            print(f"{self.nama} gagal melakukan transfer: Nominal saldo tidak mencukupi.")

# Child Class
class Nasabah(Rekening):
    def tampilkan_data(self):
        print(f"Nama        : {self.nama}")
        print(f"No. Rekening: {self.no_rekening}")
        print(f"Saldo       : {self.saldo:,.2f}")  # Format saldo dengan 2 desimal dan pemisah ribuan

# Membuat objek dari class Nasabah
nasabah1 = Nasabah("Budi", 5555, 500000.00)
nasabah2 = Nasabah("Wati", 6666, 2000000.00)

# Menampilkan data nasabah sebelum transaksi
print("Data Nasabah Sebelum Transaksi   :")
print("Data Nasabah 1 :")
nasabah1.tampilkan_data()
print("\nData Nasabah 2  :")
nasabah2.tampilkan_data()

# Simulasi transaksi setor tunai
print("\nSimulasi Transaksi Setor Tunai:")
nasabah1.setor_tunai(1000000)  # Nasabah 1 setor tunai 1.000.000
nasabah2.tarik_tunai(1000000)   # Nasabah 2 tarik tunai 1.000.000

# Menampilkan data nasabah setelah transaksi setor tunai
print("\nData Nasabah Setelah Transaksi Setor Tunai:")
print("Data Nasabah 1:")
nasabah1.tampilkan_data()
print("\nData Nasabah 2:")
nasabah2.tampilkan_data()

# Simulasi transaksi transfer
print("\nSimulasi Transaksi Transfer:")
nasabah1.transfer(nasabah2, 500000)  # Nasabah 1 transfer 500.000 ke Nasabah 2

# Menampilkan data nasabah setelah transaksi transfer
print("\nData Nasabah Setelah Transaksi Transfer:")
print("Data Nasabah 1:")
nasabah1.tampilkan_data()
print("\nData Nasabah 2:")
nasabah2.tampilkan_data()