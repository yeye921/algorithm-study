# 맞은 풀이 
# 연속적으로 나타나는 숫자는 하나만 남기고 제거
# 연속적일경우 1, 아닐경우 0을 새로운 배열에 담고, 0인 원소를 정답배열에 추가 
def solution(arr):
    dup = []
    # arr2 = arr
    arr2 = []
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            dup.append(1)
        else:
            dup.append(0)
    dup.append(0)
    
    for i in range(len(dup)):
        if dup[i] == 0:
            arr2.append(arr[i])
            
    return arr2


# 틀린 풀이
# 연속적일경우 1, 아닐경우 0을 새로운 배열에 담고, 1인 원소는 원래배열에서 제거
# remove를 이용하면 자꾸 list out of index 에러 남 
arr = [1,1,3,3,0,1,1]
dup = [1,0,1,0,0,1,0]
arr2 = arr
for i in range(len(dup)):
    if dup[i] == 1:
        del arr2[i] # arr을 이용하면 remove로 인해 배열이 변하므로 새 배열 생성 
        # arr2.remove(arr[i]) 이것도 오류남 
print(arr2)


# 다른 풀이
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue # 리스트a의 마지막 원소가 s랑 다르면 추가         a.append(i)
        a.append(i)
    return a

# 다른 풀이 2
def no_continuous(s):
    return [s[i] for i in range(len(s)) if s[i]!= s[i+1:i+2]]
