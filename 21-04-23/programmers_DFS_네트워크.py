def solution(n, computers):
    answer = 0
    # 네트워크 개수 visited 사용하여 계산
    visited = [0] * n

    for i in range(n):
        if visited[i] == 0:
            q = [i]
            while q:
                cur = q.pop()
                for j in range(len(computers[cur])):
                    if j != cur and visited[j] == 0 and computers[cur][j] == 1:
                        visited[j] = 1
                        q.append(j)
            answer += 1

    return answer