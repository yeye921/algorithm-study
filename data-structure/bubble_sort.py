''' 전체 데이터 중 가장 값이 큰 데이터를 맨 뒤로 보낸 후, 이미 정렬된 값을 제외한 데이터 중 
가장 큰 데이터를 맨뒤로 보내는 방식 => 데이터가 오름차순으로 정렬됨 '''
# 시간복잡도 O(n^2)

arr = [5,7,9,0,3,1,6,2,4,8]

def bubble_sort(arr):
    l = len(arr)
    for i in range(l-1):        # 반복 횟수에 따라 탐색 범위가 달라짐
        for j in range(l-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

print(bubble_sort(arr))
