from abc import ABC, abstractmethod

# Kelas Abstrak
class Kendaraan(ABC):
    @abstractmethod
    def jenis_kendaraan(self):
        pass

    @abstractmethod
    def jumlah_roda(self):
        pass

# Kelas turunan Mobil dari kelas Kendaraan
class Mobil(Kendaraan):
    def jenis_kendaraan(self):
        return "Mobil"

    def jumlah_roda(self):
        return 4

#Kelas turunan Motor dari kelas Kendaraan
class Motor(Kendaraan):
    def jenis_kendaraan(self):
        return "Motor"

    def jumlah_roda(self):
        return 2

#Kelas turunan Sepeda dari kelas Kendaraan
class Sepeda(Kendaraan):
    def jenis_kendaraan(self):
        return "Sepeda"

    def jumlah_roda(self):
        return 2

class Bus(Kendaraan):
    def jenis_kendaraan(self):
        return "Bus"
    
    def jumlah_roda(self):
        return 6
    
# Fungsi untuk menampilkan informasi kendaraan
def tampilkan_info_kendaraan(kendaraan):
    print(f"Jenis Kendaraan: {kendaraan.jenis_kendaraan()}, Jumlah Roda: {kendaraan.jumlah_roda()}")

# Membuat objek dari kelas Mobil, Motor, dan Sepeda
mobil = Mobil()
motor = Motor()
sepeda = Sepeda()
bis = Bus()

# Menampilkan informasi dari masing-masing kendaraan
tampilkan_info_kendaraan(mobil)   
tampilkan_info_kendaraan(motor)    
tampilkan_info_kendaraan(sepeda)
tampilkan_info_kendaraan(bis)