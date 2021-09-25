" " "
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

Sample Input 0

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
Sample Output 0

56.00
Explanation 0

Marks for Malika are  whose average is 

Sample Input 1

2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
Sample Output 1

26.50
" " "

# code
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    
    
    query_scores=student_marks[query_name]
    print('{0:.2f}'.format(sum(query_scores)/len(query_scores)))