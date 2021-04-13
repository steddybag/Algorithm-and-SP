N = int(input())
arr = list(map(int,input().split()))
for i in range(N):
    #총 배열의 길이만큼 반복문 실행
    min_val = arr[i]
    min_ind = i
    for j in range(i,N):
    #완료된 앞의 배열은 탐색 X:
        if min_val > arr[j]:
            min_val = arr[j]
            min_ind = j
        # 새로운 min 값이 나오면 위와 같이 값과 index를 저장
        # i~N까지 즉 i = 2인 자리를 선택 정렬하기위해
        # 3번째원소부터 마지막 원소까지만 탐색하면 됩니다.
    # i와 min_ind가 다르면 교환이 발생
    # 아닐 경우 교환없이 진행
    if i != min_ind:
        tmp = arr[i]
        arr[i] = arr[min_ind]
        arr[min_ind] = tmp
        print(arr[i],arr[min_ind])
        #위의 문들은 swap함수가 없다고 가정하여 만든 구문입니다.
    print(arr)