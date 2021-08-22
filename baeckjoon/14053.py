dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
def iswall(y,x):
    if 0 <= x < M and 0<= y < N:
        if home[y][x] == 1:
            return True
        else:
            return False
    return True

def clean(y,x,dir):
    global cnt
    home[y][x] = 2 # 청소하면 2
    cnt += 1

    while True: # 왼쪽탐색 존나하기
        result = 0
        # 내기준 왼쪽


        for k in range(0,4): #네면탐색
            rx = x + dx[k]
            ry = y + dy[k]
            if iswall(ry,rx)or home[ry][rx] == 2:
                result += 1


        if result == 4: # 네 면이 청소 되어있거나 벽일경우
            rx = x - dx[dir]
            ry = y - dy[dir]
            if iswall(ry, rx): # 후진해서도 벽이면
                return
            else:
                y, x = ry, rx
                continue

        temp_dir = (dir+3)% 4 #왼쪽
        ry = y + dy[temp_dir]
        rx = x + dx[temp_dir]

        if iswall(ry,rx) or home[ry][rx] == 2:
            dir = temp_dir
            continue

        if iswall(ry,rx) == False and home[ry][rx] == 0:
            clean(ry,rx,temp_dir)
            return


N, M = map(int,input().split())
r, c, d = map(int,input().split())
home = []
cnt = 0
for _ in range(N):
    home.append(list(map(int,input().split())))
clean(r,c,d)
print(cnt)