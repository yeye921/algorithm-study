# 최대한 많은 종류의 N/2마리 가져가기
# 리스트의 unique한 원소들의 개수를 세서 가져갈 수 있는 폰켓몬 수와 비교하여 처리 
 def solution(nums):
    num = len(nums) // 2
    type = len(list(set(nums)))
    if num > type:
        return type
    else:
        return num


# 최적화 코드 
def solution(nums):
    return min(len(nums)/2, len(set(nums)))  # 둘 중 작은 것을 반환   
