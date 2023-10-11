'''Implement a function called sort_students that takes a list of students objects as input and sorts the list based on their CGPA(Cumulative Grade Point Average) in descending order.Each student object has the following attributes:name(string),roll_number(string),and cpga(float).Test the function with different input lists of students.'''
def CgpaCalc(marks, n):
  grade = [0] * n
Sum = 0
for i in range(n):
       grade[i] = (marks[i] / 10)
for i in range(n):
       Sum += grade[i]
  cgpa = Sum / n
return cgpa

n = 5
marks = [ 90, 80, 70, 80, 90 ]
 
cgpa = CgpaCalc(marks, n)
       
print("CGPA = ", '%.1f' % cgpa)
print("CGPA Percentage = ", '%.2f' % (cgpa * 9.5))
