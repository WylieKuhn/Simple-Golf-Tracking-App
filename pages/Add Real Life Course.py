import streamlit as st
import sqlite3
from functions.geographic_data import get_countries
from functions.geographic_data import get_states

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
        

        courseInfo = {}
        courseInfo["name"] = st.text_input(label="Course Name")
        courseInfo["address"] = st.text_input(label="Address")

        col1, col2, col3, = st.columns(3)

        with col1:
           courseInfo["city"] = st.text_input(label="City/Town")
        with col2:
            courseInfo["State"] = st.selectbox(label="State/District", options=get_states())
        with col3:
            courseInfo["postCode"] = st.text_input(label="ZIP/Postal Code")
        courseInfo["country"] = st.selectbox(label="Country", options=get_countries())
        st.text("Test")

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
        
        hole_pars["totalPar"] = st.number_input(label="Course Par", step=1)
        

        # Input fields for each hole
        add_course_button = st.form_submit_button(label="Add Course")

        if add_course_button:
            print(courseInfo)

            if courseInfo["name"] == "" or courseInfo["address"] == "" or courseInfo["city"] == "" or courseInfo["state"] == "" or courseInfo["postCode"] == "" or courseInfo["country"] == "":
                st.error("Course Information Incomplete")

            else:
                parCheck = []
                for key, par in hole_pars.items():
                    parCheck.append(par)
                if sum(parCheck) != hole_pars["totalPar"]:
                    st.error("Mismatch Between Entered Hole Pars and Course Total Par")
                elif sum(parCheck) == hole_pars["totalPar"]:
                    conn.execute("""INSERT INTO courses(name, address, city, state, postal_code, country,hole_1_par,hole_2_par,hole_3_par,hole_4_par,hole_5_par,hole_6_par,
                hole_7_par,hole_8_par,hole_9_par,hole_10_par,hole_11_par,hole_12_par,hole_13_par,hole_14_par,hole_15_par,hole_16_par,
                hole_17_par,hole_18_par, total_par, front_nine_par, back_nine_par, user)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (courseInfo["name"], 
                                                                                
                                                                                hole_pars["hole 1"],hole_pars["hole 2"],hole_pars["hole 3"],hole_pars["hole 4"],hole_pars["hole 5"],hole_pars["hole 6"],
                hole_pars["hole 7"],hole_pars["hole 8"],hole_pars["hole 9"],hole_pars["hole 10"],hole_pars["hole 11"],hole_pars["hole 12"],hole_pars["hole 13"],
                hole_pars["hole 14"],hole_pars["hole 15"],hole_pars["hole 16"],hole_pars["hole 17"],hole_pars["hole 18"], parSum, frontNinePar,
                backNinePar, courseInfo["game"], option, courseInfo["type"]))
                conn.commit()

                st.success("Course Added Successfully!")



