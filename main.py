import numpy as np


a = [1,2,3,4]
a.append([1,2,3])
a += [[1,2],[2,3]]
b = [1,2,3,4]
b.extend([1,2,3])
b.extend([[1,2],[2,3]])
print(a,b)