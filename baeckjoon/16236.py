# 아기 상어 문제

from collections import deque

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

sx, sy = 0, 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            arr[i][j] = 0
            sx, sy = i, j
            break
size = 2
move_num = 0
eat = 0
while True:
    q = deque()
    q.append((sx, sy, 0))
    visited = [[False] * n for _ in range(n)]
    flag = 1e9
    fish = []
    while q:
        x, y, count = q.popleft()

        if count > flag:
            break
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if arr[nx][ny] > size or visited[nx][ny]:
                continue

            if arr[nx][ny] != 0 and arr[nx][ny] < size:
                fish.append((nx, ny, count + 1))
                flag = count
            visited[nx][ny] = True
            q.append((nx, ny, count + 1))

    if len(fish) > 0:
        fish.sort()
        x, y, move = fish[0][0], fish[0][1], fish[0][2]
        move_num += move
        eat += 1
        arr[x][y] = 0
        if eat == size:
            size += 1
            eat = 0
        sx, sy = x, y
    else:
        break

print(move_num)