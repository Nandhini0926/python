def bs(a, l, h, x): 

	if h>= l: 

		m = (h + l) // 2

		if a[m] == x: 
			return m 

		elif a[m] > x: 
			return bs(a, l, m - 1, x) 
		else: 
			return bs(a, m + 1, h, x) 
	else: 
		return -1
a = [ 8, 7, 3, 12, 4 ] 
x = 3
result = bs(a, 0, len(a)-1, x) 
if result != -1: 
	print("element is in index", str(result)) 
else: 
	print("element are not  in array") 

