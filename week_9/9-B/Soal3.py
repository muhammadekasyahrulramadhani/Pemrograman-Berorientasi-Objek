from collections import namedtuple

Orang=namedtuple("Orang", "nama anak")

class OrangInfo:
    def __init__(self, nama, anak):
        self._orang = Orang(nama, anak)

    @property
    def nama(self):
        return self._orang.nama

    @property
    def anak(self):
        return self._orang.anak

    def tampilkan_info(self):
        print("Nama : ", self.nama)
        print("Nama anak : ")
        for i in range(len(self.anak)):
            print(f"{i+1}. {self.anak[i]}")

john = OrangInfo("John Doe",["Timmy", "Jimmy"])
john.anak.append("Tina")
john.tampilkan_info()