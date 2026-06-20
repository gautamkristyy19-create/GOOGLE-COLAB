Open In Colab

student_name="yash"
student_age=18
attendence=85.5
is_present=True
     

students=[]
for marks  in students:
  if marks>=40:
    print("pass")
  else:
    print("fail")
     

numbers = [10, -5, 0, 25, -8, 12]

for num in numbers:
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")
     

students = {
    "Rahul": {"study_hours": 5, "attendance": 80, "marks": 85},
    "Priya": {"study_hours": 3, "attendance": 90, "marks": 65},
    "Amit": {"study_hours": 2, "attendance": 70, "marks": 15},
    "Neha": {"study_hours": 6, "attendance": 95, "marks": 92},
    "Riya": {"study_hours": 4, "attendance": 60, "marks": 35}
}

for name, data in students.items():
    print("\nStudent:", name)

    marks = data["marks"]
    attendance = data["attendance"]
    study_hours = data["study_hours"]

    if marks > 75:
        print("Performance: Strong")
    elif marks >= 40:
        print("Performance: Needs Improvement")
    else:
        print("Performance: Failed, Repeat Class")

    if attendance < 75:
        print("Warning: Low Attendance")

    if study_hours < 4:
        print("Warning: Need More Study Time")
     
Student: Rahul
Performance: Strong

Student: Priya
Performance: Needs Improvement
Warning: Need More Study Time

Student: Amit
Performance: Failed, Repeat Class
Warning: Low Attendance
Warning: Need More Study Time

Student: Neha
Performance: Strong

Student: Riya
Performance: Failed, Repeat Class
Warning: Low Attendance

students = {
    "Rahul": {"marks": 85, "attendance": 80, "study_hours": 5},
    "Priya": {"marks": 65, "attendance": 70, "study_hours": 3},
    "Amit": {"marks": 20, "attendance": 90, "study_hours": 4},
    "Neha": {"marks": 92, "attendance": 95, "study_hours": 6},
    "Riya": {"marks": 35, "attendance": 60, "study_hours": 4}
}

name = input("Enter student name: ")

if name in students:
    data = students[name]

    if data["marks"] > 75:
        print("Strong Performance")
    elif data["marks"] >= 40:
        print("Needs Improvement")
    else:
        print("Failed")

    if data["attendance"] < 75:
        print("Warning:Low Attendance")

    if data["study_hours"] < 4:
        print(" Warning:Need More Study Time")

     
Enter student name: Rahul
Strong Performance

transactions = [
    {"transaction_id": "TX101", "amount": 6200, "method": "Credit Card"},
    {"transaction_id": "TX102", "amount": 5500, "method": "Gift Card"},
    {"transaction_id": "TX103", "amount": 1200, "method": "Gift Card"},
    {"transaction_id": "TX104", "amount": 8000, "method": "Gift Card"},
    {"transaction_id": "TX105", "amount": 450, "method": "PayPal"}
]

flagged_transactions = []

for t in transactions:
    if t["amount"] > 5000 and t["method"] == "Gift Card":
        flagged_transactions.append(t)

print(flagged_transactions)

     
[{'transaction_id': 'TX102', 'amount': 5500, 'method': 'Gift Card'}, {'transaction_id': 'TX104', 'amount': 8000, 'method': 'Gift Card'}]

transactions = [
    {"transaction_id": "TX101", "amount": 6200, "method": "Credit Card"},
    {"transaction_id": "TX102", "amount": 5500, "method": "Gift Card"},
    {"transaction_id": "TX103", "amount": 1200, "method": "Gift Card"},
    {"transaction_id": "TX104", "amount": 8000, "method": "Gift Card"},
    {"transaction_id": "TX105", "amount": 450, "method": "PayPal"}
]

flagged_transactions = []

for t in transactions:
    if t["amount"] > 5000 and t["method"] == "Gift Card":
        flagged_transactions.append(t["transaction_id"])

print(flagged_transactions)
     
['TX102', 'TX104']

