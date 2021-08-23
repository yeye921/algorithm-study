# 문자열 재정렬 문제
data = input()
arr = []
val = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳일 경우 결과 리스트에 삽입
    if x.isalpha():
        arr.append(x)
    # 숫자는 따로 더하기
    else:
        val += int(x)

# 알파벳을 오름차순으로 정렬
arr.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if val != 0:
    arr.append(str(val))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print("".join(arr))