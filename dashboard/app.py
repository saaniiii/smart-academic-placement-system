import streamlit as st
import pandas as pd
import sys
import os
import mysql.connector
import matplotlib.pyplot as plt

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from analytics.model import (
    train_model,
    skill_gap_analysis,
    calculate_readiness_score,
    recommend_skills
)

# -----------------------------
# MYSQL CONNECTION
# -----------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sani2006",
    database="smart_placement"
)

cursor = conn.cursor()

st.set_page_config(page_title="Smart Placement System", layout="wide")

st.title("🎓 Smart Academic Placement Intelligence System")

# -----------------------------
# LOAD DATA FROM MYSQL
# -----------------------------
query = "SELECT * FROM students_data"
df = pd.read_sql(query, conn)

# -----------------------------
# METRICS
# -----------------------------
col1, col2, col3 = st.columns(3)

total_students = len(df)
placed_students = len(df[df["status"] == "Placed"])
placement_rate = round((placed_students / total_students) * 100, 2)

col1.metric("Total Students", total_students)
col2.metric("Placed Students", placed_students)
col3.metric("Placement Rate (%)", placement_rate)

st.divider()

# -----------------------------
# SHOW DATASET
# -----------------------------
st.subheader("📚 Student Dataset")

st.dataframe(df)

st.divider()

# -----------------------------
# PLACEMENT TREND
# -----------------------------
st.subheader("📊 Placement Trend")

placement_counts = df["status"].value_counts()

st.bar_chart(placement_counts)

st.divider()

# -----------------------------
# STUDENTS AT RISK
# -----------------------------
st.subheader("⚠ Students At Risk")

df["skills_count"] = df["skills"].apply(lambda x: len(str(x).split(",")))

at_risk = df[(df["cgpa"] < 6.5) & (df["skills_count"] < 3)]

st.dataframe(at_risk)

st.divider()

# -----------------------------
# TRAIN MODEL
# -----------------------------
model, accuracy, cm = train_model(df)

st.subheader("📊 Model Performance")
st.write(f"Model Accuracy: {round(accuracy * 100, 2)}%")

if len(cm) > 1:
    st.subheader("🔎 Confusion Matrix")

    st.write("True Negatives:", cm[0][0])
    st.write("False Positives:", cm[0][1])
    st.write("False Negatives:", cm[1][0])
    st.write("True Positives:", cm[1][1])

st.divider()

# -----------------------------
# PREDICTION INPUT
# -----------------------------
st.subheader("🔮 Predict Placement")

cgpa = st.slider("CGPA", 5.0, 10.0, 7.0)
attendance = st.slider("Attendance %", 50, 100, 75)
skills = st.slider("Number of Skills", 1, 10, 3)

if st.button("Predict Placement"):

    prediction = model.predict([[cgpa, attendance, skills]])

    prob = model.predict_proba([[cgpa, attendance, skills]])[0][1]

    score = calculate_readiness_score(model, cgpa, attendance, skills)

    result = "Placed" if prediction[0] == 1 else "Not Placed"

    st.subheader("📈 Placement Readiness Score")

    st.progress(int(score))

    st.write(f"Readiness Score: {score}/100")

    st.subheader("🎯 Placement Probability")

    st.progress(int(prob * 100))

    st.write(f"Placement Probability: {round(prob*100,2)}%")

    if prediction[0] == 1:
        st.success("High chances of Placement ✅")
    else:
        st.error("Low chances of Placement ❌")

    # SAVE PREDICTION
    query = """
    INSERT INTO predictions
    (cgpa, attendance, skills_count, score, prediction, time)
    VALUES (%s,%s,%s,%s,%s,NOW())
    """

    values = (cgpa, attendance, skills, score, result)

    cursor.execute(query, values)

    conn.commit()

    st.success("Prediction saved to database")

st.divider()

# -----------------------------
# SKILL GAP ANALYZER
# -----------------------------
st.subheader("🧠 Skill Gap Analyzer")

student_skills_input = st.text_input(
    "Enter your skills (comma separated)",
    "Python, SQL"
)

if st.button("Analyze Skill Gap"):

    top_skills, missing_skills = skill_gap_analysis(df, student_skills_input)

    st.write("🔥 Top Skills Among Placed Students:", top_skills)

    if missing_skills:
        st.warning("📌 Skills to Improve:")
        st.write(missing_skills)
    else:
        st.success("🎉 You already match top skillset!")

st.divider()

# -----------------------------
# PREDICTION HISTORY
# -----------------------------
st.subheader("📚 Prediction History")

cursor.execute("SELECT * FROM predictions ORDER BY time DESC")

rows = cursor.fetchall()

history_df = pd.DataFrame(
    rows,
    columns=["ID", "CGPA", "Attendance", "Skills", "Score", "Prediction", "Time"]
)

st.dataframe(history_df)

st.divider()

# -----------------------------
# ANALYTICS CHARTS
# -----------------------------
st.subheader("📊 Placement Analytics")

fig1, ax1 = plt.subplots()

df["status"].value_counts().plot(kind="bar", ax=ax1)

ax1.set_title("Placement Distribution")

st.pyplot(fig1)

fig2, ax2 = plt.subplots()

placed = df[df["status"] == "Placed"]
not_placed = df[df["status"] == "Not Placed"]

ax2.scatter(placed["cgpa"], placed["attendance_percent"], label="Placed")
ax2.scatter(not_placed["cgpa"], not_placed["attendance_percent"], label="Not Placed")

ax2.set_xlabel("CGPA")
ax2.set_ylabel("Attendance")
ax2.legend()

st.pyplot(fig2)

st.divider()

# -----------------------------
# SKILL RECOMMENDATION ENGINE
# -----------------------------
st.subheader("🚀 Skill Recommendation Engine")

top_skills = recommend_skills(df)

st.write("🔥 Most Valuable Skills for Placement")

st.bar_chart(top_skills)

st.divider()

# -----------------------------
# RECRUITER DASHBOARD
# -----------------------------
st.header("🏢 Placement Officer Dashboard")

df["skills_count"] = df["skills"].apply(lambda x: len(str(x).split(",")))

st.subheader("⭐ Top Performing Students")

top_students = df.sort_values(
    by=["cgpa", "skills_count", "attendance_percent"],
    ascending=False
).head(10)

st.dataframe(top_students)

st.subheader("⚠ Students Needing Training")

training_students = df[
    (df["cgpa"] < 6.5) | (df["skills_count"] < 3)
]

st.dataframe(training_students)

st.subheader("🔥 Most Demanded Skills")

all_skills = []

for skill_list in df["skills"]:
    for skill in str(skill_list).split(","):
        all_skills.append(skill.strip())

skill_series = pd.Series(all_skills)

top_skill_counts = skill_series.value_counts().head(10)

st.bar_chart(top_skill_counts)