Data = [1,2,3,4,5,6,7];

# Pengakses List
Subdata1 = Data[3];
Subdata2 = Data[-3];
# Pemotong List
Subdata3 = Data[0:4];
Subdata4 = Data[-2:];

Data2 = [100,200,300,400,500,600,700];

# Penambah List
Data3 = Data+Data2;

# Merubah Konten dari list

print(Data3);


# Mencopy data ke variabel baru
a = Data[:]
a[4]=89

# Merubah Content list dengan menggunakan metoda slicing

Data[3:5] = [11, 12]

x = [Data,Data2]

y= x[1][5];

print("Hasil : ")
print(Data)
print(Data2)
print(x)
print(y)

# Method untuk list
print("Append")
Data.append(30)

panjangList = len(Data);

print(Data)
print(panjangList)