def solution(park, routes):
    answer = []
    s = [ [i,j] for j in range(len(park[0])) for i in range(len(park)) if park[i][j] == 'S']
    i,j,w,h = s[0][0],s[0][1] , len(park[0]),len(park)
    for route in routes:
        tmp = int(route[2])
        copy_i,copy_j = i,j
        if route[0] == 'E':
            for _ in range(tmp):
                if j + 1 < w and park[i][j+1] != 'X':
                    j += 1
                else:
                    j = copy_j
                    break
        if route[0] == 'W':
            for _ in range(tmp):
                if j - 1 >= 0 and park[i][j-1] != 'X':
                    j -= 1
                else:
                    j = copy_j
                    break
        if route[0] == 'N':
            for _ in range(tmp):
                if i - 1 >= 0 and park[i-1][j] != 'X':
                    i -= 1
                else:
                    i = copy_i
                    break
        if route[0] == 'S':
            for _ in range(tmp):
                if i + 1 < h and park[i+1][j] != 'X':
                    i += 1
                else:
                    i = copy_i
                    break
    return [i,j]