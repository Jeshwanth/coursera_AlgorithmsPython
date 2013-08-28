a = [9, 5, 2, 3, 8]

for i in range(1,len(a)):
    k = i
    while (k != 0):
        if k > 0 and a[k] < a[k-1]:
            temp = a[k]
            a[k] = a[k-1]
            a[k-1] = temp
        k = k -1
    
print a