'''
算法复杂度:O(n^2)
'''

def Bubblesort(x):
	N = len(x)
	for i in range(N):
		for j in range(1,N-i):
			if x[j-1] > x[j]:
				temp = x[j]
				x[j] = x[j-1]
				x[j-1] = temp

if __name__ == '__main__':
	arr = [12,31,3,31,3,13,42637,62,5464,276,54265,413,7653,762]		
	Bubblesort(arr)
	print(arr)
