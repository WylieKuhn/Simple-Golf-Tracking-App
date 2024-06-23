import streamlit as st
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("database/golfstats.db")
cur = conn.cursor()




# Container for the form
with st.container():
    courseInfo = {}
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
            hole_pars["hole 1"] = st.number_input(label="Hole 1", min_value=0, step=1, key="1")
            hole_pars["hole 7"] = st.number_input(label="Hole 7", min_value=0, step=1, key="7")
            hole_pars["hole 13"] = st.number_input(label="Hole 13", min_value=0, step=1, key="13")
        with col2:
            hole_pars["hole 2"] = st.number_input(label="Hole 2", min_value=0, step=1, key="2")
            hole_pars["hole 8"] = st.number_input(label="Hole 8", min_value=0, step=1, key="8")
            hole_pars["hole 14"] = st.number_input(label="Hole 14", min_value=0, step=1, key="14")
        with col3:
            hole_pars["hole 3"] = st.number_input(label="Hole 3", min_value=0, step=1, key="3")
            hole_pars["hole 9"] = st.number_input(label="Hole 9", min_value=0, step=1, key="9")
            hole_pars["hole 15"] = st.number_input(label="Hole 15", min_value=0, step=1, key="15")
        with col4:
            hole_pars["hole 4"] = st.number_input(label="Hole 4", min_value=0, step=1, key="4")
            hole_pars["hole 10"] = st.number_input(label="Hole 10", min_value=0, step=1, key="10")
            hole_pars["hole 16"] = st.number_input(label="Hole 16", min_value=0, step=1, key="16")
        with col5:
            hole_pars["hole 5"] = st.number_input(label="Hole 5", min_value=0, step=1, key="5")
            hole_pars["hole 11"] = st.number_input(label="Hole 11", min_value=0, step=1, key="11")
            hole_pars["hole 17"] = st.number_input(label="Hole 17", min_value=0, step=1, key="17")
        with col6:
            hole_pars["hole 6"] = st.number_input(label="Hole 6", min_value=0, step=1, key="6")
            hole_pars["hole 12"] = st.number_input(label="Hole 12", min_value=0, step=1, key="12")
            hole_pars["hole 18"] = st.number_input(label="Hole 18", min_value=0, step=1, key="18")
        
        st.number_input(label="Course Par", step=1)
        

        # Input fields for each hole
        add_course_button = st.form_submit_button(label="Add Course")

        if add_course_button: 
            parSum = 0
            frontNinePar = hole_pars["hole 1"]+hole_pars["hole 2"]+hole_pars["hole 3"]+hole_pars["hole 4"]+hole_pars["hole 5"]+hole_pars["hole 6"]+hole_pars["hole 7"]+hole_pars["hole 8"]+hole_pars["hole 9"]
            backNinePar = hole_pars["hole 10"]+hole_pars["hole 11"]+hole_pars["hole 12"]+hole_pars["hole 13"]+hole_pars["hole 14"]+hole_pars["hole 15"]+hole_pars["hole 16"]+hole_pars["hole 17"]+ hole_pars["hole 18"]

            for hole, value in hole_pars.items():
                parSum += value

            if courseInfo["name"]=="" or courseInfo["game"] == "":
                st.error("Course Information Incomplete")

            else:
                if courseInfo["difficulty_options"] == "None":
                    conn.execute("""INSERT INTO courses(name, hole_1_par,hole_2_par,hole_3_par,hole_4_par,hole_5_par,hole_6_par,
                hole_7_par,hole_8_par,hole_9_par,hole_10_par,hole_11_par,hole_12_par,hole_13_par,hole_14_par,hole_15_par,hole_16_par,
                hole_17_par,hole_18_par, total_par, front_nine_par, back_nine_par, game, difficulty, type)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", 
                (courseInfo["name"], hole_pars["hole 1"],hole_pars["hole 2"],hole_pars["hole 3"],hole_pars["hole 4"],hole_pars["hole 5"],hole_pars["hole 6"],
                hole_pars["hole 7"],hole_pars["hole 8"],hole_pars["hole 9"],hole_pars["hole 10"],hole_pars["hole 11"],hole_pars["hole 12"],hole_pars["hole 13"],
                hole_pars["hole 14"],hole_pars["hole 15"],hole_pars["hole 16"],hole_pars["hole 17"],hole_pars["hole 18"], parSum, frontNinePar,
                backNinePar, courseInfo["game"], "None", courseInfo["type"]))
            
                    conn.commit()

                if courseInfo["difficulty_options"] == "Easy and Hard":
                    for option in ["Easy", "Hard"]:
                        conn.execute("""INSERT INTO courses(name, hole_1_par,hole_2_par,hole_3_par,hole_4_par,hole_5_par,hole_6_par,
                hole_7_par,hole_8_par,hole_9_par,hole_10_par,hole_11_par,hole_12_par,hole_13_par,hole_14_par,hole_15_par,hole_16_par,
                hole_17_par,hole_18_par, total_par, front_nine_par, back_nine_par, game, difficulty, type)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", 
                (courseInfo["name"], hole_pars["hole 1"],hole_pars["hole 2"],hole_pars["hole 3"],hole_pars["hole 4"],hole_pars["hole 5"],hole_pars["hole 6"],
                hole_pars["hole 7"],hole_pars["hole 8"],hole_pars["hole 9"],hole_pars["hole 10"],hole_pars["hole 11"],hole_pars["hole 12"],hole_pars["hole 13"],
                hole_pars["hole 14"],hole_pars["hole 15"],hole_pars["hole 16"],hole_pars["hole 17"],hole_pars["hole 18"], parSum, frontNinePar,
                backNinePar, courseInfo["game"], option, courseInfo["type"]))
                        conn.commit()
                
                if courseInfo["difficulty_options"] == "Easy, Intermediate, and Hard":
                    for option in ["Easy", "Intermediate", "Hard"]:
                        conn.execute("""INSERT INTO courses(name, hole_1_par,hole_2_par,hole_3_par,hole_4_par,hole_5_par,hole_6_par,
                hole_7_par,hole_8_par,hole_9_par,hole_10_par,hole_11_par,hole_12_par,hole_13_par,hole_14_par,hole_15_par,hole_16_par,
                hole_17_par,hole_18_par, total_par, front_nine_par, back_nine_par, game, difficulty, type)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (courseInfo["name"], hole_pars["hole 1"],hole_pars["hole 2"],hole_pars["hole 3"],hole_pars["hole 4"],hole_pars["hole 5"],hole_pars["hole 6"],
                hole_pars["hole 7"],hole_pars["hole 8"],hole_pars["hole 9"],hole_pars["hole 10"],hole_pars["hole 11"],hole_pars["hole 12"],hole_pars["hole 13"],
                hole_pars["hole 14"],hole_pars["hole 15"],hole_pars["hole 16"],hole_pars["hole 17"],hole_pars["hole 18"], parSum, frontNinePar,
                backNinePar, courseInfo["game"], option, courseInfo["type"]))
                        conn.commit()

            st.success("Course Added Successfully!")



