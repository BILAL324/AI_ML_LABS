
"""
Created on Thu Oct  5 15:33:26 2023

@author: MINUSX

"""

def calculate_gpa(students):
    
#created a list to append data in result
    results= []
    
    for student in students:
        name = student['name']
        marks = student['marks']
        total_marks = sum(marks)
        percentage = total_marks/len(marks)
        
        if percentage >=85:
            grade = 'A'
            grade_points = 4.00
            
        elif percentage >= 80:
            grade = 'A-'
            grade_points = 3.66
            
        elif percentage >= 75:
            grade = 'B+'
            grade_points = 3.33
            
        elif percentage >= 71:
            grade = 'B'
            grade_points = 3.00
            
        elif percentage >= 68:
            grade = 'B-'
            grade_points = 2.66
            
        elif percentage >= 64:
            grade = 'C+'
            grade_points = 2.33
            
        elif percentage >= 61:
            grade = 'C'
            grade_points = 2.00
            
        elif percentage >= 58:
            grade = 'C-'
            grade_points = 1.66
            
        elif percentage >= 54:
            grade = 'D+'
            grade_points = 1.30
            
        elif percentage >= 50:
            grade = 'D'
            grade_points = 1.00
            
        else:
            grade = 'F'
            grade_points = 0.00
            
        
        results.append({
            'name': name,
            'grade': [grade ],
            'grade_points': [grade_points for _ in marks],
            'gpa': round(grade_points, 2)
        })
        
    return results


students_data = [
    {'name': 'bilal', 'marks': [78, 85, 92, 69, 77]},
    {'name': 'abdullah', 'marks': [90, 88, 75, 81, 95]},
    {'name': 'zain', 'marks': [63, 76, 58, 70, 72]},
    {'name': 'umar', 'marks': [48, 53, 60, 42, 55]},
    {'name': 'ali', 'marks': [76, 79, 81, 82, 77]}
                ]



# Calculate GPA for each student
gpa_results = calculate_gpa(students_data)

# Print the results
for result in gpa_results:
    print(result)



























