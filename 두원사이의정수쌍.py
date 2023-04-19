def solution(r1, r2):
    answer = 0
    import math
    for i in range(r1):
        y2 = math.floor(math.sqrt(r2**2 - i**2))  # 얘는 floor
        y1 = math.ceil(math.sqrt(r1**2 - i**2)) # 얘는 ceil
        if y2 == y1:
            answer += 1
        else:
            answer += y2 - y1 + 1
    for i in range(r1, r2):
        y2 = math.floor(math.sqrt(r2**2 - i**2))
        answer += y2
        print(y2)
    return 4*answer


import math

r1, r2 = 999999, 1000000
print(solution(r1, r2))
