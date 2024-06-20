import sqlite3

courses = [
    "Cherry Blossom", "Tourist Trap", "Seagull Stacks", "Arizona Modern", "Original Gothic",
    "Bogey's Bonanza", "Tethys Station", "Quixiote Valley", "Sweetopia", "Upside Town", 
    "Labyrinth", "Myst", "Venice", "Laser Lair", "Ice Lair", "Alfheim", "Widows Walkabout", 
    "Meow Wolf", "Gardens Of Babylon", "Shangri-La", "El Dorado", "Atlantis", 
    "Temple at Zerzura", "20,000 Leagues Under The Sea", "Journey To The Center Of The Earth",
    "Around The World In 80 Days"
]

def get_courses():
    conn = sqlite3.connect("golfstats.db")
    cur = conn.cursor()
    course_names = cur.execute("""SELECT DISTINCT name FROM courses""")
    list_of_course_names = []
    
    for course in course_names.fetchall():
        list_of_course_names.append(course[0])
    return list_of_course_names

def get_states():
    states = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", 
              "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", 
              "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", 
              "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
    return states

