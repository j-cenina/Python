def selection_sort(num):
    for i in range(len(num)):
        min_index = i
    
        for j in range(i+1,len(num)):
            if num[min_index] > num[j]:
                min_index = j
                
                temp = num[i]
                num[i] = num[j]
                num[j] = temp
            #print(num) here to show the sorting algorithm
    return num

nums = [5,3,7,6,9,2]
print(selection_sort(nums))
