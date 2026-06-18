import pandas as pd
import matplotlib.pyplot as plt
import random

students = []

for i in range(1, 101):
    student = {
        "Student_ID": i,
        "Age": random.randint(18, 25),
        "Maths": random.randint(50, 100),
        "Physics": random.randint(50, 100),
        "Chemistry": random.randint(50, 100),
        "English": random.randint(50, 100),
        "Hindi": random.randint(50, 100),
        "Computer": random.randint(50, 100),
        "Economics": random.randint(50, 100),
        "History": random.randint(50, 100),
        "Geography": random.randint(50, 100),
        "Biology": random.randint(50, 100),
        "Attendance": random.randint(70, 100),
        "Study_Hours": random.randint(1, 10),
        "Assignments": random.randint(1, 20),
        "Projects": random.randint(1, 10),
        "Tests_Attended": random.randint(5, 15),
        "Sports_Score": random.randint(40, 100),
        "Library_Visits": random.randint(0, 20),
        "Extra_Curricular": random.randint(0, 10),
        "Discipline_Score": random.randint(60, 100),
        "Communication": random.randint(50, 100),
        "Leadership": random.randint(50, 100),
        "Teamwork": random.randint(50, 100),
        "Creativity": random.randint(50, 100),
        "Problem_Solving": random.randint(50, 100),
        "Coding_Skill": random.randint(50, 100),
        "Typing_Speed": random.randint(20, 80),
        "Internet_Usage": random.randint(1, 8),
        "Sleep_Hours": random.randint(4, 10),
        "Health_Score": random.randint(50, 100),
        "BMI": round(random.uniform(18, 30), 1),
        "Parent_Education": random.randint(10, 20),
        "Family_Income": random.randint(20000, 100000),
        "Distance_From_School": random.randint(1, 20),
        "Mobile_Usage": random.randint(1, 8),
        "Social_Media_Hours": random.randint(0, 6),
        "Online_Courses": random.randint(0, 5),
        "Scholarship": random.randint(0, 1),
        "Semester": random.randint(1, 8),
        "CGPA": round(random.uniform(5, 10), 2),
        "Placement_Training": random.randint(0, 1),
        "Internships": random.randint(0, 3),
        "Overall_Performance": random.randint(50, 100),
        "AI_Skill": random.randint(50, 100),
        "Cloud_Skill": random.randint(50, 100),
        "AWS_Skill": random.randint(50, 100),
        "GitHub_Skill": random.randint(50, 100),
        "Python_Skill": random.randint(50, 100),
        "Java_Skill": random.randint(50, 100)
    }
    students.append(student)

df = pd.DataFrame(students)

# Save dataset
df.to_csv("student_dataset.csv", index=False)

print("Dataset Created Successfully!")
print(df.head())

# Chart 1: Study Hours vs CGPA
plt.figure(figsize=(8, 5))
plt.scatter(df["Study_Hours"], df["CGPA"])
plt.title("Study Hours vs CGPA")
plt.xlabel("Study Hours")
plt.ylabel("CGPA")
plt.show()

# Chart 2: Attendance Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Attendance"], bins=10)
plt.title("Attendance Distribution")
plt.xlabel("Attendance %")
plt.ylabel("Number of Students")
plt.show()

# Chart 3: Average Subject Marks
subjects = [
    "Maths", "Physics", "Chemistry", "English",
    "Hindi", "Computer", "Economics",
    "History", "Geography", "Biology"
]

avg_marks = df[subjects].mean()

plt.figure(figsize=(10, 5))
plt.bar(avg_marks.index, avg_marks.values)
plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.show()

# Chart 4: Coding Skill vs Placement Training
plt.figure(figsize=(8, 5))
plt.scatter(df["Coding_Skill"], df["Placement_Training"])
plt.title("Coding Skill vs Placement Training")
plt.xlabel("Coding Skill")
plt.ylabel("Placement Training")
plt.show()
