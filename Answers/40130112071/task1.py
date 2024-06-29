def find_missing_num(array):
    n=len(array)
    sum1=(n*(n+1))//2
    sum2=sum(array)
    return sum1-sum2

array=[5,2,0,3,1]
print(find_missing_num(array))
