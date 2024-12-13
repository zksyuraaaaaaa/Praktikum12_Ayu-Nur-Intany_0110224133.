from Animal import animal

class bird(animal):
    

    def __init__(self, nama, makanan, hidup, berkembang_biak,Warna,paruh) :
        super().__init__(nama,makanan, hidup, berkembang_biak)
        self.warna = Warna
        self.paruh = paruh

    # Method
    def info_bird(self):
        super().info_animal()
        print("Warna\t\t\t:",self.warna,"\njenis paruh\t\t:",self.paruh)

print()
elang = bird("Elang","Daging","Ditebing","Menghasilkan Telur","Coklat","Bengkok dan Lancip")
print("## Info Bird ##")
elang.info_bird()
cendrawasih = bird("cendrawasih","buah-buahan atau Serangga","Dihutan","Menghasilkan Telur","merah,biru,hijau dll","Ramping,tebal dan Lancip")
cendrawasih.info_bird()
merak = bird("Merak","buah-buahan atau Serangga","Dihutan dekat sungai","Menghasilkan Telur","biru,hijau dan coklat","Pendek,tebal dan Berbentuk kerucut")
merak.info_bird()