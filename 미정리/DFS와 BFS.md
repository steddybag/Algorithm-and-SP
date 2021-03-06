# 파이썬문법

### DFS와 BFS 차이

```python
while queue:
    a, b = queue[0][0],queue[0][1]
    queue.pop(0)
    for i in range(4):
        x = a+dx[i]
        y = b+dy[i]
        if n>x>=0 and m>y>=0 and s[x][y] == '1':
            queue.append([x,y])
            s[x][y] = s[a][b] + 1
         #BFS는 큐 사용
        # DFS는 stack 사용
        
    while queue : #BFS사용
        x, y = queue.pop(0)
        #print(queue)
        for i in range(4):
           nx = x + dx[i]
           ny = y + dy[i]
           #모퉁이가 아니라면
           if 0<=nx<16 and 0<=ny<16:
               if arr[nx][ny] == '0':
                   arr[nx][ny] = '1'
                   queue.append((nx,ny))
               elif arr[nx][ny] == '3':
                   res = 1
                   break
        if res == 1:
            break
```



### MAP 에선 pop과 append가 안된다(무조건 list)

```python
arr.append(arr.pop(0))
```



### 파이썬 특정 열만 inline for loop으로 표현 가능

```python
b = [i[0] for i in a]
```



### lambda를 활용한 새로운 기준 정렬 방법

```python
arr = sorted(arr,key=lambda x: x[0])
```



### 큐랑 스택의 차이

```python
큐
arr.pop(0)
스택
arr.pop(-1)

추가는 둘다
arr.append()
arr.extend()는 list 붙이기 할 때
```

### input과 split 시 list형태로 return

```python
arr = input().split()
['10', '2', '+', '3', '4', '+', '*', '.']
['5', '3', '*', '+', '.']
['1', '5', '8', '10', '3', '4', '+', '+', '3', '+', '*', '2', '+', '+', '+', '.']
```

### python 순열 라이브러리

```python
import permutation
```

### 파이썬 pop시 계산 순서에 주의

```python
나눗셈 뺄셈의 경우 먼저 pop된 경우가 정확한 계산에 방해가 될 수 있습니다.
따라서 num.pop(-2) * num.pop()
식으로 계산 필요

try :

except:
구문을 활용하여 error 관리 용이
	try:
        for i in inputList:
            if i == '.':
                result = MyList.pop()
                if len(MyList) != 0:
                    result = 'error'
                break
            elif i == '+':
                MyList.append(MyList.pop(-2) + MyList.pop())
            elif i == '-':
                MyList.append(MyList.pop(-2) - MyList.pop())
            elif i == '*':
                MyList.append(MyList.pop(-2) * MyList.pop())
            elif i == '/':
                MyList.append(MyList.pop(-2) // MyList.pop())
            else:  # 숫자는 int형으로 변환
                MyList.append(int(i))
                
    except:  # 에러
        result = 'error'
```



### 리스트에서 특정 항목 index 찾기

```python
list.index('c')
#단 index는 값이 없을시 오류를 반환
find함수는 값이 없을시 -1을 반환
```



### python 순열 라이브러리

```python
import permutation
```

### 

### dfs 방법 (재귀함수 및 여러가지가 존재)

```python
def dfs(x,y):
    global ans
    input_list[x][y]='2'
```

### 

### 파이썬은 함수 선언 후 굳이 변수값을 함수 내에 할당하지 않아도 된다.

```python
def rockscisorpaper(l_idx, r_idx):
    l, r = cards[l_idx-1], cards[r_idx-1]
```

### 특수한 경우면 경우에 따라 아래와 같이 나눌 것

```python
def rockscisorpaper(l_idx, r_idx):
    l, r = cards[l_idx-1], cards[r_idx-1]
    if l == r:
        return l_idx
    elif l == 1: # 가위
        if r == 3: return l_idx
        elif r == 2: return r_idx
    elif l == 2: # 바위
        if r == 1: return l_idx
        elif r == 3: return r_idx
    elif l == 3: # 보
        if r == 2: return l_idx
        elif r == 1: return r_idx
def cardgame(lo, hi):
    if lo == hi:
        return lo
    else:
        mid = (lo+hi) // 2
        l = cardgame(lo, mid)
        r = cardgame(mid+1, hi)
        return rockscisorpaper(l, r)
```

### 이진 탐색이나 이진트리로 나눌 때 아래의 방식 이용

```python
def cardgame(lo,hi):
    if lo == hi:
        return lo
    else:
        mid = (lo+hi) // 2
        l = cardgame(lo,mid)
        r = cardgame(mid+1,hi)
        return rockscisorpaper(l,r)
    
```

### 꼭 답을 찾는 방법을 택할 필요는 없다. 전체의 경우를 구한후 비교도 가능

```python
import permutation
전체의 경우를 싹 다 조사한 후 출력
```

