import datetime
import re

SEMESTER = {
    'f': 'Fall',
    'w': 'Winter',
    's': 'Spring',
    'su': 'Summer'
}

class Course:
    def __init__(self, department, course_number, year, semester):
        self.department = department
        self.course_number = course_number
        self.year = year
        if len(year) == 2:
            self.year = datetime.datetime.strptime(year,'%y').strftime('%Y')
    
        if len(semester) <= 2:
            self.semester = SEMESTER[semester.lower()]
        else:
            self.semester = semester.capitalize()
    
    def __str__(self):
        return f'Department: {self.department}, Course Number: {self.course_number}, Year: {self.year}, Semester: {self.semester}'

def course_string_to_object_step_by_step(course_str):
    
    department_course_number_str, semester_year_str = '', ''
    split_course_str_by_space = course_str.split(' ')
    if len(split_course_str_by_space) == 1:
        return None
    
    for idx, x in enumerate(split_course_str_by_space):
        if x[-1].isdigit():
            department_course_number_str = ' '.join(split_course_str_by_space[0:idx + 1])
            semester_year_str = ' '.join(split_course_str_by_space[idx + 1:])
            break
    
    department, course_number = '', ''
    split_department_course_number_str = re.split('-| |:', department_course_number_str)
    if len(split_department_course_number_str) > 1:
        department = split_department_course_number_str[0]
        course_number = split_department_course_number_str[1]
    else:
        department = department_course_number_str.rstrip('0123456789')
        course_number = department_course_number_str[len(department):]

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
            year  = semester_year_str[0:len(semester_year_str) - len(semester)]
        else:
            semester = semester_year_str.rstrip('0123456789')
            year  = semester_year_str[len(semester):]

    return Course(department, course_number, year, semester)

def course_string_to_object_with_regex(course_str):
    department, course_number, year, semester = '', '', '', ''
    match = re.findall(r'([a-zA-Z]+)[-| |:]?(\d+) ([a-zA-Z]{1,4}) ?([0-9]{2,4})', course_str)
    if len(match) > 0:
        department, course_number, semester, year = match[0]
    else:
        match = re.findall(r'([a-zA-Z]+)[-| |:]?(\d+) ([0-9]{2,4}) ?([a-zA-Z]{1,4})', course_str)
        if len(match) > 0:
            department, course_number, year, semester = match[0]
        else:
            return None

    return Course(department, course_number, year, semester)


if __name__ == '__main__':
    print(course_string_to_object_step_by_step('CS:111 16fall'))
    print(course_string_to_object_step_by_step('CS-111 Fall 2016'))
    print(course_string_to_object_step_by_step('CS111 F2016'))
    print(course_string_to_object_with_regex('CS:111 16fall'))
    print(course_string_to_object_with_regex('CS-111 Fall 2016'))
    print(course_string_to_object_with_regex('CS111 F2016'))