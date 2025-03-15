class Hewan:
    def suara(self):
        return "Suara hewan"
class Sapi(Hewan):
    def suara(self):
        return "Sapi : Mooo"
class Anjing(Hewan):
    def suara(self):
        return "Anjing : Gug-Gug"

def tampilkan_suara(hewan):
    print(hewan.suara())

suara_hewan = Hewan()
sapi = Sapi()
anjing = Anjing()

tampilkan_suara(suara_hewan)  
tampilkan_suara(sapi)
tampilkan_suara(anjing)