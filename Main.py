import random
import pandas as pd

results=[]
for x in range(100000):

    StudentID=random.randint(10000000,90000000)
    print("Student ID Number:", StudentID)
    M1_Score=random.randint(0,100)
    print(M1_Score)
    attendance=random.randint(0,100)
    print(attendance)
    Hw=random.randint(0,100)
    print(Hw)
    M2_Score=random.randint(0,100)
    print(M2_Score)
    Finalexam=random.randint(0,100)
    print(Finalexam)
    Finalgrade=0.16*M1_Score+0.16*M2_Score+0.40*Finalexam+0.05*attendance+0.23*Hw
    print(Finalgrade)
    # implemented all grades for course, need to figure out how to compute the average score
    # and return the result as a letter grade (A 93, B 83, etc)-use if statements for that
    if Finalgrade>94:
        Lettergrade="A"
    elif 89.00 < Finalgrade < 93.99:
        Lettergrade="A-"
    elif Finalgrade > 83.00 and Finalgrade<88.99:
        Lettergrade="B+"
    elif Finalgrade > 79.00 and Finalgrade < 82.99:
        Lettergrade = "B"
    elif Finalgrade > 74 and Finalgrade<78.99:
        Lettergrade="B-"
    elif Finalgrade > 69 and Finalgrade<73.99:
        Lettergrade="C+"
    elif Finalgrade > 64 and Finalgrade<68.99:
        Lettergrade="C"
    elif Finalgrade > 59.00 and Finalgrade<63.99:
        Lettergrade="C-"
    elif Finalgrade > 55.00 and Finalgrade<58.99:
        Lettergrade="D"
    else:
        Lettergrade="F"

# top and bottom scorers 12/10/2024
# Number of each grade: A, B,C.....



    results.append({
        "Student ID Number": StudentID,
        "Midterm 1 Score": M1_Score,
        "Midterm 2 Score": M2_Score,
        "HW Score ": Hw,
        "Attendance/Participation": attendance,
        "Final Exam Score": Finalexam,
        "Overall Percentage": Finalgrade,
        "Course letter grade":Lettergrade,

    })

df = pd.DataFrame(results)
df.to_excel("chem1a_results.xlsx", index=False)
print("Scores saved to 'chem 1a_results.xlsx'")

