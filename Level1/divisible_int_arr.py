# 나누어 떨어지는 -> %연산자 이용, 나누어 떨어질 경우, 새로운 배열에 삽입 후 정렬
def solution(arr, divisor):
    result = []
    for i in arr:
        if i % divisor == 0:
            result.append(i)
    if len(result)==0:
        result.append(-1)
    else:
        result.sort()
    return result


# 다른 풀이 - 리스트 컴프리핸션 이용
def solution(arr, divisor):
    result = [i for i in arr if i%divisor==0]
    if len(result) ==0:
        result.append(-1)
    else:
        result.sort()
    return result


# 다른 풀이 2
def solution(arr, divisor):
    result = [i for i in arr if i%divisor==0]
    if len(result) ==0:
        return [-1]
    else:
        return sorted(result)  # result.sort()일 경우 null을 반환!

# 최적화 코드(or 이용)
# 리스트에 값이 있으면 True이고 없으면 False인 것을 이용
def solution(arr,divisor):
    return sorted([i for i in arr if n%divisor == 0]) or [-1]




