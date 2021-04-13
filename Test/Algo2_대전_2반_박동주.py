def preorder(N):
    cnt[0]+=1
    if child[N][0]!=0:
        preorder(child[N][0])
    if child[N][1]!=0:
        preorder(child[N][1])

T = int(input())
for tc in range(1,T+1):
    #이진 트리 N번 노드의 자손 노드 개수
    #1~V번 까지 노드 존재
    #이진 트리이므로 자손노드는 최대 2개
    # V 노드 개수, N 노드번호
    V, N = map(int,input().split())
    arr = list(map(int,input().split()))
    #VLR인 preorder 순회 사용하면 자손노드 개수 파악 가능
    child = [[0,0] for _ in range(V+1)]
    cnt = [0] #전역변수와 같은 효값 list의 주소값 참조
    #L,R child[0] child[1]로 표현
    for i in range(V-1): #edge수는 V-1
        st = arr[2*i]
        end = arr[2*i + 1]
        if child[st][0] == 0:
            child[st][0] = end
        else:
            child[st][1] = end
    preorder(N)
    #VLR식으로 순회하여 N번째 Node를 포함한 subtree만 순회
    cnt[0]-=1
    #본인을 포함한 수이므로 최종적으로 -1

    print('#{} {}'.format(tc, cnt[0]))