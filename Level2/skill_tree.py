# 내 풀이
# 리스트에서 skill에 들어있는 것의 순서만 중요하므로 그것들만 따로 새 리스트로 만들어서 순서를 확인하는 방식 
def solution(skill, skill_trees):
    ans = 0
    arr = []
    skill = list(skill)
    for i in range(len(skill_trees)):
        arr.append([j for j in skill_trees[i] if j in skill])
    print(skill,arr)
    
    for i in range(len(arr)):
        cnt = 0
        for j in range(len(arr[i])):
            if arr[i][j] == skill[j]:  # arr의 순서가 skill의 순서와 일치해야 함 
                cnt += 1
        if len(arr[i]) == cnt: # 순서가 일치하는 개수가 arr[i]의 길이와 똑같아야 함
            ans+= 1
    return ans

# 더 나은 풀이1
def solution(skill,skill_trees):
    ans = 0
    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0): # 포인트!
                    break
        else:
            ans += 1
    
    return ans

# 2
def solution(skill,skill_trees):
    ans = 0
    for i in skill_trees:
        skill_list = ''
        for j in i:
            if j in skill:
                skill_list += j
        if skill_list == skill[0:len(skill_list)]:  # 포인트!
            ans += 1
    return ans


    
    
