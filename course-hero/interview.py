class Course:
    def __init__(self, department, course_number, year, semester):
        self.department = department
        self.course_number = course_number
        self.year = year
        self.semester = semester
    
    def __str__(self):
        return f'Department: {self.department}, Course Number: {self.course_number}, Year: {self.year}, Semester: {self.semester}'

def course_string_to_object(course_str):
    split_course_str_by_space = course_str.split(' ')
    # print(split_course_str_by_space)
    department, course = '', ''
    department_course_str, semester_year_str = '', ''
    for idx, x in enumerate(split_course_str_by_space):
        if idx == 0 and x[-1].isdigit():
            department_course_str = x
            semester_year_str = ' '.join(split_course_str_by_space[1:])
            break
        elif idx == 1 and x[-1].isdigit():
            department = split_course_str_by_space[0]
            course = x
            semester_year_str = ' '.join(split_course_str_by_space[2:])
    print('department', department)
    print('course', course)
    print('department_course_str', department_course_str)
    print('semester_year_str', semester_year_str)

if __name__ == '__main__':
    course_string_to_object('CS111 2016 Fall')