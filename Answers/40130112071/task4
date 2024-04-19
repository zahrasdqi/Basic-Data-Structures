def merge_sorted_array(array1, array2):
    merge=[]
    i=0
    j=0
    while i<len(array1) and j<len(array2):
        if array1[i]<=array2[j]:
            merge.append(array1[i])
            i+=1
        else:
            merge.append(array2[j])
            j+=1
    
    while i<len(array1):
        merge.append(array1[i])
        i+=1
    while j<len(array2):
        merge.append(array2[j])
        j+=1

    return merge


array1=[1,2,3]
array2=[2,5,6]
print(merge_sorted_array(array1, array2))
