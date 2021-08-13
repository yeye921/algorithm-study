input_num = int(input()) 
numbers = list(map(int, input().split())) 
numbers.sort() 
input_num2 = int(input()) 
numbers2 = list(map(int, input().split()))

# 이분 탐색
for num in numbers2: 
    left, right = 0, 
    len(numbers) - 1 
    is_find = False

    while True: 
        median = (left + right) // 2 
        if num == numbers[median]: 
            print(1) 
            is_find = True 
            break 
        elif num > numbers[median]: 
            left = median + 1 
        elif num < numbers[median]: 
            right = median - 1 
            if left > right: 
                break 
            
    if not is_find: 
        print(0)
