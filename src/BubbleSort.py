a = [9, 5, 2, 3, 8]

for n in range(len(a)):
    swapped = False
    for j in range(len(a)-1,n,-1):
        if a[j] < a[j-1]:
            temp = a[j]
            a[j] = a[j-1]
            a[j-1] = temp
            swapped = True
    
    if swapped == False:
        break
    
print a