import sqlite3
import statistics
import streamlit as st
import matplotlib.pyplot as plt
from scipy.stats import norm

conn = sqlite3.connect("database/golfstats.db")
cur = conn.cursor()
totalScores = [0,0]
zScores = [0,0]

average = st.empty()





def get_courses():
    conn = sqlite3.connect("database/golfstats.db")
    cur = conn.cursor()
    course_names = cur.execute("""SELECT DISTINCT name FROM digital_courses""")
    list_of_course_names = []
    
    
    for course in course_names.fetchall():
        list_of_course_names.append(course[0])
    return list_of_course_names


with st.container():
    zScoreDisplay = st.empty()

    with st.form(key="statsform"):
        
        course = st.selectbox(label="Select Course", options=get_courses())
        difficulty = st.selectbox(label="Difficulty", options=["None", "Easy", "Intermediate", "Hard"])

        submit = st.form_submit_button(label="See Stats")

        if submit:
            totalScores = []
            zScores = []

            data = cur.execute(f"""SELECT total_score FROM games WHERE course = ? AND difficulty = ?""", (course, difficulty))

            for total in data.fetchall():
                totalScores.append(total[0])

            if len(totalScores) > 1:
                for score in totalScores:
                    zScore = round((score-statistics.mean(totalScores))/statistics.pstdev(totalScores),3)
                    zScores.append(zScore)

   
    
    col1, col2, col3, = st.columns(3)

    with col1:
        pass
    with col2:
        st.metric(label="Mean", value=round(statistics.mean(totalScores),2))

        st.text("Chance of beating your")
        st.text("best score")
        st.metric(label="", value=f"{(1-norm.sf(min(zScores)))*100:.2f}%", label_visibility="hidden")

        st.metric(label="Standard Deviation", value=round(statistics.pstdev(totalScores),2))
        st.metric(label="Variance", value=round(statistics.variance(totalScores),2))
        

    fig, ax = plt.subplots()
    ax.hist(zScores, bins=50)
    st.text("Normal Distrobution")
    st.pyplot(fig)
    
    












