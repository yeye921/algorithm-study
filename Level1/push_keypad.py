# 2,5,8,0 원소와 마지막 오른손 위치 간 키패드 상의 거리  = d_r
# 2,5,8,0 원소와 마지막 왼손 위치 간 키패드 상의 거리 = d_l
# d1,d2를 비교하여 가까운 거리를 구하면 해결할 수 있다 

def solution(numbers, hand):
    ans = ''
    tmp_l = '*'
    tmp_r = '#'
    
    for i in numbers:
        if i in [1,4,7]:
            tmp_l = i   # 왼손의 위치 저장
            ans += 'L'  
        elif i in [3,6,9]:
            tmp_r = i   # 오른손의 위치 저장
            ans += 'R'
        elif i in [2,5,8,0]:
            if distance(tmp_r,i) > distance(tmp_l,i): # 왼손의 위치가 더 가까울 경우
                tmp_l = i
                ans += 'L'
            elif distance(tmp_r,i) < distance(tmp_l,i): # 오른손의 위치가 더 가까울 경우
                tmp_r = i
                ans += 'R'
            else:
                if hand == 'right':
                    tmp_r = i
                    ans += 'R'
                else:
                    tmp_l = i
                    ans += 'L'
    return ans    
     
# 거리 구하기 => 2차원 배열 원소로 변환해서 구함
def distance(tmp,i):
    location = { '1':(0,0), '2':(0,1), '3':(0,2),
                '4':(1,0), '5':(1,1), '6':(1,2),
                '7':(2,0), '8':(2,1), '9':(2,2),
                '*':(3,0), '0':(3,1), '#':(3,2) }
    tmp = str(tmp)
    i = str(i)
    x_t, y_t = location[tmp]
    x_i, y_i = location[i]
    return abs(x_t - x_i)+abs(y_t - y_i)

    






# 다른 풀이
def solution(numbers, hand):
    answer = ''
    
    # 인덱스: 키패드 숫자, 튜플 값: 키패드 숫자의 2차원 배열에서 위치 (포인트)
    board = [(0, 1), (3, 0), (3, 1), (3, 2), (2, 0), (2, 1), (2, 2), (1, 0), (1, 1), (1, 2)]
    left = (0, 0)
    right = (0, 2)
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left = board[number]

        elif number in [3, 6, 9]:
            answer += 'R'
            right = board[number]

        else:
            d_r = abs(board[number][0] - right[0]) + abs(board[number][1] - right[1])
            d_l = abs(board[number][0] - left[0]) + abs(board[number][1] - left[1])
            if d_r > d_l:
                answer += 'L'
                left = board[number]
            elif d_r < d_l:
                answer += 'R'
                right = board[number]
            else:
                if hand == 'right':
                    answer += 'R'
                    right = board[number]
                else:
                    answer += 'L'
                    left = board[number]
                
    return answer

            
