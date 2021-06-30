# 빈 배열일 경우와 아닌 경우로 나눔, remove()이용
def solution(arr):
    if len(arr)<=1:
        # 빈 배열일 경우
        return [-1]
    else:
        # 아닐 경우
        arr.remove(min(arr))
        return arr

# 최적화 코드
def solution(arr):
    return [i for i in arr if i > min(arr)]
