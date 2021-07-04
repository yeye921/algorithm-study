# a[0]*b[0]+ .... + a[n-1]*b[n-1] 공식이용 
def solution(a, b):
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result


# 다른 풀이
def solution(a,b):
    c = []
    for i in range(len(a)):
        c.append(a[i]*b[i])
    return sum(c)


# 최적화 코드
# 리스트 컴프리핸션 & zip함수 이용 
def solution(a,b):
    return sum([x*y for x,y in zip(a,b)])
