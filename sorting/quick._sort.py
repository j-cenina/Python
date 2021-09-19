from random import randint

def create_array(size=10,max=50):
    return [randint(0, max) for _ in range(size)]

def quick_sort(a):
    if len(a) <= 1: return a
    small, equal,large = [],[],[]
    pivot=a[randint(0,len(a)-1)]
    for x in a:
        if x < pivot: small.append(x)
        elif x == pivot: equal.append(x)
        else:large.append(x)
    return quick_sort(small) + equal + quick_sort(large)

a = create_array()
print("unsorted:",a)
b = quick_sort(a)
print("sorted:",b)



