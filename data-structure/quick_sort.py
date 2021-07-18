# 피벗을 설정한 다음 큰 수와 작은 수를 교환한 후, 리스트를 반으로 나누는 방식
# 평균 시간 복잡도: O(NlogN), 최악의 경우: O(N^2)


# 전통 퀵 정렬 분할 방식 
arr = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(arr, start, end):
    if start >= end:  # 원소 1개인 경우 종료 
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right: # 엇갈릴 때 까지 반복
        # 피벗보다 큰 데이터를 찾을 때 까지 반복
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때 까지 반복
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은데이터와 피벗을 교체
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:   # 엇갈리지 않았다면 작은데이터와 큰데이터를 교체
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort(arr,start,right - 1)
    quick_sort(arr,right + 1, end)


quick_sort(arr,0,len(arr)-1)
print(arr)


# 파이썬의 장점을 살린 퀵 정렬
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗은 첫번째 원소
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분 
    right_side = [x for x in tail if x > pivot]   # 분할된 오른쪽 부분

    return quick_sort(left_side) + [pivot] + quick_sort[right_side]

print(quick_sort(array))
    
    
