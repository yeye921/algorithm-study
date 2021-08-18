# DP를 이용한 문제
# 완전탐색(Brute-force)로 풀 경우, 시간 복잡도 O(n^3)으로 시간초과
# 왼쪽 위부터 배열의 인덱스를 업데이트 해가면서 이를 이용하여 최대 크기의 정사각형을 찾는 방식
# 0이 아닌 인덱스의 값을 왼쪽,왼쪽 위, 위의 세 곳을 확인하여 값이 가장 낮은 인덱스의 값보다 1크게 업데이트 해줌
def findLargestSquare(board):
    answer = 1
    res = [[1 if x=='O' else 0 for x in y] for y in board]
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 'O':
                res[y][x] = min(res[y-1][x], res[y-1][x-1], res[y][x-1]) + 1
                if res[y][x] > answer: answer = res[y][x]

    return answer ** 2