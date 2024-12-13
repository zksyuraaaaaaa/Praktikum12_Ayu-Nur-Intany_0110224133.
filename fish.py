from Animal import animal

class fish(animal):
    

    def __init__(self, nama, makanan, hidup, berkembang_biak,bernapas,habitat) :
        super().__init__(nama,makanan, hidup, berkembang_biak)
        self.bernapas = bernapas
        self.habitat = habitat

    # Method
    def info_fish(self):
        super().info_animal()
        print("Bernapas \t\t:",self.bernapas,"\nTempat Habitat\t\t:",self.habitat)

print()
lumba_lumba = fish("Lumba-lumba","ikan","Di Laut","Melahirkan","Paru-paru","Air tawar atau Air asin")
print("## Info Fish ##")
lumba_lumba.info_fish()
paus_orca = fish("Paus Orca","ikan","Di Laut","Melahirkan","Paru-paru","Perairan Dingin")
print("## Info Fish ##")
paus_orca.info_fish()
pari = fish("Pari","ikan","Di Perairan Laut","Bertelur dan Melahirkan","Insang","Air tawar atau Air asin")
print("## Info Fish ##")
pari.info_fish()