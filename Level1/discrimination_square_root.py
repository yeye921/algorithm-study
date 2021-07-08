def solution(n):
    for i in range(1,int(n**0.5)+1):
        if i**2 == n:
            return (i+1)**2
    else:
        return -1


# 다른 풀이
# n에 루트를 씌운 수가 정수이면 제곱근임을 이용 
def solution(n):
    sqrt = n ** (1/2)
    if sqrt % 1 == 0:  # 1로 나눈 나머지가 0이면 정수라는 뜻 
        return (sqrt + 1) ** 2
    return -1


# 다른 풀이2
def solution(n):
    return n == int(n**.5)**2 and int(n**.5+1)**2 or -1
    # n이 제곱근이면 n+1의 제곱을 리턴, 아니면 -1을 리턴 
