def max_sum_subarray(array):
    maxsum=float('-inf')
    sum=0
    for num in array:
        sum=max(num,sum+num)
        maxsum=max(maxsum,sum)
        return maxsum
    
array=[-2, -1, -3, 4, -1, 2, 1, -5, 4]
print(max_sum_subarray(array))