# 소수 판별 => 에라토스테네스의 체 이용 (1.6~2초) 
def solution(n):
    cnt = 0
    for i in range(2,n+1): # 1은 소수 아니니까 제외
        for j in range(2,int(i**0.5+1)): # 2부터 자기자신의 제곱근까지, 정수처리 
            if i%j==0:
                break
        else:
            cnt += 1
    
    return cnt


# 다른 풀이(에라토스테네스의 체 이용2) (5~9초) 
# 루트 n이전까지 소수의 배수를 제거
def solution(n):
    num = set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num -= set(range(2*i,n+i,i)) 

    return len(num)

# 최적화 코드 (1.6~2초) 
def solution(n):
    num = set(range(2,n+1))

    for i in range(2,int(n**0.5)+1):
        if i in num:
            num -= set(range(i*i,n+i,i)) 

    return len(num)
        
        
