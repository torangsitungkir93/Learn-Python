import sys
import timeit

data_list = [1,2,3,4,5,"pisang goreng",False];
data_tuple = (1,2,3,4,5,"pisang goreng",False);

besarDataList = sys.getsizeof(data_list)
besarDataTuple = sys.getsizeof(data_tuple)

waktuDataList = timeit.timeit(stmt="[1,2,3,4,5,6,7,8]",number=1000000)
waktuDataTuple = timeit.timeit(stmt="(1,2,3,4,5,6,7,8)",number=1000000)

print("Besasr data List : ",besarDataList)
print("Besar data Tuple : ",besarDataTuple)
print("Waktu untuk memproses list : ",waktuDataList)
print("Waktu untuk memproses tuple : ",waktuDataTuple)