import datetime
import re

class Course:
    def __init__(self, department, course_number, year, semester):
        self.department = department
        self.course_number = course_number
        self.year = year
        self.semester = semester
    
    def __str__(self):
        return f'Department: {self.department}, Course Number: {self.course_number}, Year: {self.year}, Semester: {self.semester}'

SEMESTER = {
    'f': 'Fall',
    'w': 'Winter',
    's': 'Spring',
    'su': 'Summer'
}

def course_string_to_object_step_by_step(course_str):
    
    department_course_str, semester_year_str = '', ''
    split_course_str_by_space = course_str.split(' ')
    for idx, x in enumerate(split_course_str_by_space):
        if x[-1].isdigit():
            department_course_str = ' '.join(split_course_str_by_space[0:idx + 1])
            semester_year_str = ' '.join(split_course_str_by_space[idx + 1:])
            break
    
    department, course = '', ''
    split_department_course_str = re.split('-| |:', department_course_str)
    if len(split_department_course_str) > 1:
        department = split_department_course_str[0]
        course = split_department_course_str[1]
    else:
        department = department_course_str.rstrip('0123456789')
        course = department_course_str[len(department):]

    semester, year = '', ''
    split_semester_year_str = semester_year_str.split(' ')
    if (len(split_semester_year_str) > 1):
        if split_semester_year_str[0].isdigit():
            year = split_semester_year_str[0]
            semester = split_semester_year_str[1]
        else:
            semester = split_semester_year_str[0]
            year = split_semester_year_str[1]
    else:
        if semester_year_str[0].isdigit():
            semester = semester_year_str.strip('0123456789')
            year  = semester_year_str[len(semester):]
        else:
            semester = semester_year_str.rstrip('0123456789')
            year  = semester_year_str[len(semester):]
    
    if len(year) == 2:
        year = datetime.datetime.strptime(year,'%y').strftime('%Y')
    
    if len(semester) <= 2:
        semester = SEMESTER[semester.lower()]
    else:
        semester = semester.capitalize()

    course = Course(department, course, year, semester)
    print(course)


if __name__ == '__main__':
    course_string_to_object_step_by_step('CS:111 16 fall')
    course_string_to_object_step_by_step('CS-111 Fall 2016')
    course_string_to_object_step_by_step('CS111 F2016')