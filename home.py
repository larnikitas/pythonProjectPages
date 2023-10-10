import streamlit as st
import pandas as pd

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



