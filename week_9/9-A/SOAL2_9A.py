import math

class Lingkaran:
    def __init__(self, jari_jari):
        self._jari_jari = jari_jari

    @property
    def jari_jari(self):
        return self._jari_jari

    @jari_jari.setter
    def jari_jari(self, nilai):
        if nilai < 0:
            raise ValueError("Jari-jari tidak boleh negatif.")
        self._jari_jari = nilai

    @property
    def luas(self):
        return math.pi * (self._jari_jari ** 2)

    @property
    def keliling(self):
        return 2 * math.pi * self._jari_jari

    @classmethod
    def dari_diameter(cls, diameter):
        jari_jari = diameter / 2
        return cls(jari_jari)

    @staticmethod
    def konversi_ke_cm(jari_jari_inch):
        return jari_jari_inch * 2.54

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat objek Lingkaran
    lingkaran1 = Lingkaran(5)
    print(f"Jari-jari: {lingkaran1.jari_jari} cm")
    print(f"Luas: {lingkaran1.luas:.2f} cm²")
    print(f"Keliling: {lingkaran1.keliling:.2f} cm")

    # Mengubah jari-jari
    lingkaran1.jari_jari = 10
    print(f"Jari-jari baru: {lingkaran1.jari_jari} cm")
    print(f"Luas baru: {lingkaran1.luas:.2f} cm²")
    print(f"Keliling baru: {lingkaran1.keliling:.2f} cm")

    # Menggunakan class method
    lingkaran2 = Lingkaran.dari_diameter(20)
    print(f"Jari-jari dari diameter 20 cm: {lingkaran2.jari_jari} cm")

    # Menggunakan static method
    jari_jari_cm = Lingkaran.konversi_ke_cm(5)
    print(f"Jari-jari 5 inch dalam cm: {jari_jari_cm:.2f} cm")