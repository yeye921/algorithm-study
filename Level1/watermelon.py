# n이 홀수인 경우와 짝수인 경우로 나눔
def solution(n):
    if n%2==0:
        return "수박"*(n//2)  # 짝수인 경우도 //연산자 사용해야 오류안남, why?
    else:
        return "수박"*(n//2)+"수"


# 다른 풀이1
def solution(n):
    return "수박"*(n//2) + "수"*(n%2) 

# 다른 풀이2
def solution(n):
    s = "수박" * n
    return s[:n]
