def linear_search(L,x):
	n=len(L)
	for i in range(n):
		if L[i]==x:
			return i
	return -1
L=[2,5,45,25,36,12,5,36,58,49,36,75,24,3,152,45,3256,212,235,22,33,65,29,37,71,19]
linear_search(L,33)