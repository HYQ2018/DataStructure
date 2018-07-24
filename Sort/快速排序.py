'''
快速排序：
算法复杂度:O(nlog(n))
最坏情况（逆序）:O（n^2）
稳定性：不稳定排序
'''

def quick_sort(x,left,right):
	if left < right:
		mid = partition(x,left,right)
		quick_sort(x,left,mid-1)
		quick_sort(x,mid+1,right)
def partition(x,left,right):
	priot = x[right]
	while left<right:
		while left < right and x[left] <= priot:
			left = left + 1
		x[right] = x[left]
		while left < right and x[right] >= priot:
			right = right - 1
		x[left] = x[right]
	x[left] = priot
	return left
	
if __name__ == '__main__':
	arr = [12,3,3415441,4213,4312,3,42,43,54,51,4215,4,512134,57,8,4,3654,3735]
	quick_sort(arr,0,len(arr)-1)


