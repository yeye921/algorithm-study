# 요소 하나하나씩 탐방하며 더함 => 2중 for문 이용
def solution(arr1, arr2):
    n = len(arr1) 
    m = len(arr1[0])
    result = []
    for i in range(n):
        answer = []         # 초기화(중요)
        for j in range(m):
            answer.append(arr1[i][j]+arr2[i][j])
        result.append(answer)
            
    return result

# 다른 풀이
def solution(arr1,arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]

    return arr1

# 최적화 코드  
def solution(A,B):
    answer = [[c + d for c,d in zip(a,b)] for a,b in zip(A,B)]
    return answer
