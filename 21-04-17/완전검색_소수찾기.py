res = []
def prime_number(n):
    if n==0 or n==1:
        return False
    
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def perm(arr, depth, n, k):
    # depth가 0부터 시작하여 k라면 k개를 모두 뽑은 것이므로 print하고 return
    if (depth == k):
        global res
        res.append(arr[:k])
        return arr[:k]
    for idx in range(depth, n):
        # 각 depth에 대해 남아 있는 것들 중에 모두 뽑아보고,
        # 해당 경우에 대해 재귀적으로 perm 함수를 돌리고,
        # 원상복구 하여 다시 경우의 수를 찾는다
        arr[idx], arr[depth] = arr[depth], arr[idx]
        perm(arr, depth+1, n, k)
        arr[idx], arr[depth] = arr[depth], arr[idx]

def solution(numbers):
    answer = 0
    num = []
    visited = []
    for i in numbers:
        num.append(i) 
    n = len(num)
    for i in range(1,n+1):
        perm(num,0,n,i)
        
    for i in res:
        k = int(''.join(i))
        if k not in visited:
            if prime_number(k):
                visited.append(k)
    answer = len(visited)
    
    return answer
