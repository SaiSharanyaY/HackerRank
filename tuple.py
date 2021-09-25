" " " 
Task
Given an integer, n, and  space-separated integers as input, create a tuple, , of those n  integers. Then compute and print the result of .

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

Input Format

The first line contains an integer,n , denoting the number of elements in the tuple.
The second line contains n space-separated integers describing the elements in tuple .

Output Format

Print the result of hash(t)
" " "

# code : 
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
    for i in range(n):
        integer_list[i] = int(integer_list[i])
    
    
    print(hash(tuple(integer_list)))
