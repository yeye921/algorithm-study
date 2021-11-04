# 삼각형 분류 문제

t = int(input())
for i in range(t):
    li = list(map(int, input().split()))
    li.sort()
    if li[0] + li[1] <= li[2]:
        print(f"Case #{i+1}: invalid!") # 삼각형이 만들어지지 않을 경우
    else:
        if li[0] == li[1] == li[2]:
            print(f"Case #{i+1}: 정삼각형")
        elif li[0] == li[1] or li[1] == li[2] or li[0] == li[2]:
            print(f"Case #{i+1}: 이등변삼각형")
        elif li[0] != li[1] != li[2]:
            print(f"Case #{i+1}: 부등변삼각형")