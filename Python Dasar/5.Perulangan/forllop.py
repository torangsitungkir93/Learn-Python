

gorengan =['bakwan','cireng','tahu isi','tempik']

# for g in gorengan:
#     print(g)
#     print(len(g))
#     print(len(gorengan))

buah = ['semangka','jeruk','apel']
sayur = ['kangkung','wortel','tomat','kentang']

daftarBelanja = [gorengan,buah,sayur];

for subDaftarBelanja in daftarBelanja:
    print(subDaftarBelanja)
    for komponen in subDaftarBelanja:
        print(komponen)