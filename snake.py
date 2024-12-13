from Animal import animal

class snake(animal):
    

    def __init__(self, nama, makanan, hidup, berkembang_biak,warna,habitat) :
        super().__init__(nama,makanan, hidup, berkembang_biak)
        self.warna = warna
        self.habitat = habitat

    # Method
    def info_snake(self):
        super().info_animal()
        print("Warna \t\t\t:",self.warna,"\nTempat Habitat\t\t:",self.habitat)

print()
king_cobra = snake("King Cobra","Daging","Di Hutan","Bertelur","Hitam","Hutan atau Rawa")
print("## Info Snake ##")
king_cobra.info_snake()
anaconda = snake("Anaconda","Daging","Di Hutan hujan tropis","Melahirkan","Hijau","Hutan atau Rawa daerah Tropis Amerika")
anaconda.info_snake()
sanca = snake("Sanca Batik","Daging","Di Hutan","Bertelur","coklat muda dan abu-abu kekuningan","Hutan atau Rawa")
sanca.info_snake()