    
def find__average_marks(marks):
    sum_marks=sum(marks)
    print('The sum is ',sum_marks)
    
    length=len(marks)
    
    average_marks=sum_marks/length
    
    return average_marks


def compute_grades(average_marks):
    
    if average_marks>=80:
        grade='A'
        
    elif average_marks<80 and average_marks>=60:
        grade='B'
        
    elif average_marks<60 and average_marks>=50:
        grade='C'
        
    else:
        grade='D'
    return grade
        
marks=[60,80,90,100]  
average_marks=find__average_marks(marks)     
print('The average marks is',average_marks) 

grade=compute_grades(average_marks)
print("Your grade is",grade)
