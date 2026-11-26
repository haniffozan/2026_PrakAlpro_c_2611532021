schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

bussiest_day = ""
longest = 0 # the amount of courses tha bussiest day has
course_appearance = 0
for day in schedule:
    # to find the bussiest day
    if len(schedule[day]) > longest:
        longest = len(schedule[day])
        bussiest_day = day

print(f"Bussiest day: {bussiest_day} ({longest} courses).")

current_course = input("Look how many day the course you input existed: ")
for day in schedule:
    for course in schedule[day]:
        if course == current_course:
            course_appearance += 1

print(f"{current_course}: {course_appearance} days.")
