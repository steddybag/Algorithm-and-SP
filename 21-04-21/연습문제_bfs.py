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
    cur = s.pop(0) # queue는 앞에서부터 pop 0인지 명시해줄 것! dfs와 bfs 차이 -1이냐 0이냐
    if visited[cur] == 0:
        visited[cur] = 1
        print(cur,end='-')
        for i in range(1,N+1): #
            if adj_list[cur][i] == 1:
                if visited[i] == 0:
                    s.append(i)