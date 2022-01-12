def banding(ar) :
    if ar[0]==ar[len(ar)-1] :
        return "True"
    else :
        return "False"

arr = []
n = int(input("Masukkan jumlah array : "))
for i in range(n) :
    a = int(input())
    arr.insert(i,a)
print(banding(arr))



        
    
