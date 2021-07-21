# for문으로 1부터 숫자들을 누적해서 더해가면서 n과 일치하는지 확인하는 방식
def solution(n):
    ans = 0
    for i in range(1,n+1):
        if accumulate(i,n) == None:
            continue
        else:
            ans += 1
    return ans
    
    
def accumulate(i,n):
    tmp = 0
    cnt = 0
    for i in range(i,n+1):
        tmp += i
        cnt += 1
        if tmp == n:
            return cnt # cnt개의 연속된 숫자들의 합으로 n을 나타낼 수 있다
        elif tmp > n:
            break
            return 0  


# 나와 같은 방식이지만 더 나은 풀이
def solution(n):
    ans = 0
    for i in range(1,n+1): 
        s = 0
        while s < n:
            s += i   #
            i += 1   # 이 2줄이 내 풀이에서 이중 for문 역할 
        if s == n:
            ans += 1
    
    return ans