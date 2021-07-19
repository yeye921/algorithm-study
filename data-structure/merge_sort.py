# 일단 반으로 나누고 합쳐서 정렬
# n/2로 나누고, 1개의 요소가 남기까지 재귀적으로 divide한다
# 그 후, 그 다음에 2개씩 요소들을 반복적으로 merge한다 

def divide(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    left_list = list[:mid]
    right_list = list[mid:]
    left_list = merge(left_list)
    right_list = merge(right_list)
    return merge(left_list,right_list)

def merge(left,right):
    arr = []
    while len(left)>0 or len(right)>0:
        if len(left)>0 and len(right)>0:
            if left[0] <= right[0]:
                arr.append(left[0])
                left = left[1:]
            else:
                arr.append(right[0])
                right  = right[1:]
        elif len(left) > 0:
            arr.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            arr.append(right[0])
            right = right[1:]
    return arr 
