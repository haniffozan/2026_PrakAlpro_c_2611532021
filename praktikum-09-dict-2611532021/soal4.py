all_students = set(input("All students: ").split())
student_submited = set(input("Students submitted: ").split())
not_submited = all_students - student_submited

print(f"Submitted: {len(student_submited)} students")
print(f"Not submitted: {len(not_submited)} students")
for student in not_submited:
    print(student)