# 내 풀이: max,min함수 활용
def solution(s):
    ans = ''
    s = list(map(int,s.split()))  # 공백으로 나눈 문자열 리스트 -> 정수 리스트 변환
    return str(min(s))+" "+str(max(s))

# 다른 풀이: sort함수 활용
def solution(s):
    s = s.split()
    a = [int(i) for i in s]
    a.sort()
    return str(a[0])+" "+str(a[-1])
    