def pass_or_fail(marks):
    if marks > 27:
        return "Pass"
    else:
        return "Fail"


marks = int(input("Enter marks: "))
print(pass_or_fail(marks))
     
Enter marks: 34
Pass

def highest_marks(marks):
    return max(marks)

def average_marks(marks):
    return sum(marks) / len(marks)

def count_above_75(marks):
    count = 0
    for mark in marks:
        if mark > 75:
            count += 1
    return count

marks = [78, 91, 55, 72, 40, 88, 98, 81, 11, 23, 78, 88, 91, 96]

print(highest_marks(marks))
print(average_marks(marks))
print(count_above_75(marks))
     
98
70.71428571428571
9

from google.colab import files
uploaded=files.upload()
     
Upload widget is only available when the cell has been executed in the current browser session. Please rerun this cell to enable.
Saving session4_dummy_students_data.csv.xls to session4_dummy_students_data.csv.xls

import pandas as pd

# Read CSV file
df = pd.read_csv("sessio")

# Calculate average score
avg_score = df["Score"].mean()

print("Average Score:", avg_score)
     

df["average"] = df[["math", "science", "english"]].mean(axis=1)
print(df[["name", "math", "science", "english", "average"]])
low_attendence=df[df["attendance_percent"]<75]
print(low_attendence)
     
      name  math  science  english    average
0    Aarav    78       84       69  77.000000
1     Diya    91       88       94  91.000000
2    Kabir    55       61       58  58.000000
3    Meera    72       79       81  77.333333
4    Rohan    40       52       47  46.333333
5     Sara    88       93       90  90.333333
6   Ishaan    64       70       66  66.666667
7   Ananya    95       92       89  92.000000
8   Vivaan    48       57       51  52.000000
9     Tara    83       76       85  81.333333
10   Arjun    67       63       72  67.333333
11   Nisha    74       81       79  78.000000
12     Dev    35       45       42  40.666667
13   Priya    89       86       91  88.666667
14   Kunal    58       54       60  57.333333
15    Riya    92       90       96  92.666667
16      Om    61       69       65  65.000000
17   Aditi    80       85       83  82.666667
18    Yash    43       49       46  46.000000
19   Sneha    77       73       80  76.666667
    student_id    name  age     city  math  science  english  \
4          105   Rohan   17   Mumbai    40       52       47   
8          109  Vivaan   17   Mumbai    48       57       51   
12         113     Dev   17   Mumbai    35       45       42   
18         119    Yash   17  Mathura    43       49       46   

    attendance_percent  study_hours_per_week  assignments_submitted  \
4                   68                     3                      5   
8                   71                     4                      6   
12                  62                     2                      4   
18                  66                     3                      5   

    final_project_score    average  
4                    45  46.333333  
8                    55  52.000000  
12                   39  40.666667  
18                   48  46.000000  

import pandas as pd
df = pd.read_csv("session4_dummy_students_data.csv.xls")
df["average"] = (df["math"] + df["science"] + df["english"]) / 3
df["result"] = df["average"].apply(lambda x: "Pass" if x > 40 else "Fail")
print("Class Average:", df["average"].mean())
subjects = ["math", "science", "english"]
for subject in subjects:
    print(f"\n{subject.upper()}")
    print("Highest:", df[subject].max())
    print("Lowest :", df[subject].min())
top_score = df["average"].max()
top_students = df[df["average"] == top_score]
print("\nTop Student(s):")
print(top_students[["name", "average"]])
print("\nAttendance Below 75:")
print(df[df["attendance_percent"] < 75][["name", "attendance_percent"]])
print("\nAssignments Submitted < 6:")
print(df[df["assignments_submitted"] < 6][["name", "assignments_submitted"]])
     
Class Average: 71.35000000000001

MATH
Highest: 95
Lowest : 35

SCIENCE
Highest: 93
Lowest : 45

ENGLISH
Highest: 96
Lowest : 42

Top Student(s):
    name    average
15  Riya  92.666667

Attendance Below 75:
      name  attendance_percent
