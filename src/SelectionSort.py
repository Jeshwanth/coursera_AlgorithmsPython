a = [9, 5, 2, 3, 8]

for i in range(0,len(a)):
    k = i
    for n in range(i+1,len(a)):
        if a[n] < a[k]:
            k = n 
    temp = a[i]
    a[i] = a[k]
    a[k] = temp
    
print a