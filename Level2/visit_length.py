# 좌표에서 방문가능한 좌표로 이동한다면, 간선을 set에 저장해두고, 겹치는 길이 있을 수 있으므로 set을 사용하고 len을 return 함
# 출발지점과 도착지점이 반대여도 같은 간선이므로 한번 저장할때 두 튜플로 저장하여 예외처리 해준다
def solution(dirs):
    command = {'U':(0, 1), 'D':(0, -1), 'L':(-1, 0), 'R':(1, 0)}
    road = set()
    cur_x, cur_y = (0,0)
    
    for d in dirs:
        next_x, next_y = cur_x + command[d][0], cur_y + command[d][1]
        if -5<= next_x <=5 and -5<= next_y <=5:
            road.add((cur_x, cur_y, next_x, next_y))
            road.add((next_x, next_y, cur_x, cur_y))
            cur_x, cur_y = next_x, next_y

    return len(road) // 2
            