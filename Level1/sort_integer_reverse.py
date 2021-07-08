# n의 각 자릿수를 큰 것 부터 작은 순으로 정렬
# 정수를 리스트로 변경 후, 내림차순으로 정렬한 다음 다시 정수로 변경
def solution(n):
    n = [str(i) for i in str(n) ] # 정수 -> (문자열)리스트
    n.sort(reverse=True) # 내림차순 정렬
    n = "".join(n)       # 리스트 -> 문자열 
    return int(n)        # 문자열 -> 정수 


# 다른 풀이
def solution(n):
    ls = list(str(n))       # 정수->문자열->리스트
    ls.sort(reverse=True)   # 리스트 정렬
    return int("".join(ls)) # 리스트->문자열->정수


# 다른 풀이2
# sorted하면 리스트로 변환해서 나옴 
def solution(n):
    return int("".join(sorted(list(str(n),reverse=True))
    
