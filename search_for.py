import streamlit as st

def app(my_class_room):
    st.subheader('Search for Student')

    # User input
    fname = st.text_input('Enter First Name:')
    lname = st.text_input('Enter Last Name:')

    # Button to trigger search
    if st.button('Search', use_container_width=True):
        # Search students and display results
        results = my_class_room.search_students(fname, lname)

        if not results.empty:  # Check if DataFrame is not empty
            st.dataframe(results)
        else:
            st.warning('No students found.')