4    Rohan                  68
8   Vivaan                  71
12     Dev                  62
18    Yash                  66

Assignments Submitted < 6:
     name  assignments_submitted
4   Rohan                      5
12    Dev                      4
18   Yash                      5

import pandas as pd
df = pd.read_csv("session4_dummy_students_data.csv.xls")
df['average']=df[['math','science','english']].mean()
result=[]
for avg in df['average']:
    if avg>=40:
        result.append('Pass')
    else:
        result.append('Fail')
df['result']=result
print(df)

total=df['average'].sum()
students=len(df)
class_average=total/students
print('Class Average:',class_average)
     
    student_id    name  age     city  math  science  english  \
0          101   Aarav   16   Mumbai    78       84       69   
1          102    Diya   16    Delhi    91       88       94   
2          103   Kabir   17  Mathura    55       61       58   
3          104   Meera   16    Noida    72       79       81   
4          105   Rohan   17   Mumbai    40       52       47   
5          106    Sara   16    Delhi    88       93       90   
6          107  Ishaan   17  Mathura    64       70       66   
7          108  Ananya   16    Noida    95       92       89   
8          109  Vivaan   17   Mumbai    48       57       51   
9          110    Tara   16    Delhi    83       76       85   
10         111   Arjun   17  Mathura    67       63       72   
11         112   Nisha   16    Noida    74       81       79   
12         113     Dev   17   Mumbai    35       45       42   
13         114   Priya   16    Delhi    89       86       91   
14         115   Kunal   17  Mathura    58       54       60   
15         116    Riya   16    Noida    92       90       96   
16         117      Om   17   Mumbai    61       69       65   
17         118   Aditi   16    Delhi    80       85       83   
18         119    Yash   17  Mathura    43       49       46   
19         120   Sneha   16    Noida    77       73       80   

    attendance_percent  study_hours_per_week  assignments_submitted  \
0                   92                     8                      9   
1                   96                    11                     10   
2                   75                     5                      6   
3                   89                     7                      8   
4                   68                     3                      5   
5                   97                    10                     10   
6                   82                     6                      7   
7                   94                    12                     10   
8                   71                     4                      6   
9                   90                     9                      9   
10                  80                     6                      8   
11                  88                     8                      8   
12                  62                     2                      4   
13                  95                    10                     10   
14                  77                     5                      6   
15                  98                    13                     10   
16                  79                     6                      7   
17                  91                     9                      9   
18                  66                     3                      5   
19                  87                     8                      8   

    final_project_score  average result  
0                    82      NaN   Fail  
1                    93      NaN   Fail  
2                    60      NaN   Fail  
3                    78      NaN   Fail  
4                    45      NaN   Fail  
5                    95      NaN   Fail  
6                    69      NaN   Fail  
7                    91      NaN   Fail  
8                    55      NaN   Fail  
9                    86      NaN   Fail  
10                   70      NaN   Fail  
11                   80      NaN   Fail  
12                   39      NaN   Fail  
13                   92      NaN   Fail  
14                   63      NaN   Fail  
15                   96      NaN   Fail  
16                   68      NaN   Fail  
17                   84      NaN   Fail  
18                   48      NaN   Fail  
19                   79      NaN   Fail  
Class Average: 0.0

import pandas as pd

df = pd.read_csv("session4_dummy_students_data.csv.xls")  # Replace with your file name
print(df.head())
     
   student_id   name  age     city  math  science  english  \
0         101  Aarav   16   Mumbai    78       84       69   
1         102   Diya   16    Delhi    91       88       94   
2         103  Kabir   17  Mathura    55       61       58   
3         104  Meera   16    Noida    72       79       81   
4         105  Rohan   17   Mumbai    40       52       47   

   attendance_percent  study_hours_per_week  assignments_submitted  \
0                  92                     8                      9   
1                  96                    11                     10   
2                  75                     5                      6   
3                  89                     7                      8   
4                  68                     3                      5   

   final_project_score  
0                   82  
1                   93  
2                   60  
3                   78  
4                   45
