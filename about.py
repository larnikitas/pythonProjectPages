import streamlit as st

def app():
    st.subheader('Greenwood International School')

    st.write("Greenwood International School, nestled in the serene environment of Knowledge City, stands as a beacon of progressive education and holistic development. Established in 1995, the school has earned a reputation for providing a robust educational experience that seeks to cultivate the innate potential of each student.")
    # Display the image
    st.image("images/school.png", caption="School in forest", use_column_width=True)

    with st.expander("See Philosophy:"):
        st.write("The philosophy of Greenwood is deeply rooted in the belief that education should extend beyond academic excellence to include the development of character, creativity, and curiosity in every child. The school aims to foster an environment where students are encouraged to explore, inquire, and innovate, enabling them to become lifelong learners and contributors to a global society.")
    # Create three columns
    col1, col2, col3 = st.columns(3)

    # Display images
    with col1:
        st.image("images/students1.png", caption="students playing", use_column_width=True)

    with col2:
        st.image("images/students2.png", caption="students playing", use_column_width=True)

    with col3:
        st.image("images/students3.png", caption="students playing", use_column_width=True)

