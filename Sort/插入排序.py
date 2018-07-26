'''
插入排序
时间复杂度:O(n^2)
稳定性:稳定
'''
def insert_sort(x):
	N = len(x)
	for i in range(1,N):
		j = i -1
		key = x[i]
		while j >= 0:
			if x[j] > key:
				x[j+1] = x[j]
				x[j] = key
			j = j -1
			
