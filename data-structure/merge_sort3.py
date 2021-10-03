import random
data_list = random.sample(range(100),10)

def mergesplit(data_list):
    if len(data_list) <= 1:
        return data_list
    medium = len(data_list) // 2
    left = mergesplit(data_list[:medium])
    right = mergesplit(data_list[medium:])
    return merge(left,right)


def merge(left,right):
    merged = list()
    left_point,right_point = 0,0

    # case1 - left, right 둘 다 있을 경우
    while len(left) > left_point and right[right_point]:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1

    # case2 - left 데이터가 없을 때
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1

    # case3 - right 데이터가 없을 때
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1

    return merged

mergesplit(data_list)
