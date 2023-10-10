import streamlit as st
from streamlit_option_menu import option_menu
import home, add_student, edit_student,  about, search_for
from students import Student, Classroom

# https://icons.getbootstrap.com/

def main():
    st.set_page_config(layout="wide")
    menu = ["Home", "Add Student","Edit Student", "Search Student", "About"]

    # Initialize session state for the classroom if it doesn't exist
    if 'my_class_room' not in st.session_state:
        st.session_state.my_class_room = Classroom('b_class')
        st.session_state.my_class_room.add_demo_data()

    with st.sidebar:
        page = option_menu(
            menu_title='M E N U',
            options=menu,
            icons=['house', 'person-fill','pencil-square', 'binoculars-fill', 'info-circle'],
            menu_icon='chat-text-fill',
            orientation="vertical",
            default_index=0,
            styles={
                "container": {"padding": "5!important", "background-color": 'black'},
                "icon": {"color": "white", "font-size": "23px"},
                "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                             "--hover-color": "blue"},
                "nav-link-selected": {"background-color": "#02ab21"}, }
        )

    if page == "Home":
        home.app(st.session_state.my_class_room)

    elif page == "Add Student":
        add_student.app(st.session_state.my_class_room)

    elif page == "Edit Student":
        edit_student.app(st.session_state.my_class_room)

    elif page == "Search Student":
        search_for.app(st.session_state.my_class_room)

    elif page == "About":
        about.app()

if __name__ == '__main__':
    main()
