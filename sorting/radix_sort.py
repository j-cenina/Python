def radix_sort(alist):
	Radix = 10
	maxlength = False #maxLength=0
	temp,placement =-1,1
	
	while not maxlength:
		maxlength = True
		#declare and initialize buckets
		buckets = [list() for _ in range(Radix)]
		
		#split alist b/w lists(buckets/radix)
		for item in alist:
			temp = int(item//placement)
			buckets[temp % Radix].append(item)
			if maxlength and temp > 0:
				maxlength = False
				
		#empty lists into alist array
		#concatenation
		a = 0
		for b in range(Radix):
			buck = buckets[b]
			for element in buck:
				alist[a] = element
				a += 1
				
		#move to next significant digit
		placement*=Radix
		
new_list = [55,45,3,289,213,1,288,53,2]
radix_sort(new_list)
print(new_list)