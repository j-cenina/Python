def merge_sort(lst):
	n = len(lst)
	if n == 1 or n == 0:
		return lst
	else:
		length = n//2
		A = lst[:length]
		B = lst[length:]
		A = merge_sort(A)
		B = merge_sort(B)
		i, j = 0, 0
		lst = []
		while i < len(A) and j < len(B):
			if A[i] < B[j]:
				lst.append(A[i])
				i += 1
			else:
				lst.append(B[j])
				j += 1
		if i == len(A):
			lst += B[j:]
		else:
			lst += A[i:]
		return lst
		
list = [5,4,6,2,7,9,18,-39,0,17,24]
print("Your sorted list is", merge_sort(list))