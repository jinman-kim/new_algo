self_ = []
for i in range(1,10000):
    tmp = i
    for j in str(i):
        tmp += int(j)
    self_.append(tmp)
answer = set(list(range(1,10001))) - set(self_)
for i in sorted(list(answer)):
    print(i)