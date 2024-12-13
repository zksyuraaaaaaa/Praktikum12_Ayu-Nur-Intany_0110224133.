class animal:
    #konstruktor
    def __init__(self, nama, makanan, hidup, berkembang_biak) :
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
        
    #method informasi
    def info_animal(self):
        print("nama hewan\t\t:",self.nama, "\nMakanan\t\t\t:", self.makanan, "\nhidup\t\t\t:", self.hidup,"\nBerkembangBiak\t\t: ", self.berkembang_biak )
    
#objek 
kucing = animal("Kucing", "daging", "hidup", "melahirkan")
kucing.info_animal()

anjing = animal("Anjing", "Daging", "hidup", "melahirkan")
anjing.info_animal()

serigala = animal("Serigala", "daging", "hidup", "melahirkan")
serigala.info_animal()