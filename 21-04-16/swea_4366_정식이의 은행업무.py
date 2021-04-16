T = int(input())
for test_case in range(1,T+1):
    n_2 = list(input())
    n_3 = list(input())
    chk = []
    for i in range(len(n_2)):
        if n_2[i] == '1':
            n_2[i] = '0'
            chk.append(int(''.join(n_2),2))
            n_2[i] = '1'
        else:
            n_2[i] = '1'
            chk.append(int(''.join(n_2),2))
            n_2[i] = '0'
    res = 0
    for i in range(len(n_3)):
        d = ['0', '1', '2']
        origin = n_3[i]
        d.remove(n_3[i])
        for j in d:
            n_3[i] = j
            tmp = int(''.join(n_3),3)
            if tmp in chk:
                res = tmp
                break
        if res != 0:
            break
        n_3[i] = origin

    print('#{} {}'.format(test_case,res))