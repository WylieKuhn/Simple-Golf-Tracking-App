import streamlit as st
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("golfstats.db")
cur = conn.cursor()




# Container for the form
with st.container():
    courseInfo = {}
    easy = int()
    intermediate = int()
    hard = int()
    noOptions = int()
    hole_pars = {}

    st.sidebar.text("Add User")
    # Centered header
    st.markdown("<h1 style='text-align: center;'>Add A Course</h1>", unsafe_allow_html=True)

    # Form definition
    with st.form(key="scores"):

        # Columns for hole inputs
        col1, col2 = st.columns(2)

        courseInfo = {}

        with col1:
            courseInfo["name"] = st.text_input(label="Course Name")
            courseInfo["type"] = st.selectbox(label="Difficulty Options", options=["VR", "Non-VR Digital", "IRL"])
        with col2:
            courseInfo["difficulty_options"] = st.selectbox(label="Difficulty Options", options=["None", "Easy and Hard", "Easy, Intermediate, and Hard"])
            courseInfo["game"] = st.text_input(label="Game Name")

        st.header("Enter Hole Pars")

        col1, col2, col3, col4, col5, col6 = st.columns(6)

        with col1:
            hole_pars["Hole 1"] = st.number_input(label="Hole 1", min_value=0, step=1, key="1")
            hole_pars["Hole 7"] = st.number_input(label="Hole 7", min_value=0, step=1, key="7")
            hole_pars["Hole 13"] = st.number_input(label="Hole 13", min_value=0, step=1, key="13")
        with col2:
            hole_pars["Hole 2"] = st.number_input(label="Hole 2", min_value=0, step=1, key="2")
            hole_pars["Hole 8"] = st.number_input(label="Hole 8", min_value=0, step=1, key="8")
            hole_pars["Hole 14"] = st.number_input(label="Hole 14", min_value=0, step=1, key="14")
        with col3:
            hole_pars["Hole 3"] = st.number_input(label="Hole 3", min_value=0, step=1, key="3")
            hole_pars["Hole 9"] = st.number_input(label="Hole 9", min_value=0, step=1, key="9")
            hole_pars["Hole 15"] = st.number_input(label="Hole 15", min_value=0, step=1, key="15")
        with col4:
            hole_pars["Hole 4"] = st.number_input(label="Hole 4", min_value=0, step=1, key="4")
            hole_pars["Hole 10"] = st.number_input(label="Hole 10", min_value=0, step=1, key="10")
            hole_pars["Hole 16"] = st.number_input(label="Hole 16", min_value=0, step=1, key="16")
        with col5:
            hole_pars["Hole 5"] = st.number_input(label="Hole 5", min_value=0, step=1, key="5")
            hole_pars["Hole 11"] = st.number_input(label="Hole 11", min_value=0, step=1, key="11")
            hole_pars["Hole 17"] = st.number_input(label="Hole 17", min_value=0, step=1, key="17")
        with col6:
            hole_pars["Hole 6"] = st.number_input(label="Hole 6", min_value=0, step=1, key="6")
            hole_pars["Hole 12"] = st.number_input(label="Hole 12", min_value=0, step=1, key="12")
            hole_pars["Hole 18"] = st.number_input(label="Hole 18", min_value=0, step=1, key="18")
        
        st.number_input(label="Course Par", step=1)
        

        # Input fields for each hole
        add_course_button = st.form_submit_button(label="Add Course")

        if add_course_button:
            print(courseInfo)

            if courseInfo["name"]=="" or courseInfo["game"] == "":
                st.error("Course Information Incomplete")
            else:
                if courseInfo["type"] == "VR":
                    if courseInfo["difficulty_options"] == "None":
                        noOptions = 1
                    elif courseInfo["difficulty_options"] == "Easy and Hard":
                        easy = 1
                        hard = 1
                    elif courseInfo["difficulty_options"] == "Easy, Intermediate, and Hard":
                        easy = 1
                        hard = 1
                        intermediate = 1

                    cur.execute(
                        """INSERT INTO courses(name, type, game, easy, medium, hard, no_difficulty)
                        VALUES (?, ?, ?, ?, ?, ?, ?)""",
                        (courseInfo['name'], courseInfo['type'], courseInfo['game'], easy, intermediate, hard, noOptions)
                    )
                    conn.commit()

                easy = 0
                hard = 0
                intermediate = 0
                noOptions = 0

                st.success("Course Added Successfully!")



