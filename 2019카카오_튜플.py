def solution(s):
    tmp = []
    for i in s[1:-1].split('},'):
        a = i
        a = a.replace('{','')
        a = a.replace('}','')
        tmp.append(list(map(int, a.split(','))))
    tmp.sort(key=lambda x:len(x))
    answer = []
    for i in tmp:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer
