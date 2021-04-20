import sys
sys.stdin = open('input.txt','r')

def qsort(a,low,high):
    if low < high:
        pivot = part(a,low,high)
        qsort(a,low,pivot-1)
        qsort(a,pivot+1,high)

def part(a,pivot,high):
    # 맨 왼쪽 인자가 pivot역할
    i = pivot+1
    j = high
    while True:
        while i<high and a[i] < a[pivot]:
            i += 1
            #pivot을 기준으로 왼쪽에는 작은게 와야하므로 계속해서 진행
        while j>pivot and a[j] > a[pivot]:
            j -= 1

        if j <= i : #i랑 j가 교차하면 해당 반복문 break
            break
        # 아닌게 발생하면
        a[i],a[j] = a[j],a[i]
        #교환 후 넘어가기
        i += 1
        j -= 1
    a[pivot], a[j] = a[j], a[pivot]
    # pivot 기준
    return j

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    qsort(arr,0,N-1)
    print('#{} {}'.format(tc,arr[N//2]))