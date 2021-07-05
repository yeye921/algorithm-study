# nums 중 3개뽑음 => 조합이용
# 소수판단(1과 자기자신외에는 나누어 떨어지는 수 없음) => 2중 for문 이용
from itertools import combinations
def solution(nums):
    arr = list(combinations(nums,3))
    result = []
    for i in arr:
        result.append(sum(i))
    answer = 0
    
    for i in result:
        cnt = 0
        for j in range(1,i+1):
            if i % j ==0:
                cnt += 1
        if cnt == 2:
            answer += 1
    return answer
        

# 다른 풀이
from itertools import combinations as cb
def solution(nums):
    answer = 0
    for i in cb(nums,3):
        cand = sum(i)
        for j in range(2,cand):  # 1과 자기자신을 제외한 수(2 ~ N-1)에서 나누어 떨어지는지 체크  
            if cand % j==0:
                break
        else:
            answer += 1  # else문의 위치 

    return answer


# 최적화 코드 (에라토스테네스의 체 이용)
from itertools import combinations
def solution(nums):
    answer = 0
    for i in combinations(nums,3):
        cand = sum(i)
        for j in range(2,cand**0.5+1): # 2부터 자기자신의 제곱근 까지 체크 
            if cand % j==0:
                break
        else:
            answer += 1

    return answer
