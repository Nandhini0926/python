def hs(a): 
	n = len(a) 
	for i in range(n // 2 - 1, -1, -1): 
		heapiy(a, n, i) 
        
	for i in range(n-1, 0, -1): 
		a[i], a[0] = a[0], a[i] 
		heapiy(a, i, 0) 


def heapiy(a, n, i): 
	larger = i
	left = 2 * i + 1	  
	right = 2 * i + 2	  

	if left < n and a[i] < a[left]: 
		larger = left 

	if right < n and a[larger] < a[right]: 
		larger = right 

	if larger != i: 
		a[i],a[larger] = a[larger],a[i] 
		heapiy(a, n, larger) 

        
a= [ 27, 10, 20, 7, 9, 17] 
hs(a) 
n = len(a) 
print ("sorted array are: ") 
for i in range(n): 
	print ("%d" %a[i]), 



