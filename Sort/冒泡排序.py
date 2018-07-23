'''
// 分类 -------------- 内部比较排序
// 数据结构 ---------- 数组
// 最差时间复杂度 ---- O(n^2)
// 最优时间复杂度 ---- 如果能在内部循环第一次运行时,使用一个旗标来表示有无需要交换的可能,可以把最优时间复杂度降低到O(n)
// 平均时间复杂度 ---- O(n^2)
// 所需辅助空间 ------ O(1)
// 稳定性 ------------ 稳定
'''

def Bubblesort(x):
	N = len(x)
	count = 0
	for i in range(N):
		for j in range(1,N-i):
			count = count + 1
			if x[j-1] > x[j]:
				temp = x[j]
				x[j] = x[j-1]
				x[j-1] = temp
	print(count)

def Bubble_sort2(x):
	#带FLAG
	FLAG = 0
	N = len(x)
	count = 0
	for i in range(N):
		for j in range(1,N-i):
			count = count + 1
			if x[j-1] > x[j]:
				FLAG = 1
				temp = x[j]
				x[j] = x[j-1]
				x[j-1] = temp
		if FLAG == 0:
			print(count)
			break
	print(count)

if __name__ == '__main__':
	arr = [12,31,3,31,3,13,42637,62,5464,276,54265,413,7653,762]		
	Bubblesort(arr)
	print(arr)
	arr = list(range(100))
	Bubble_sort2(arr)
