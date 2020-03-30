# Teknik Looping

namaBand = ['Payung Teduh',
            'ST 12',
            'Parah Yena'
            ]

kumpulanLagu = ['Akad',
                'Zona Nyaman',
                'Rumahku',
                'Sang Filsuf'
                ]
# enumerate
for i,band in enumerate(namaBand):
    print(i,': ',band)

# ZIP

for band,lagu in zip(namaBand,kumpulanLagu):
    print(band,'Menyanyi dengan judul lagu : ',lagu)

playlist = {'baby baby','ada apa dengan cinta','cenat-cenut','jaran goyang'}
playlist2 = {'Payung Teduh':'Akad',
             'fourtwnty':'Zona Nyaman',
             'Dialog Dini Hari':'Rumahku',
             }

for i,v in playlist2.items():
    print(i,"Lagunya : ",v)
