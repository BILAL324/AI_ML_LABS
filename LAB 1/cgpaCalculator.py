import numpy

Cgpa = input('Enter present CGPA:')
creditHour =input('Enter present Credit hours:')
TotalCH = input('Enter complete credit hours:')
RquiredCgpa = input('Enter required CGPA:')

cur_CGPA = float(Cgpa)
cur_cre_hr =int(creditHour)
comp_cre_hr = int(TotalCH)
req_CGPA= float(RquiredCgpa)

t_points = cur_CGPA * comp_cre_hr
t_credit =comp_cre_hr + cur_cre_hr
cur_points = req_CGPA * t_credit
points_for_reqcgpa = cur_points - t_points
needed_gpa = points_for_reqcgpa/ cur_cre_hr

if needed_gpa >= 4:
    print(needed_gpa)
else:
    print('Enter the correct gpa')