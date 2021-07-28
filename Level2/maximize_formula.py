# 내 풀이
# 연산자 우선순위 재정의하여 만들 수 있는 가장 큰 숫자 제출(+,-,*), 절댓값
# 연산자 들을 리스트에 담아서 중복걸러낸 다음에 우선순위 정함
# 같은 연산자 끼리는 앞에 있는 것의 우선순위가 더 높다
# 문자열 수식을 계산하는 eval()이용 
import math
from itertools import permutations
def solution(ex):
    res = []    # 연산자를 기준으로 문자열을 잘라서 저장하는 리스트
    ans = []    # 우선순위에 따라 나올 수 있는 값들의 리스트
    k = ["-","+","*"]
    _k = [i for i in ex if i in k]
    l = [(i,j) for i,j in enumerate(ex) if j in k] # -,+,* 가 들어있는 인덱스와 값 저장 
    dup = list(set(_k))
    
    # 잘라서 넣기
    for i in range(len(l)):
        if i == 0:
            b = l[0][0]
            print(b)
            res.append(ex[:b])
            res.append(ex[b])
        else:
            a = b + 1      # start
            b = l[i][0]    # end
            res.append(ex[a:b])
            res.append(ex[b])
    res.append(ex[b+1:])
    print(res)
        
    p = list(permutations(dup,len(dup))) # 우선순위 조합
    print(p)
    
    # 우선순위에 맞게 계산
    for i in range(len(p)): # 우선순위 조합 탐색
        arr = res[:]
        for j in range(len(dup)): # 연산자 우선순위(1,2,3) 탐색
            x = arr.count(p[i][j])
            for _ in range(x):  # 같은 연산자 여러개면 그 개수만큼 반복
                r = arr.index(p[i][j])
                arr[r-1] = str(eval(arr[r-1]+arr[r]+arr[r+1]))  # 연산자로 계산해서 그 값을 리스트에 다시 저장
                del arr[r] 
                del arr[r]
                print(arr)
        ans.append(abs(int(arr[0])))
    # print(ans)
    # print(p)    
    return int(max(ans))


    
# 더 나은 풀이
# 정규 표현식 이용
import re
from itertools import permutations

def solution(expression):
    #1
    op = [x for x in ['*','+','-'] if x in expression]
    op = [list(y) for y in permutations(op)]
    ex = re.split(r'(\D)',expression)

    #2
    a = []
    for x in op:
        _ex = ex[:]
        for y in x:
            while y in _ex:
                tmp = _ex.index(y)
                _ex[tmp-1] = str(eval(_ex[tmp-1]+_ex[tmp]+_ex[tmp+1])) # 나랑 똑같은 방식
                _ex = _ex[:tmp]+_ex[tmp+2:]  # del로 제거하는 대신에 슬라이싱 이용 
        a.append(_ex[-1])

    #3
    return max(abs(int(x)) for x in a)