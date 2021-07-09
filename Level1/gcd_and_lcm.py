# 최대공약수 -> 유클리드 호제법 이용
# 최소공배수 -> 두 자연수의 곱/ 최대공약
def gcd(n1, n2):
    if n1 < n2:
        (n1, n2) = (n2, n1)

    while n2 != 0:
        (n1, n2) = (n2, n1 % n2)

    return n1


def solution(n, m):
    return [gcd(n, m), (n * m) / gcd(n,m)]
