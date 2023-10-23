import streamlit as st
from students import Student, Classroom


def app(my_class_room):
    st.title("Student Grades Modifier")
    # Input for the student ID
    updated = False
    student_id = st.number_input("Enter Student ID", min_value=1, value=1)
    student = my_class_room.get_student_by_id(student_id)
    # Button to search for the student
    if st.button("Search"):
        student = my_class_room.get_student_by_id(student_id)

    if student:
        st.write(f"Found: {student.fname} {student.lname}")
        updated = upgrade_values(student)

    else:
        st.write("Student not Found!")

    # Displaying success message outside the button click logic to avoid immediate clearing
    if updated:
        st.success("Grades updated successfully!")

def upgrade_values(student):
    updated = False
    with st.form(key="grades_form"):
        courses = student.courses
        math_grade = st.number_input("Grade for Math", min_value=-1, max_value=100, value=courses['Math'])
        history_grade = st.number_input("Grade for History", min_value=-1, max_value=100,
                                        value=courses['History'])
        physics_grade = st.number_input("Grade for Physics", min_value=-1, max_value=100,
                                        value=courses['Physics'])
        english_grade = st.number_input("Grade for English", min_value=-1, max_value=100,
                                        value=courses['English'])
        biology_grade = st.number_input("Grade for Biology", min_value=-1, max_value=100,
                                        value=courses['Biology'])

        # Button to update the grades
        submitted = st.form_submit_button("Update Grades")

    # Move grade updating logic outside the form to ensure the values are updated before the next cycle of rendering
    if submitted:
        student.add_grade('Math', math_grade)
        student.add_grade('History', history_grade)
        student.add_grade('Physics', physics_grade)
        student.add_grade('English', english_grade)
        student.add_grade('Biology', biology_grade)

        updated = True

    return updated