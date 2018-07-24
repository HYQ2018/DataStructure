'''
堆排序
时间复杂度：O(nlog(n))
稳定性：堆排序为不稳定排序

'''


#调整堆
def adjust_heap(x,i,size):
	lchild = i*2+1
	rchild = i*2+2
	max = i
	if i < int(size/2):
		if lchild < size and x[lchild] > x[max]:
			max = lchild
		if rchild < size and x[rchild] > x[max]:
			max = rchild
		if max != i:
			x[max],x[i] = x[i],x[max]
			adjust_head(x,max,size)

#建立堆
def build_heap(x):
    size = len(x)
    for i in range(0,int(size/2))[::-1]: #将range(10)倒序
        print(i)
        adjust_heap(x,i,size)

#堆排序
def sort_heap(x):
	build_heap(x)
	for i in range(0,len(x))[::-1]:
		x[0],x[i] = x[i],x[0]
		adjust_heap(x,0,i)
	
	
	
	
	
