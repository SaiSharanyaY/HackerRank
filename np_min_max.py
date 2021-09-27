# code:

import numpy as np

n,m = list(input().split())

a = np.array([input().split() for _ in range(int(n[0]))], int)



print (np.max(np.min(a, axis=1)))

