import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    V = [0 for i in range(N+1)]
    # len - 1 0은 0이므로
    arr = list(map(int,input().split()))
    # cloud 식으로 풀자
    cld = 1
    for i in range(len(arr)//2):
        cld += 1
        st = arr[2*i]
        end = arr[2*i +1]
        if V[st] == 0 and V[end] == 0:
            V[st], V[end] = cld, cld
        elif V[st]*V[end] == 0:
            num = V[st] + V[end]
            V[st] = num
            V[end] = num
        else:
            tmp = V[st]
            for j in range(len(V)):
                if V[j] == tmp:
                    V[j] = V[end]
    V = V[1:]
    cld += 1
    for j in range(len(V)):
        if V[j] == 0:
            V[j] = cld
            cld += 1
    print('#{} {}'.format(test_case,len(set(V))))