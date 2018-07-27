'''
归并排序
时间复杂度:O(nlog(n))
稳定性：稳定的
'''

def merge_sort(x,low,high):
    if low == high:
        pass
    else:
        mid = (low + high)//2
        merge_sort(x,low,mid)
        merge_sort(x,mid+1,high)
        i = low
        j = mid + 1
        l = [-1 for s in range(high+1-low)]
        temp = 0
        while i<=mid and j<=high:
            if x[i] <= x[j]:
                l[temp] = x[i]
                temp = temp + 1
                i = i+1
            elif x[j] < x[i]:
                l[temp] = x[j]
                temp = temp + 1
                j = j+1
        while i<=mid:
            l[temp] = x[i]
            temp = temp + 1
            i = i + 1
        while j <=high:
            l[temp] = x[j]
            temp = temp + 1
            j = j+1
        for ss in range(low,high+1):
            x[ss] = l[ss-low]
            print(x)

