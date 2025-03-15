class Mobil:
    def __init__(self, name):
        self.name = name

    def mesin(self):
        return f"{self.name} : Mobil 2000cc 4 Cylinder"

class Motor:
    def __init__(self, name):
        self.name = name

    def mesin(self):
        return f"{self.name} : Motor 250cc 4 Cylinder"

def tampilkan_mesin(kendaraan):
    print(kendaraan.mesin())

mobil = Mobil("Civic")
motor = Motor("ZX 25")

tampilkan_mesin(mobil)  
tampilkan_mesin(motor)  