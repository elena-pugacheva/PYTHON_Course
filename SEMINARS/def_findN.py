def FindN(array):
    count=0
    for i in range(1,len(array)-1):
        if array[i-1]<array[i]>array[i+1]:
            count +=1
        return count