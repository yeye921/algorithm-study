# 괄호가 열렸으면 반드시 닫혀야 함!
#  ")"가 나올 때 까지는 스택에 쌓고 "()"이 만나면 제거하는 방식 이용
# 배열에 원소가 없어야 올바른 괄호
# 내 풀이, 런타임 에러남 
def solution(s):
    a = []
    for i in range(len(s)):
        if s[0] == ")": return False
        elif s[i] == ")" and a[-1] == "(":
            del a[-1]
            pass
        else: a.append(s[i])
    return a == []

# 더 나은 풀이 1
def solution(s):
    st = []
    for c in s:
        if c == '(':
            st.append(c) # st에는 "("만 저장함

        if c == ')':
            try:
                st.pop()
            except IndexError:
                return False

    return len(st) == 0

# 2
def solution(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else: # c == ")" 라는 의미 
            if stack and stack.pop() == '(': # 스택이 비어있지 않고, 마지막원소가 "("이면 
                continue
            else: return False # 이 부분이 중요 
                               # 스택이 비어있거나, 마지막 원소가 ")"이면 false로 반환
    return len(stack) == 0
