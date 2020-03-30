
# Fungsi dengan menggunakan argument Sederhana
def siswa(nama):
    print('Siswa ini bernama :',nama)

siswa("Torangto Situngkir")

# Fungsi menggunakan keywords arguments

def guru(nama,pelajaran):
    print("Guru ini bernama ",nama)
    print("Mengajari ",pelajaran)

guru(pelajaran="Olah Raga",nama="Endang")
# Fungsi dengan menggunakan default

def penjagaSekolah(nama,shift='Siang',galak="tidak") :
    print("Penjaga sekolah ini bernama : ",nama)
    print("Shiftnya : ",shift)
    print("Galak? : ",galak)

penjagaSekolah("Entis")
penjagaSekolah("Pak Maman","Malam")


