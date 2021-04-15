a = [5,7,2,34,8]

def selectionSort(A,n):
    if n == len(A):
        return
    else:
        min = n
        for i in range(n,len(A)):
            if A[i] < A[min]:
                min = i
        A[min],A[n] = A[n],A[min]
        selectionSort(A,n+1)
selectionSort(a,0)
print(a)

