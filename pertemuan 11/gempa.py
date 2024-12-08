class gempa:
    def __init__(self, skala, lokasi):
        self.skala = skala
        self.lokasi = lokasi
    def dampak(self):        
        print(f"ada gempa baru nih di {self.lokasi}")
        print(f"skala dari gempa ini adalah {self.skala}")
        if self.skala < 2 :
            print('dampak gempa ga berasa')
        elif self.skala >=2 and self.skala <= 4 :
            print('dampak gempa bangunan retak-retak')
        elif self.skala > 4 and self.skala <= 6 :
            print('dampak gempa bangunan roboh')    
        elif self.skala > 6 :
            print('dampak gempa bangunan roboh dan potensi tsunami')
        else :
            print('sistem tidak  terbaca')

# gempa().skala = 2
# gempa().dampak()

gempa2 = gempa(2, "sumbawa")
gempa2.dampak()