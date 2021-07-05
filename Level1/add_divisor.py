# 약수 구하기 => 1~n까지의 수 중 n이 나누어 떨어지는 것은 n의 약수이다
# 약수에 해당하면 result에 더해줌
def solution(n):
    result = 0
    for i in range(1,n+1):
        if n%i==0:
            result += i
    return result
        

# 최적화 코드 
def solution(n):
    return sum([i for i in range(1,n+1) if num%i==0])

# 다른 풀이
def solution(n):
    return n + sum([i for i in range(1,(num//2)+1) if num%i==0])
