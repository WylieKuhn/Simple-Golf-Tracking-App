import sqlite3
from courses import courses

print("Welcome to the Simple Golf Tracking App")
print("")
print("This app was built on streamlit in python mainly for use by players of Walkabout Mini-Golf, but can be used to track real life golf games as well")
print("")
print("After this window closes run 'launch.bat' to run the app")

WMCInstall = str(input("Would you like to initialize this app with the walkabout mini-golf courses information already in the database? [y/n]: "))



conn = sqlite3.connect("golfstats.db")
cur = conn.cursor()
cur.execute(f"""CREATE TABLE courses(name, type, game, easy, medium, hard, no_difficulty)""")
conn.commit()

if WMCInstall.lower() == 'y':
    for course in courses:
        cur.execute("""INSERT INTO courses(name, type, game, easy, medium, hard, no_difficulty) VALUES (?, ?, ?, ?, ?, ?, ?)""", (course, "VR", "Walkabout Mini-Golf", 1, 0, 1, 0,))
        conn.commit()
else:
    print("Welcome")