# 용액 문제

import sys
def solution(liq):
    l=0
    r=len(liq)-1
    ans = [abs(liq[l]+liq[r]),(liq[l],liq[r])]
 
    while l<r:
        mix = liq[l]+liq[r]
        if abs(mix) < ans[0]:
            ans[0] = abs(mix)
            ans[1] = (liq[l],liq[r])
        if mix > 0:
            r-=1
        elif mix < 0:
            l += 1
        else:
            return ans[1]
    return ans[1]
 
if __name__== "__main__":
    n = map(int,sys.stdin.readline().split())
    liq = list(map(int,sys.stdin.readline().split()))
    ans = solution(liq)
    print("{} {}".format(ans[0],ans[1]))