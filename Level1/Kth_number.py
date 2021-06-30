# commands 어떻게 처리하는 지가 관건
#  2차원 배열의 반복문 처리(한 행씩 처리)
# list의 n번째 => list[n-1] 
def solution(array, commands):
  answer = []
  for i in range(len(commands)):
        arr_list = array[commands[i][0]-1:commands[i][1]]
        arr_list.sort()
        answer.append(arr_list[commands[i][2]-1])
  return answer

# 다른풀이(map,람다함수 공부하기)
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

# i,j,k 한번에 입력할 수도 있음 
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer
