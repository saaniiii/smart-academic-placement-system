import pandas as pd
import mysql.connector
import os

# -----------------------------
# LOAD DATASET
# -----------------------------

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, "data", "students.csv")

df = pd.read_csv(file_path)

# -----------------------------
# TRANSFORM DATA
# -----------------------------

df["skills_count"] = df["skills"].apply(lambda x: len(str(x).split(",")))

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

# -----------------------------
# LOAD DATA INTO MYSQL
# -----------------------------

for _, row in df.iterrows():

    query = """
    INSERT INTO students_data
    (name, cgpa, attendance_percent, skills, skills_count, status)
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    values = (
        row["name"],
        row["cgpa"],
        row["attendance_percent"],
        row["skills"],
        row["skills_count"],
        row["status"]
    )

    cursor.execute(query, values)

conn.commit()

print("ETL Pipeline Completed Successfully")