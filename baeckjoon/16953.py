# A -> B 문제

# 풀이 - 1
a, b = map(int, input().split()) 
que = [(a, 1)] 
result = -1 
while que: 
    x, cnt = que.pop(0) 
    if x == b: 
        result = cnt 
        break 
    
    if x*2 <= b: 
        que.append((x*2, cnt+1)) 
    
    if int(str(x)+'1') <= b:
         que.append((int(str(x)+'1'), cnt+1)) 

print(result)

# 풀이 - 2
a, b = map(int, input().split()) 
que = [(b, 1)] 
result = -1 
while que: 
    x, cnt = que.pop(0) 
    if x == a: result = cnt 
    break 
    
    if x%2 == 0 and x/2>=a: 
        que.append((x/2, cnt+1)) 
    
    elif x%10 == 1 and int(x/10) >= a: 
        que.append((int(x/10), cnt+1)) 
    else: 
        break 

print(result)