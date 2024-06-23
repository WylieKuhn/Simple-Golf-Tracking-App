import sqlite3
from functions.courses import wmc_courses
from functions.wmg_course_info import all_courses

print("Welcome to the Simple Golf Tracking App")
print("")
print("This app was built on streamlit in python mainly for use by players of Walkabout Mini-Golf, but can be used to track real life golf games as well")
print("")
print("After this window closes run 'launch.bat' to run the app")

WMCInstall = str(input("Would you like to initialize this app with the walkabout mini-golf courses information already in the database? [y/n]: "))



conn = sqlite3.connect("database/golfstats.db")
cur = conn.cursor()
cur.execute(f"""CREATE TABLE digital_courses(name, hole_1_par,hole_2_par,hole_3_par,hole_4_par,hole_5_par,hole_6_par,
            hole_7_par,hole_8_par,hole_9_par,hole_10_par,hole_11_par,hole_12_par,hole_13_par,hole_14_par,hole_15_par,hole_16_par,
            hole_17_par,hole_18_par, total_par, front_nine_par, back_nine_par, game, difficulty, type, user)""")
conn.commit()

cur.execute(f"""CREATE TABLE irl_courses(name, address, city, state, postal_code, country, hole_1_par,hole_2_par,hole_3_par,hole_4_par,hole_5_par,hole_6_par,
            hole_7_par,hole_8_par,hole_9_par,hole_10_par,hole_11_par,hole_12_par,hole_13_par,hole_14_par,hole_15_par,hole_16_par,
            hole_17_par,hole_18_par, total_par, front_nine_par, back_nine_par)""")
conn.commit()

if WMCInstall.lower() == 'y':
    for course in all_courses:
        cur.execute("""INSERT INTO digital_courses(name, hole_1_par,hole_2_par,hole_3_par,hole_4_par,hole_5_par,hole_6_par,
            hole_7_par,hole_8_par,hole_9_par,hole_10_par,hole_11_par,hole_12_par,hole_13_par,hole_14_par,hole_15_par,hole_16_par,
            hole_17_par,hole_18_par, total_par, front_nine_par, back_nine_par, game, difficulty, type, user)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", 
            (course["name"], course["hole_1_par"],course["hole_2_par"],course["hole_3_par"],course["hole_4_par"],course["hole_5_par"],course["hole_6_par"],
            course["hole_7_par"],course["hole_8_par"],course["hole_9_par"],course["hole_10_par"],course["hole_11_par"],course["hole_12_par"],course["hole_13_par"],
            course["hole_14_par"],course["hole_15_par"],course["hole_16_par"],course["hole_17_par"],course["hole_18_par"], course["total_par"], course["front_nine_par"],
            course["back_nine_par"], course["game"], course["difficulty"], course["type"], "Broman"))
        conn.commit()
    
else:
    print("Welcome")
    
