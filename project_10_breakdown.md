
# 🧠 Project 10: Resume Job Matcher

This project predicts the most suitable job role from a resume summary using a TF-IDF vectorizer and Logistic Regression model.

---

## 🧭 Phase-by-Phase Breakdown

### 🔹 Phase 1: Dataset Creation
- 50 sample resume summaries
- 5 job roles: Data Analyst, Frontend Developer, Backend Developer, Project Manager, ML Engineer
- File: `resume_job_dataset.csv`

---

### 🔹 Phase 2: Vectorization
- Text preprocessing with `TfidfVectorizer`
- Converts each resume summary into a numerical feature vector

---

### 🔹 Phase 3: Model Training
- Model: Logistic Regression (multi-class)
- Trained with 80/20 train-test split
- File: `resume_model.joblib`

---

### 🔹 Phase 4: Evaluation
- Evaluated on accuracy, precision, recall, and F1-score
- Some imbalance and low scores due to small dataset size

---

### 🔹 Phase 5: Streamlit App
- Input: Resume summary text area
- Output: Predicted job role
- File: `app/resume_match_app.py`

---

### 🔹 Phase 6: Hugging Face Deployment
- `README.md` for auto-launch
- `requirements.txt` for dependencies
- Zipped for upload

---

### 🔹 Phase 7: GitHub Packaging
- GitHub-friendly ZIP created with all components

---

## 🎯 Core Summary

| Component        | Description                          |
|------------------|--------------------------------------|
| Dataset          | `resume_job_dataset.csv`             |
| Model            | `LogisticRegression`                 |
| Vectorizer       | `TfidfVectorizer`                    |
| Deployment       | Streamlit + Hugging Face             |
| ZIPs             | `resume_job_matcher.zip`, `*_github.zip` |

---

## ✅ Ideal For
- Resume parsing
- Job recommendation systems
- HR Tech Demos
