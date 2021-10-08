# 틱! 택! 토! 문제

player = int(input())
coordinates = [list(map(int, input().split())) for _ in range(9)]
B = [[0] * 4 for _ in range(4)]
result = 0

for coord in coordinates:
    B[coord[0]][coord[1]] = player
    for n in range(1, 4):
        if B[n][1] == B[n][2] == B[n][3] > 0 or B[1][n] == B[2][n] == B[3][n] > 0:
            result = player
            break
    if B[1][1] == B[2][2] == B[3][3] > 0 or B[1][3] == B[2][2] == B[3][1] > 0:
        result = player
        break
    if result != 0:
        break
    if player == 1:
        player = 2
    else:
        player = 1

print(result)