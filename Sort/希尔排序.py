
'''
shell排序的时间复杂度：   
shell排序的时间复杂度是根据选中的 增量d 有关的，所以分析shell排序的时间复杂度是个比较麻烦的事；这里只给出答案，不推算了；
在最优的情况下，时间复杂度为：O（n ^ (1.3) ）   （元素已经排序好顺序）
在最差的情况下，时间复杂度为：O（n ^ 2）；
'''


def shell_sort(x):
    D = int(len(x)/2)
    while D>=1:
        for i in range(D,len(x)):
            j = i - D
            key = x[i]
            while j >= 0:
                if x[j] > key:
                    x[j+D] = x[j]
                    x[j] = key
                j = j - D
        D = int(D/2)
     
