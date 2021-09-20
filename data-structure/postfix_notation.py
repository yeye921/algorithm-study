# 후위표기식 

# 연산자의 우선순위에 따라 스택에 연산자를 push/pop한다
# 1. '(': 나오면 바로 스택에 push한다.
# 2. ')': 우선순위가 가장 높은 괄호연산자가 끝난다는 뜻이므로, 괄호 안에 남아있는 연산자를 전부 pop하고 '('도 pop해줌. ')'는 처음부터 스택에 넣지 않는다.
# 3. '', '/': 스택에 '', '/'가 있다면 그것들을 먼저 없어질 때까지 pop해주고 끝나면 push한다. ('+','-'은 우선순위가 낮으므로 pop안함)
# 4. '+', '-': 스택에 다른 사칙연산자가 있다면 그것들을 먼저 없어질 때까지 (괄호연산자 직전가지)pop해주고 끝나면 push한다.

a=input()
stack=[]
res=''
for x in a:
    if x.isdecimal():
        res+=x
    else:
        if x=='(':
            stack.append(x)
        elif x=='*' or x=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                res+=stack.pop()
            stack.append(x)
        elif x=='+' or x=='-':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.append(x)
        elif x==')':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.pop()
while stack:
    res+=stack.pop()
print(res)