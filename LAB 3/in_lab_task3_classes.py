# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 16:57:00 2023

@author: MINUSX
"""

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = []

    def add_marks(self, subject, mark):
        self.marks.append((subject, mark))

    def calculate_average(self):
        if not self.marks:
            return 0

        total_marks = sum(mark for subject, mark in self.marks)
        average = total_marks / len(self.marks)
        return average

# Create an instance of the Student class
student1 = Student("Bilal", 10)

# Add some marks
student1.add_marks("Math", 96)
student1.add_marks("Science", 85)
student1.add_marks("English", 88)

# Calculate and print the average marks

average_marks = student1.calculate_average()
print(f"Average marks for {student1.name} (Roll Number {student1.roll_number}): {average_marks:.2f}")
