import sys
sys.stdin = open('input.txt','r')

N = int(input())
arr = list(map(int,input().split()))

adj_list = [[0]*(N+1) for _ in range(N+1)]

for i in range(len(arr)//2):
        adj_list[arr[2*i]][arr[2*i + 1]] = 1
        adj_list[arr[2 * i + 1]][arr[2 * i]] = 1
visited = [0] * (N+1)

s = [] # stack처럼 pop은 -1
s.append(1)

while s:
    cur = s.pop(-1)
    if visited[cur] == 0:
        visited[cur] = 1
        print(cur,end='-')
        for i in range(N,0,-1): # range(1,N+1) 이면 1-3-7-6-5-2-4 가 됩니다.
            if adj_list[cur][i] == 1:
                if visited[i] == 0:
                    s.append(i)