import streamlit as st
import pandas as pd
'''
def app(my_class_room):
    st.subheader('Home Page - All Students')

    # Button to save data to CSV
    if st.button('Save Data'):
        my_class_room.save_students_to_csv()
        st.success("Data saved successfully!")

    # Button to load data from CSV
    if st.button('Load Data'):
        try:
            my_class_room.load_students_from_csv()
            st.success("Data loaded successfully!")
        except FileNotFoundError:
            st.error("No data file found!")

    rows = len(my_class_room.get_students_data()) * 35 + 35
    if len(my_class_room.students) > 0:
        st.dataframe(my_class_room.get_students_data(), height = rows)
    else:
        st.write('no students in the classroom')

'''


def app(my_class_room):
    st.subheader('Home Page - All Students')
    selection = 'Sort by ID'
    # First row of buttons [Save Data, Load Data, Sort by ID]
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button('Save Data'):
            my_class_room.save_students_to_csv()
            st.success("Data saved successfully!")

    with col2:
        if st.button('Load Data'):
            try:
                my_class_room.load_students_from_csv()
                st.success("Data loaded successfully!")
            except FileNotFoundError:
                st.error("No data file found!")

    with col3:
        if st.button('Sort by ID'):
            selection = 'Sort by ID'
            my_class_room.sort_students_by_id()
            st.success("Data sorted by ID!")

    # Second row of buttons [Sort by Grade, Sort by BMI, Sort by Name]
    col4, col5, col6 = st.columns(3)

    with col4:
        if st.button('Sort by Grade'):
            selection = 'Sort by Grade'
            my_class_room.bubble_sort_students_by_grade()
            st.success("Data sorted by grade!")

    with col5:
        if st.button('Sort by BMI'):
            selection = 'Sort by BMI'
            my_class_room.selection_sort_students_by_bmi()
            st.success("Data sorted by BMI!")

    with col6:
        if st.button('Sort by Name'):
            selection = 'Sort by Name'
            my_class_room.sort_students_by_name()
            st.success("Data sorted by name!")

    # Display Data
    data_to_show = my_class_room.generate_dataframe()
    if selection == 'Sort by Grade':
        data_to_show = data_to_show[['Last Name', 'First Name', 'Average Grade','Math', 'History',
                     'Physics', 'English', 'Biology']]
    elif selection == 'Sort by BMI':
        data_to_show = data_to_show[['Last Name', 'First Name','Height', 'Weight', 'BMI','BMI Category']]
    elif selection == 'Sort by Name':
        data_to_show = data_to_show[['Last Name', 'First Name','Average Grade', 'BMI']]

    rows_shown = len(data_to_show)
    if rows_shown > 15:
        rows_shown = 15
    rows = rows_shown * 35 + 35
    if len(data_to_show) > 0:
        st.dataframe(data_to_show, height=rows)
    else:
        st.write('No students in the classroom')