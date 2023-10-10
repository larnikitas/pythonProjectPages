import pandas as pd
from datetime import datetime
import random  # To generate random grades

class Student:
    def __init__(self, id, fname, lname, dateBirth, height,weight, gender):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.dateBirth = dateBirth
        self.height = height
        self.weight = weight
        self.gender = gender
        self.courses = {}

    def add_grade(self, course_name, grade):
        self.courses[course_name] = grade

    def average_grade(self):
        if len(self.courses) == 0:
            return -1
        else:
            return sum(self.courses.values()) / len(self.courses)

    def __str__(self):
        return f"id: {self.id} first name: {self.fname}, last name: {self.lname} genter: {self.genter} "


class Classroom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.students = []
        self.filename = room_name + '.csv'

    def add_demo_data(self):
        # Create student instances with specific data
        students_data = [
            [1, "Alice", "Johnson", "2000-01-01", 153, 49, "Female"],
            [2, "Bob", "Smith", "2001-02-02", 165, 59, "Male"],
            [3, "Charlie", "Brown", "2002-03-03", 159, 65, "Male"],
            [4, "Diana", "White", "2003-04-04", 169, 64, "Female"],
            [5, "Eva", "Black", "2004-05-05", 180, 80, "Female"],
            [6, "Frank", "Taylor", "2000-06-06", 165, 78, "Male"],
            [7, "Grace", "Lee", "2001-07-07", 155, 60, "Female"],
            [8, "Henry", "Miller", "2002-08-08", 192, 84, "Male"],
            [9, "Ivy", "Davis", "2003-09-09", 168, 58, "Female"],
            [10, "Jack", "Wilson", "2004-10-10", 178, 72, "Male"],
            [11, "Kathy", "Moore", "2000-11-11", 162, 64, "Female"],
            [12, "Liam", "White", "2001-12-12", 183, 95, "Male"],
            [13, "Mia", "Harris", "2002-01-13", 171, 80, "Female"],
            [14, "Noah", "Nelson", "2003-02-14", 176, 90, "Male"],
            [15, "Olivia", "Martin", "2004-03-15", 181, 71, "Female"],
            [16, "Paul", "Garcia", "2000-04-16", 187, 87, "Male"],
            [17, "Quincy", "Adams", "2001-05-17", 188, 92, "Male"],
            [18, "Rosa", "Martinez", "2002-06-18", 174, 95, "Female"],
            [19, "Sam", "Lee", "2003-07-19", 167, 60, "Male"],
            [20, "Tina", "Turner", "2004-08-20", 164, 54, "Female"]
        ]
        #id, fname, lname, dateBirth, height,weight, gender
        # Courses list
        courses = ['Math', 'History', 'Physics', 'English', 'Biology']
        # Add the students to the classroom
        for data in students_data:
            student = Student(id=data[0], fname=data[1], lname=data[2],
                    dateBirth=datetime.strptime(data[3], "%Y-%m-%d").date(),  # Convert string to datetime
                    height=data[4], weight=data[5], gender=data[6])

            # Add random grades for each course
            for course in courses:
                student.add_grade(course, random.randint(8, 20))  # Assign random grades between 8 and 20

            self.add_student(student)

    def add_student(self, student):
        self.students.append(student)

    def average_grade_class(self):
        if len(self.students) == 0:
            return -1

        total_grades = sum(st.average_grade() for st in self.students)
        return total_grades / len(self.students)

    def get_students_data(self):
        data = []
        for student in self.students:
            data.append({
                'ID': student.id,
                'First Name': student.fname,
                'Last Name': student.lname,
                'Date of Birth': student.dateBirth,
                'Height': student.height,
                'Weight': student.weight,
                'Gender': student.gender,
                'Courses': student.courses
            })
        return data

    def save_students_to_csv(self):
        df = pd.DataFrame(self.get_students_data())
        df.to_csv(self.filename, index=False)

    def load_students_from_csv(self):
        df = pd.read_csv(self.filename)
        self.students = []
        for index, row in df.iterrows():
            student = Student(
                row['ID'],
                row['First Name'],
                row['Last Name'],
                row['Date of Birth'],
                row['Height'],
                row['Weight'],
                row['Gender']
            )
            student.courses = eval(row['Courses'])
            self.students.append(student)

    def search_students(self, fname="", lname=""):
        """
        Search for students based on partial matches for first name and last name.
        If fname or lname is empty or None, it ignores that field in the search.
        """
        df = pd.DataFrame(self.get_students_data())  # Get the DataFrame of students

        # Convert to lowercase for case-insensitive search
        fname = fname.lower() if fname else ""
        lname = lname.lower() if lname else ""

        # Apply filtering to DataFrame
        if fname:
            df = df[df['First Name'].str.lower().str.contains(fname)]
        if lname:
            df = df[df['Last Name'].str.lower().str.contains(lname)]

        return df

    def student_exists(self, searchID):
        for student in self.students:
            if student.id == searchID:
                return True
        return False

    def get_next_student_id(self):

        # Check if there are no students
        if not self.students:
            return 1

        # Find the maximum ID among the students
        max_id = max(student.id for student in self.students)

        # Return the next ID
        return max_id + 1

    def get_student_by_id(self, id):
        for student in self.students:
            if student.id == id:
                return student
        return None

    def update_student(self, id, fname, lname, dateBirth, height, weight, gender):
        student = self.get_student_by_id(id)
        if student:
            student.fname = fname
            student.lname = lname
            student.dateBirth = dateBirth
            student.height = height
            student.weight = weight
            student.gender = gender
            return True
        return False
