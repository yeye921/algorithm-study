def solution(n):
    ans = 0
    q = -1
    r = '' # 문자열 이용
    while(q != 0):
        q = n // 3
        r += str(n % 3)
        n = q
        
    l = len(r)
    
    for i in range(l): 
        if r[i] == '0':
            continue
        else:
            ans += 3**(l-1-i)*int(r[i]) # 인덱스를 이용한 처리 주의하기
    
    return ans




# 다른 풀이
def solution(n):
    r = ''
    while n:   # n이 0이면 탈출
        r += str(n % 3)
        n = n // 3

    ans = int(r,3) # 3진수로 표현된 문자열 r을 10진수 정수로 변환함
    return ans
        
        
