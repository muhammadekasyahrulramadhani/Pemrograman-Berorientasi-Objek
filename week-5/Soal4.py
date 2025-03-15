class Persegi:
    def keliling(self, sisi):
        return sisi * 4

class Lingkaran:
    def keliling(self, diameter):
        return 3.14 * diameter

class Segitiga:
    def keliling (self, sisi):
        return  sisi * 3

def hitung_keliling(bentuk, *args):
    return bentuk.keliling(*args)

persegi = Persegi()
lingkaran = Lingkaran()
segitiga = Segitiga()

print("Keliling Persegi:", hitung_keliling(persegi, 4))  
print("Keliling Lingkaran:", hitung_keliling(lingkaran, 14))
print("Keliling Segitiga:", hitung_keliling(segitiga, 8))  