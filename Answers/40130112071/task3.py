def remove_duplicates(array):
    n=len(array)
    for i in range(0, len(array)):
        for j in range(i+1,len(array)):
            if(array[i]==array[j]):
                n-=1
    return n
                

array=[1,1,2,2,3,4,5,5]
print(remove_duplicates(array))