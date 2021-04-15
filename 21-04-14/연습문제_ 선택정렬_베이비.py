#트리풀 우선
# A = '667767'
A = '123333'
cnt = [0] * 10
for i in A:
    cnt[int(i)] +=1

run = triplet = 0

for i in range(10):
    if cnt[i] >= 3:
        triplet +=1
        cnt[i] -= 3

    if i>1:
        if cnt[i]*cnt[i-1]*cnt[i-2] > 0:
            run += 1
            cnt[i] -= 1
            cnt[i-1] -= 1
            cnt[i-2] -= 1

if run + triplet == 2:
    print('Baby-gin')