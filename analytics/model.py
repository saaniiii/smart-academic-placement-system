import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from collections import Counter

# -----------------------------
# TRAIN MODEL
# -----------------------------
def train_model(df):

    df["skills_count"] = df["skills"].apply(lambda x: len(str(x).split(",")))

    X = df[["cgpa", "attendance_percent", "skills_count"]]
    y = df["status"].apply(lambda x: 1 if x == "Placed" else 0)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    cm = confusion_matrix(y_test, y_pred, labels=[0, 1])

    return model, accuracy, cm


# -----------------------------
# SKILL GAP ANALYZER
# -----------------------------
def skill_gap_analysis(df, student_skills):

    placed_df = df[df["status"] == "Placed"]

    all_skills = []

    for skills in placed_df["skills"]:
        split_skills = [s.strip() for s in skills.split(",")]
        all_skills.extend(split_skills)

    skill_frequency = Counter(all_skills)

    top_skills = [skill for skill, count in skill_frequency.most_common(5)]

    student_skill_list = [s.strip() for s in student_skills.split(",")]

    missing_skills = [
        skill for skill in top_skills if skill not in student_skill_list
    ]

    return top_skills, missing_skills


# -----------------------------
# PLACEMENT READINESS SCORE
# -----------------------------
def calculate_readiness_score(model, cgpa, attendance, skills_count):

    probability = model.predict_proba([[cgpa, attendance, skills_count]])[0][1]

    cgpa_score = (cgpa / 10) * 30
    attendance_score = (attendance / 100) * 20
    skills_score = (skills_count / 10) * 30
    model_score = probability * 20

    total_score = cgpa_score + attendance_score + skills_score + model_score

    return round(total_score, 2)

def recommend_skills(df):

    placed_students = df[df["status"] == "Placed"]

    skills_list = placed_students["skills"].dropna().tolist()

    all_skills = []

    for skills in skills_list:
        split_skills = [skill.strip() for skill in skills.split(",")]
        all_skills.extend(split_skills)

    skill_series = pd.Series(all_skills)

    top_skills = skill_series.value_counts().head(5)

    return top_skills