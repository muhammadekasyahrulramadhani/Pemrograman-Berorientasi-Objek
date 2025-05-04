class Sim_Cache:
    def __new__(cls):
        if not hasattr(cls, 'cache'):
            cls.cache = super().__new__(cls)
        return cls.cache

    def __init__(self):
        self.nama_web = "PBOTRI"
        self.create_cache()

    def create_cache(self):
        self.cache_source = self.nama_web + ".txt"
        self.cache_file_name = "cache_" + self.nama_web + ".txt"
        with open(self.cache_source, "r") as sf, open(self.cache_file_name, "w") as cf:
            cf.write(f"Ini adalah file cache dari web {self.nama_web}\n")
            line1 = False
            for l in sf:
                if "Start_cache" in l:  # menentukan baris awal cache
                    line1 = True
                if line1:
                    cf.write(l)  # menyalin cache dari source

    def get_cache(self):
        print(f"Nama file cache adalah {self.cache_file_name}")
        with open(self.cache_file_name, "r") as cf:
            print(cf.read())

print("=====Instansiasi pertama:=====")
cache1 = Sim_Cache()
cache1.get_cache()

print("\n=====Instansiasi kedua:=====")
cache2 = Sim_Cache()
with open("cache_PBOTRI.txt", "a") as add_cache:
    add_cache.write("\n***Baris tambahan di file cache***")
cache2.get_cache()
