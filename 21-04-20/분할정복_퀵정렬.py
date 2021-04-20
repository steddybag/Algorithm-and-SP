def qsort(a,low,high):
    if low<high:
        pivot = partition(a,low,high)
        qsort(a,low,pivot-1)
        qsort(a,pivot+1,high)

def partition(a,pivot,high):
    i = pivot + 1
    j = high
    while True:
        while i < high and a[i] < a[pivot]:
            i+=1
        # 좌측 부분을 쭉 스캔
        while j > pivot and a[j] > a[pivot]:
            j-=1

        if j<=i:
            break
        #우측 부분에서 스캔
        a[i],a[j] = a[j],a[i]
        i+=1
        j-=1
    
    a[pivot],a[j] = a[j], a[pivot]
    #기준을 바꾼다.
    return j

a = [11,45,22,81,23,34,99,22,17,8]
print('정렬전:\t',a)
qsort(a,0,len(a)-1)
print('정렬후:\t',a)

