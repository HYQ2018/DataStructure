'''

时间复杂度：O(N*base)
base是位数
空间复杂度：O(N)
稳定性：稳定
'''

def radix_sort(x,base):	
	for k in range(base):
		buck = [[] for i in range(10)]
		for i in x:
			buck[int(i/(10**k))%10].append(i)
		x = [j for i in buck for j in i]
	return x


		
	
