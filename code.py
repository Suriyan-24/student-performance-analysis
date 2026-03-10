import numpy as np
import pandas as pd

# Weights for each factor (importance of each metric)
weights = np.array([0.25, 0.20, 0.15, 0.15, 0.05, 0.05, 0.10, 0.05])

# Grade calculation
def get_grade(score):
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B+"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "D"

# Student category
def categorize_student(score):
    if score >= 90:
        return "All-round Achiever"
    elif score >= 80:
        return "Creative Performer"
    elif score >= 70:
        return "Hardworking Student"
    elif score >= 60:
        return "Average Learner"
    else:
        return "Needs Guidance"

# Suggestions based on input metrics
def suggest_improvements(iq, attention, attendance, study_hours, extracurricular, games, sports, leisure):

    suggestions = []

    if iq < 100:
        suggestions.append("Consider brain training or cognitive exercises to improve reasoning ability.")

    if attention < 6:
        suggestions.append("Improve attention span using focused study sessions or mindfulness techniques.")

    if attendance < 75:
        suggestions.append("Increase class attendance to improve understanding of lessons.")

    if study_hours < 15:
        suggestions.append("Increase weekly study hours to strengthen subject knowledge.")

    if extracurricular < 2:
        suggestions.append("Participate in extracurricular activities for better creativity and soft skills.")

    if games < 1:
        suggestions.append("Play strategic games like chess to develop critical thinking.")

    if sports < 1:
        suggestions.append("Engage in sports for physical health and discipline.")

    if leisure > 8:
        suggestions.append("Reduce leisure time and balance it with productive study activities.")

    if not suggestions:
        suggestions.append("All metrics look good. Maintain your current balance and keep progressing.")

    return " | ".join(suggestions)


# -------------------- USER INPUT --------------------

print("\nEnter the following student details:\n")

iq = float(input("IQ (example 90 - 140): "))
attention = float(input("Attention Span (1 - 10 scale): "))
attendance = float(input("Class Attendance %: "))
study_hours = float(input("Study Hours per week: "))
extracurricular = float(input("Extracurricular hours per week: "))
games = float(input("Strategic games hours per week: "))
sports = float(input("Sports hours per week: "))
leisure = float(input("Leisure hours per week: "))

# -------------------- NORMALIZATION --------------------

attention_norm = (attention / 10) * 100

inputs = np.array([
    iq,
    attention_norm,
    attendance,
    study_hours * 4,
    extracurricular * 10,
    games * 10,
    sports * 10,
    leisure * 10
])

# -------------------- SCORE CALCULATION --------------------

score = np.dot(inputs, weights)
score = round(score, 2)

grade = get_grade(score)
category = categorize_student(score)

suggestions = suggest_improvements(
    iq, attention, attendance, study_hours,
    extracurricular, games, sports, leisure
)

# -------------------- OUTPUT TABLE --------------------

data = {
    "Metric": [
        "IQ",
        "Attention Span (1-10)",
        "Class Attendance (%)",
        "Study Hours/week",
        "Extracurricular hrs/week",
        "Strategic Games hrs/week",
        "Sports hrs/week",
        "Leisure hrs/week"
    ],
    "Value": [
        iq,
        attention,
        attendance,
        study_hours,
        extracurricular,
        games,
        sports,
        leisure
    ]
}

df = pd.DataFrame(data)

df.loc[len(df)] = ["Estimated Score", score]
df.loc[len(df)] = ["Grade", grade]
df.loc[len(df)] = ["Category", category]
df.loc[len(df)] = ["Suggestions", suggestions]

print("\nStudent Academic Performance Summary\n")
print(df.to_string(index=False))
