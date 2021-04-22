from collections import deque

def bfs(N, M):
    queue = deque()
    queue.append((N, 0))
    check = {}
    while queue:
        item, count = queue.popleft()
        if check.get(item, 0):
            continue
        check[item] = 1
        if item == M:
            return count
        count += 1
        if 0 < item + 1 <= 1000000:
            queue.append((item + 1, count))
        if 0 < item - 1 <= 1000000:
            queue.append((item - 1, count))
        if 0 < item * 2 <= 1000000:
            queue.append((item * 2, count))
        if 0 < item - 10 <= 1000000:
            queue.append((item - 10, count))


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    print('#{} {}'.format(tc, bfs(N, M)))