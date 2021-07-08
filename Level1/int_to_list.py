# 자연수 -> 문자열 -> 리스트로 바꾼 다음 뒤집고 문자열 -> 정수->리스트로 변환
# n을 뒤집음 -> reverse 함수 이용
def solution(n):
    n = [int(i) for i in str(n)].reverse()
    return n


# 최적화 코드
def solution(n):
    return [int(i) for i in str(n)][::1] # 처음부터 끝까지 역순으로 
    

# 다른 풀이
def solution(n):
    return list(map(int,reversed(str(n))))
