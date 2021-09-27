# code

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
n,m = map(int, raw_input().split())

arr=np.array([raw_input().split() for _ in range(n)], int)
print(np.prod(np.sum(arr, axis=0)))
