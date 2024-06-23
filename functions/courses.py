import sqlite3




wmc_courses = [
    "Cherry Blossom", "Tourist Trap", "Seagull Stacks", "Arizona Modern", "Original Gothic",
    "Bogey's Bonanza", "Tethys Station", "Quixiote Valley", "Sweetopia", "Upside Town", 
    "Labyrinth", "Myst", "Venice", "Laser Lair", "Ice Lair", "Alfheim", "Widows Walkabout", 
    "Meow Wolf", "Gardens Of Babylon", "Shangri-La", "El Dorado", "Atlantis", 
    "Temple at Zerzura", "20,000 Leagues Under The Sea", "Journey To The Center Of The Earth",
    "Around The World In 80 Days"
]



def get_digital_courses():
    conn = sqlite3.connect("database/golfstats.db")
    cur = conn.cursor()
    course_names = cur.execute("""SELECT DISTINCT name FROM digital_courses""")
    list_of_course_names = []
    
    for course in course_names.fetchall():
        list_of_course_names.append(course[0])
    return list_of_course_names


