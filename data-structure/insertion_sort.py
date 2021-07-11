# 데이터를 하나씩 확인하며 각 데이터를 적절한 위치에 삽입하는 알고리즘 
# 데이터가 거의 정렬되어 있을 때 매우 빠르게 동작

def insertion_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):  # i~1까지 감소하며 반복 
            if arr[j] < arr[j-1]: # 한 칸씩 왼쪽으로 이동 
                arr[j],arr[j-1] = arr[j-1], arr[j]
            else:        # 자신보다 작은 데이터를 만나면 그 위치에서 멈춤 
                break


array = [7,5,9,0,3,1,6,2,4,8]
insertion_sort(array)
print(array)
