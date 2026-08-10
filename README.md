# 🩺 Diabetes Prediction AI

### An AI-powered web application for diabetes risk prediction

<p align="center">
  <strong>Built with Python • TensorFlow • Streamlit</strong>
</p>

---

## 🌟 Overview

**Diabetes Prediction AI** is a machine learning web application designed to predict diabetes risk based on patient health information.

The application provides an easy-to-use interface where users can enter patient data and receive an AI-based prediction with its probability.

> ⚠️ **Disclaimer:** This project is for educational purposes only and is not a medical diagnosis tool.

---

## ✨ Features

* 🧑‍⚕️ Patient information input
* 🧠 Neural Network prediction model
* 📊 Prediction probability
* 🖥️ Interactive Streamlit interface
* ⚡ Fast predictions
* 📦 Saved preprocessing pipeline
* 🎨 Clean and responsive UI

---

## 🛠️ Technologies

| Technology            | Usage                |
| --------------------- | -------------------- |
| 🐍 Python             | Programming          |
| 🧠 TensorFlow / Keras | Neural Network       |
| 📊 Pandas             | Data Processing      |
| 🔢 NumPy              | Numerical Operations |
| ⚙️ Scikit-learn       | Preprocessing        |
| 🎨 Streamlit          | Web Application      |
| 💾 Joblib             | Model Preprocessing  |

---

## 📋 Input Features

The application uses patient information such as:

* Gender
* Age
* BMI
* HbA1c Level
* Blood Glucose Level
* Hypertension
* Heart Disease
* Race
* Smoking History

---

## 🧠 Model

The prediction system uses a trained **Neural Network** model.

The preprocessing pipeline includes:

```text
Raw Patient Data
       ↓
Data Encoding
       ↓
Feature Alignment
       ↓
Standard Scaling
       ↓
Neural Network
       ↓
Prediction Probability
       ↓
Diabetes / No Diabetes
```

---

## 🚀 Run the Project

### 1️⃣ Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2️⃣ Navigate to the project

```bash
cd Diabetes-Prediction
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Streamlit

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```text
Diabetes-Prediction/
│
├── app.py
├── diabetes_model.h5
├── scaler.pkl
├── feature_columns.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🎯 Prediction Result

The application displays one of two results:

### 🟢 No Diabetes Detected

The predicted probability is below the selected classification threshold.

### 🔴 Diabetes Detected

The predicted probability reaches or exceeds the classification threshold.

---

## 📸 Application Preview

Add a screenshot of the Streamlit application here:

```markdown
![Diabetes Prediction App](screenshot.png)
```

---

## 👩‍💻 Author

**Sola Mohamed**

Computer Science & Artificial Intelligence Student

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐
