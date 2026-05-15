# Heart Disease Prediction System

A Machine Learning-based web application that predicts the likelihood of heart disease based on patient medical information.

This project uses patient health parameters such as age, cholesterol, blood pressure, chest pain type, heart rate, and other medical indicators to predict whether a person has heart disease.

The project is designed for **educational, demonstration, and portfolio purposes** to showcase machine learning workflows, healthcare prediction systems, and model deployment concepts.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Dataset Information](#dataset-information)
- [Dataset Structure](#dataset-structure)
- [Target Variable](#target-variable)
- [Tech Stack](#tech-stack)
- [Machine Learning Workflow](#machine-learning-workflow)
- [Recommended Models](#recommended-models)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Sample Prediction](#sample-prediction)
- [Model Evaluation](#model-evaluation)
- [Future Improvements](#future-improvements)
- [Disclaimer](#disclaimer)
- [License](#license)

---

## Overview

Heart disease is one of the major causes of death worldwide. Early prediction of heart disease can help improve treatment planning and reduce health risks.

This project applies **Machine Learning Classification Algorithms** to analyze patient health data and predict whether a person is likely to have heart disease.

The system can be used as:

- A Machine Learning Demo Project
- A Healthcare Analytics Project
- A Portfolio Project
- A Binary Classification Case Study
- A Beginner-Friendly Medical Prediction System

---

## Features

- Heart disease prediction using patient health data
- Data preprocessing pipeline
- Exploratory Data Analysis (EDA)
- Machine learning model training
- Model evaluation and performance metrics
- Binary classification prediction
- Scalable architecture for future deployment
- Clean and modular implementation

---

## Dataset Information

| Feature | Value |
|----------|--------|
| Dataset Name | Heart Disease Dataset |
| Dataset Type | Structured CSV |
| Number of Rows | 1025 |
| Number of Columns | 14 |
| Problem Type | Binary Classification |
| Target Variable | `target` |

---

## Dataset Structure

The dataset contains the following medical attributes:

| Column Name | Description |
|-------------|-------------|
| `age` | Age of the patient |
| `sex` | Gender (1 = Male, 0 = Female) |
| `cp` | Chest pain type |
| `trestbps` | Resting blood pressure |
| `chol` | Serum cholesterol level |
| `fbs` | Fasting blood sugar > 120 mg/dl |
| `restecg` | Resting electrocardiographic results |
| `thalach` | Maximum heart rate achieved |
| `exang` | Exercise-induced angina |
| `oldpeak` | ST depression induced by exercise |
| `slope` | Slope of peak exercise ST segment |
| `ca` | Number of major vessels |
| `thal` | Thalassemia result |
| `target` | Heart disease prediction |

---

## Target Variable

The `target` column represents the prediction label.

| Value | Meaning |
|--------|----------|
| `1` | Heart Disease Present |
| `0` | No Heart Disease |

---

## Tech Stack

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Joblib

### Development Tools
- Jupyter Notebook / VS Code
- Git & GitHub

---

## Machine Learning Workflow

The project follows a standard machine learning workflow:

```text
Data Collection
        ↓
Data Cleaning
        ↓
Data Preprocessing
        ↓
Exploratory Data Analysis (EDA)
        ↓
Feature Engineering
        ↓
Train-Test Split
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Prediction
```

---

## Recommended Models

The following machine learning algorithms can be used:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Naive Bayes
- Gradient Boosting
- XGBoost

---

## Project Structure

```text
heart-disease-prediction/
│
├── data/
│   └── heart_disease.csv
│
├── notebook/
│   └── heart_disease_prediction.ipynb
│
├── model/
│   └── trained_model.pkl
│
├── main.py
├── requirements.txt
├── README.md
│
└── assets/
    └── screenshots
```

---

## Requirements

Before running the project, ensure the following software is installed.

### Software Requirements

- Python 3.10+
- pip
- Virtual Environment (`venv`)
- Git

### Python Dependencies

Install dependencies manually:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib
```

Or install using:

```bash
pip install -r requirements.txt
```

---

## Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/heart-disease-prediction.git
```

### 2. Move to Project Directory

```bash
cd heart-disease-prediction
```

### 3. Create Virtual Environment

Windows:

```bash
python -m venv venv
```

Mac/Linux:

```bash
python3 -m venv venv
```

### 4. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Requirements File

Create a `requirements.txt` file:

```txt
pandas
numpy
matplotlib
seaborn
scikit-learn
joblib
```

Generate automatically:

```bash
pip freeze > requirements.txt
```

---

## Usage

### Run Python Script

```bash
python main.py
```

### Run Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
heart_disease_prediction.ipynb
```

---

## Sample Prediction

Example patient data:

```python
sample_patient = [[52, 1, 0, 125, 212, 0, 1, 168, 0, 1.0, 2, 2, 3]]

prediction = model.predict(sample_patient)

print(prediction)
```

Output:

```text
[1]
```

Meaning:

```text
Heart Disease Present
```

---

## Model Evaluation

Common evaluation metrics used:

- Accuracy Score
- Precision
- Recall
- F1 Score
- Confusion Matrix
- ROC-AUC Score

Example:

```text
Model Accuracy: 87%
```

---

## Future Improvements

Possible enhancements:

- Add advanced feature engineering
- Improve prediction accuracy
- Deploy using Django/FastAPI
- Build React frontend UI
- Add authentication system
- Add patient prediction history
- Deploy to AWS/Render

---

## Disclaimer

This project is intended for:

- Educational purposes
- Learning Machine Learning concepts
- Demonstration projects
- Portfolio showcase

This system **must not be used for real medical diagnosis or treatment decisions**.

Always consult a healthcare professional for medical advice.

---

## License

This project is licensed for **educational and demonstration purposes**.

---

## Author

**Anamika M**

Full Stack Web Developer | Aspiring Machine Learning Engineer

Passionate about building intelligent web applications using Machine Learning, Django, React, and Python.