# 🎓 Smart Academic Placement Prediction System

An **AI-powered academic analytics platform** that predicts student placement probability, analyzes skill gaps, and provides actionable recommendations to improve placement readiness.

This project combines **Machine Learning, Data Engineering, Analytics, and Interactive Dashboards** to simulate a real-world **placement intelligence system used by universities**.

---

# 🚀 Project Overview

The **Smart Academic Placement System** helps students and institutions:

• Predict placement chances using Machine Learning
• Analyze skill gaps between placed and non-placed students
• Recommend in-demand industry skills
• Track prediction history using a database
• Visualize placement analytics through an interactive dashboard
• Analyze resumes and extract skills automatically

The system provides **data-driven insights to improve student employability**.

---

# 🧠 Key Features

## 1️⃣ Placement Prediction Model

* Logistic Regression ML model
* Predicts placement chances based on:

  * CGPA
  * Attendance
  * Skills Count

## 2️⃣ Placement Readiness Score

* Calculates a **placement readiness score out of 100**
* Visualized with a progress indicator

## 3️⃣ Skill Gap Analyzer

* Compares student skills with **top skills among placed students**
* Identifies **missing skills required for placement**

## 4️⃣ Skill Recommendation Engine

* Recommends **most valuable skills based on placed student data**

## 5️⃣ Placement Analytics Dashboard

Interactive visualizations:

* Placement distribution
* CGPA vs Attendance patterns
* Skills vs Placement correlation

## 6️⃣ Resume Analyzer (AI Feature)

* Upload resume
* Extract skills automatically
* Compare skills with industry demand

## 7️⃣ Prediction History Storage

* Stores predictions in **MySQL database**
* Maintains historical analytics

## 8️⃣ ETL Data Pipeline

* Extracts student data
* Transforms skill features
* Loads processed data into MySQL database

---

# 🏗️ System Architecture

```
Student Data (CSV)
        │
        ▼
ETL Pipeline (Python + Pandas)
        │
        ▼
MySQL Database
        │
        ▼
Machine Learning Model
(Logistic Regression)
        │
        ▼
Streamlit Dashboard
        │
        ├── Placement Prediction
        ├── Skill Gap Analysis
        ├── Analytics Visualization
        └── Resume Analyzer
```

---

# 🛠️ Tech Stack

### Programming

* Python

### Data Science

* Pandas
* NumPy
* Scikit-learn

### Visualization

* Matplotlib
* Streamlit

### Database

* MySQL

### Data Engineering

* ETL Pipeline (Python)

### AI Feature

* Resume Skill Extraction

---

# 📂 Project Structure

```
smart_academic_placement_system
│
├── analytics
│   └── model.py
│
├── dashboard
│   └── app.py
│
├── pipeline
│   └── etl_pipeline.py
│
├── resume_analyzer
│   └── analyzer.py
│
├── data
│   └── students.csv
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/smart-academic-placement-system.git
cd smart-academic-placement-system
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows:

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Run the Streamlit dashboard:

```bash
streamlit run dashboard/app.py
```

Open in browser:

```
http://localhost:8501
```

---

# 🗄️ Database Setup

Create database in MySQL:

```sql
CREATE DATABASE smart_placement;
```

Create prediction table:

```sql
CREATE TABLE predictions (
id INT AUTO_INCREMENT PRIMARY KEY,
cgpa FLOAT,
attendance INT,
skills_count INT,
score FLOAT,
prediction VARCHAR(20),
time TIMESTAMP
);
```

---

# 📊 Example Dashboard Features

The dashboard displays:

✔ Total Students
✔ Placement Rate
✔ Placement Prediction Model Accuracy
✔ Skill Gap Analysis
✔ Skill Recommendation Engine
✔ Placement Analytics Graphs

---

# 📈 Machine Learning Model

Algorithm used:

**Logistic Regression**

Features used for prediction:

| Feature      | Description                   |
| ------------ | ----------------------------- |
| CGPA         | Academic performance          |
| Attendance   | Student attendance percentage |
| Skills Count | Number of technical skills    |

Output:

**Placement Probability**

---

# 🔮 Future Improvements

Possible upgrades:

• Deep Learning placement prediction model
• NLP-based resume analysis using spaCy or Transformers
• Job role recommendation engine
• Integration with LinkedIn job data
• Student performance tracking over semesters
• Real-time placement analytics

---

# 👨‍💻 Author

**Sani Jain**

Computer Science Engineering Student
Interested in **Data Engineering, AI, and Analytics Systems**

---

# ⭐ If you like this project

Give the repository a **star ⭐ on GitHub**
