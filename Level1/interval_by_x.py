def solution(x, n):
    answer = []
    for i in range(1,n+1): //range 처음과 끝 주의
        a = x * i
        answer.append(a)
    return answer

// 다른 풀이
def solution(x, n):
    return [i * x + x for i in range(n)]  //리스트 컴프리헨션 이용
    //return [i*x for i in range(1,n+1)]  // 이게 더 이해하기 쉬
