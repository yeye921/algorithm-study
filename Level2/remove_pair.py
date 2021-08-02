# stack을 이용해서 맞는 쌍이 나오면 pop하는 방식
def solution(s): 
    stack = []
    for i in s:
        if len(stack) == 0: stack.append(i)
        elif stack[-1] == i: stack.pop()
        else: stack.append(i)
    if len(stack) == 0: return 1
    else: return 0 


# 틀린 풀이(참고)
# 정답은 맞으나 효율성에서 실패 
# 한 쌍의 문자열이 나오면, s에서 제거하고 제거전의 위치부터 시작
# (삭제하고 정렬하는 시간이 있기때문에 시간에서 오래 걸림)
def solution(s):
    start = 0
    while start < len(s) - 1: 
        if s[start] == s[start+1]: s = s[0:start] + s[start+2:]; start = max(0, start-1) # 포인트
        else: start += 1

    if len(s) == 0: return 1
    else: return 0