import streamlit as st
from students import Student, Classroom
from datetime import datetime

def app(my_class_room):
    st.title('Edit Student Data')

    # Step 1: Input Student ID to Edit
    student_id = st.number_input('Enter Student ID to search:', 1, 1000)
    student = my_class_room.get_student_by_id(student_id)

    if student:
        # Step 2: Display and Edit Student Data
        with st.form("edit_student"):
            st.subheader(f'Editing Data for Student ID: {student.id}')
            fname = st.text_input('First Name', value=student.fname)
            lname = st.text_input('Last Name', value=student.lname)
            dateBirth = st.date_input('Birth Date', value=student.dateBirth)
            gender = st.radio('Gender', ['Male', 'Female'], index=(0 if student.gender == 'Male' else 1))
            weight = st.slider('Weight', 30, 150, value=student.weight)
            height = st.slider('Height', 130, 200, value=student.height)

            # Submit button to save changes
            submitted = st.form_submit_button("Save Changes", use_container_width=True)
            if submitted:
                my_class_room.update_student(student_id, fname, lname, dateBirth, height, weight, gender)
                st.success('Student data updated successfully!')
    else:
        st.warning('No student found with the provided ID.')