class persegi:
    def __init__ (self, sisi):
        self.sisi = sisi
        
    def rumus_luas(self):
        return self.sisi ** 2
    
    def rumus_keliling(self):
        return self.sisi * 4

sisi = int(input("masukkan sisi persegi : "))
    
Persegi = persegi(sisi)
      
print("Luas persegi adalah : ", Persegi.rumus_luas())
print("Keliling persegi adalah : ", Persegi.rumus_keliling())