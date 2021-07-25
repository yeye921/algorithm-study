def heap_sort(arr):
    # 최대 힙 만들기 
    for i in range(1,len(arr)):
        c = i
        while c != 0:  # 한번 if문이 수행될 때 마다 그것의 부모를 다 조사 
            root = (c - 1) // 2
            if arr[root] < arr[c]:
                arr[root],arr[c] = arr[c], arr[root]
            
            c = root  # c는 현재 루트노드를 나타냄
    
    # 크기를 줄여가며 반복적으로 힙 구성 
    for j  in range(len(arr)-1,-1,-1):
        arr[0],arr[j] = arr[j], arr[0]  # 맨 앞의 원소와 맨 뒤의 원소를 바꿈
        root = 0
        c = 1

        while c < j:  # 맨 뒤 원소는 정렬됬다고 생각하고, 제외한 나머지에 heapify수행
            c = 2 * root + 1 # c는 왼쪽 자식 노드 
            # 바뀐 것으로 다시 heapify 수행  
            if c < j-1 and arr[c] < arr[c+1]: # 둘 중 더 큰 것의 인덱스를 c로 취함 
                c += 1
            if c < j and arr[root] < arr[c]: # 부모노드와 자식노드를 비교 
                arr[root], arr[c] = arr[c], arr[root] 
            
            root = c  # 현재 자식 노드를 뜻함

b = [5,2,3,9,6,1,8,4,7]
heap_sort(b)
# 결과 >> [1,2,3,4,5,6,7,8,9]
print(b)