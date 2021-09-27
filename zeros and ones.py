# code:

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

i = raw_input().split()


print(np.zeros((int(i[0]),int(i[1]),int(i[2])), dtype=np.int))
print(np.ones((int(i[0]),int(i[1]),int(i[2])), dtype=np.int))
