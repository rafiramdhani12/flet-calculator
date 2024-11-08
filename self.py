class Hewan:
    def __init__(self,nama):
        self.nama = nama # ! self digunakan untuk merujuk ke instance
        
    def berbicara(self):
        print(f"hewan {self.nama} berbicara")
        

kucing = Hewan("kucing")
kucing.berbicara()

def chelsea():
    count = 1
    for i in range(4):
        print("🧑🏿"*count)
        count += 1
    
chelsea()

class Nama:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
        
person1 = Nama("perrel" , 35)
print(person1.nama)
print(person1.umur)
