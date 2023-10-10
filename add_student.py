import streamlit as st
from students import Student, Classroom
from datetime import datetime

def app(my_class_room):
    st.subheader('Add Student')
    next_id = my_class_room.get_next_student_id()
    with st.form("student_details", clear_on_submit=True):
        id = st.number_input('ID', 1, 1000, value=next_id)
        fname = st.text_input('ENTER FIRST NAME ')
        lname = st.text_input('ENTER LAST NAME')
        dateBirth = st.date_input('ENTER YOUR BIRTH DATE ')
        gender = st.radio('GENDER ', ['Male', 'Female'])
        weight = st.slider('WEIGHT', 30, 150)
        height = st.slider('HEIGHT', 130, 200)

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit", use_container_width=True)

        # If form is submitted and ID does not exist, add student
        if submitted: # and len(errors) == 0:
            # Validation
            num_errors = validate_entry(my_class_room, id, fname, lname)
            if num_errors == 0:
                stu1 = Student(id, fname, lname, dateBirth, height, weight, gender)
                my_class_room.add_student(stu1)
                st.success(f"Student {fname} {lname} added successfully")

def validate_entry(my_class_room, id, fname, lname):
    # Validation
    errors = []
    id_exists = my_class_room.student_exists(id)
    if id_exists:
        errors.append(f"Student id:{id} exists! Leave the system to auto generate new id.")
    if not fname:
        errors.append("First name cannot be empty.")
    if not lname:
        errors.append("Last name cannot be empty.")

    for error in errors:
        st.warning(error)

    return len(errors)