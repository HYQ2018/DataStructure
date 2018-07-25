'''
选择排序
时间复杂度:O(n^2)
稳定性：不稳定
'''

def select_sort(x):
	N = len(x)
	for i in range(N):
		for j in range(i,N):
			if x[j] < x[i]:
				x[i],x[j] = x[j],x[i]


