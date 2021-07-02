# a,b중 작은 수 구해서, 그 수를 1씩 증가시키면서 더하는 방식
def solution(a, b):
    result = 0
    if a>b:
        x = b
    else:
        x = a
    for _ in range(abs(a-b)+1): # 단순 횟수 반복
        result += x
        x += 1
    return result


# 다른 풀이
def solution(a,b):
    if a > b: a, b = b, a
    return sum(range(a,b+1))

# 최적화 코드(시간복잡도:O(1))
def solution(a,b):
    return (abs(a-b)+1)*(a+b)//2   # 수열 공식
