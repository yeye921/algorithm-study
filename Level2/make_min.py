# 땅따먹기 문제와 유사 (그 문제는 덧셈이지만, 이 문제는 곱해서 더하는 문제)
# 누적된 값이 최소가 되도록 만드는 것이 목표(그리디x)
# A의 가장 작은 값과 B의 가장 큰 값을 순서대로 곱해서 더하는 형태
def solution(A,B):
    answer = 0
    A = sorted(A)
    B = sorted(B, reverse=True)

    answer = sum([a * b for a, b in zip(A, B)])
    return answer

# 더 나은 풀이
def getMinSum(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))