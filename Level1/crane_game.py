''' moves의 원소를 열로 보고, 입력받은 열에서 가장 위에 있는 원소를
새 리스트에 append하고 같은 인형의 연속 체크하는 방식 이용'''


def solution(board, moves):
    answer = 0
    stack = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0: # i-1열의 가장 위에 있는 원소 찾음 
                stack.append(board[j][i-1])
                board[j][i-1] = 0 # 삭제대신 0대입
                break # 맨 위의 것 하나만 찾으면 되므로 건너뜀 
        
        # append하고 난 후, 연속해서 같은 인형있으면 pop함
        if len(stack)>1:
            if stack[-1] == stack[-2]: 
                answer += 2
                stack.pop()
                stack.pop()
                
    print(stack)       
    return answer
