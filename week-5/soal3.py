class Barang:
    def __init__(self, merek, harga_satuan): 
        self.merek = merek 
        self.harga_satuan = harga_satuan 

    def mul(self, qty_jual): 
        print('Banyaknya penjualan:', qty_jual, 'buah')      
        return self.harga_satuan * qty_jual
    
class Penjualan:
    def __init__(self, merek, qty_jual): 
        self.merek = merek 
        self.qty_jual = qty_jual

redmi10 = Barang ("Redmi10", 2140) 
qty_maret = Penjualan ("Redmi10", 20) 
print(f"Total penjualan {redmi10.merek}: {redmi10.mul(qty_maret.qty_jual)} ribu")
