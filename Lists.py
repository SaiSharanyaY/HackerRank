" " " 
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
  
  Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
" " "


# code:

if __name__ == '__main__':
    N = int(raw_input())
    lis=[]
    
    for i in range(N):
        cmd = raw_input().split()
        if cmd[0] == 'insert':
            lis.insert(int(cmd[1]),int(cmd[2]))
        elif cmd[0] == 'append':
            lis.append(int(cmd[1]))
        elif cmd[0] == 'print':
            print(lis)
        elif cmd[0] == 'remove':
            lis.remove(int(cmd[1]))
        elif cmd[0] == 'sort':
            lis.sort()
        elif cmd[0] == 'pop':
            lis.pop()
        elif cmd[0] == 'reverse':
            lis.reverse()
        else:
            print("Invalid Input")
