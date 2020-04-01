 # Input Outpu File

 # Membuat File Text


file = open("data.txt",'w')
file.write("Ini adalah data text yang dibuat dengan menggunakan python")
file.write("\nIni baris kedua")
file.write("\nIni baris ketiga")
file.close()

# Appending mode

file3 = open("data.txt","a")
file3.write("\nIni baris yang dibuat dengan mode Append")
file3.close()

# Membaca File
file2 = open("data.txt","r")
#print(file2.read())
print(file2.readline(1))
print(file2.readline(3))
print(file2.readline(4))
