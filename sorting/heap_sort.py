#main function
def heap_sort(lst):
    n = len(lst)
    #max heap
    for i in range(n-1, -1, -1):
        heapify(lst, n, i)
    #for i in range(0, n-1):
        #heapify(lst, n, i)
        
    for i in range(n-1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        heapify(lst, i, 0)

def heapify(lst, n, i):
    largest = i
    l = 2*i+1
    r = 2*i+2
    if l < n and lst[i] < lst[l]:
        largest = l
    if r < n and lst[largest] < lst[r]:
        largest = r
    if largest != i: 
        lst[i],lst[largest] = lst[largest],lst[i] # swap 
        heapify(lst, n, largest)

new_list = [10, 7, 2, 6, 5, 4, 8, 1, 3, 9]
heap_sort(new_list)
print(new_list)