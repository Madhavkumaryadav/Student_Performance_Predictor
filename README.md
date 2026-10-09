#### END TO END DATA SCIENCE PROJECT #### 

# Student Performance Prediction Web App

This is an **end-to-end Machine Learning web application** that predicts a student’s **math score** based on demographic and academic features like gender, race/ethnicity, parental education, lunch type, test preparation course status, and reading & writing scores.

It uses a **trained ML model + Flask web interface** to make real-time predictions from user inputs.

---

## 📌 Table of Contents

1. 📘 Project Overview  
2. 🧩 Features  
3. 🛠️ Tech Stack  
4. 🗂️ Project Structure  
5. 🚀 How to Run Locally  
6. 🧪 Usage  
7. 📦 Model Training and Prediction  
8. ❤️ Contributions  
9. 📄 License

---

## 📘 Project Overview

This repository contains a complete ML pipeline — from loading and processing the data, training a model, saving transformation and model artifacts (`preprocessor.pkl`, `model.pkl`), to building a **Flask app** that exposes a prediction interface. The prediction form takes user input, processes it the same way as training data, and outputs a prediction.

---

## 🧩 Features

✔️ Data preprocessing (encoding, scaling, handling missing values)  
✔️ Trained regression model to predict student performance  
✔️ Web UI with HTML forms to input data  
✔️ Real-time score prediction via Flask  
✔️ Custom exception handling and pipeline structure  
✔️ Clean directory layout for training & deployment

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Flask** — backend web server  
- **scikit-learn** — ML model & preprocessing  
- **pandas, numpy** — data handling  
- **HTML/CSS** — frontend templates  
- **Pickle** — model persistence

---

## 🗂️ Project Structure

ML_Project_1/
│
├── artifacts/ # Saved trained model & preprocessing
│ ├── model.pkl
│ └── preprocessor.pkl
├── notebook/ # EDA / Training notebooks
├── src/
│ ├── pipeline/
│ │ ├── predict_pipeline.py
│ │ └── (training pipeline scripts if any)
│ ├── exception.py
│ └── utils.py
├── templates/
│ ├── index.html
│ └── (other HTML files)
├── app.py # Flask backend
├── requirements.txt
├── setup.py
└── README.md



---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Madhavkumaryadav/ML_Project_1.git
cd ML_Project_1python -m venv venv

Activate Virtual environement :
Windows: venv\Scripts\activate
macOS/Linux: source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Flask App
python app.py


Then open your browser and go to:

http://127.0.0.1:5000

Usage
Open browser
Enter student details (gender, race_ethnicity, parental education, etc.)
Click “Predict”
See the predicted math score
📦 Model Training & Retraining (Optional)
If training script exists in this repo (train_pipeline.py / notebook):
Perform preprocessing → transformation
Train best model
Save artifacts to artifacts/
The Flask app uses these .pkl files to make predictions
The PredictPipeline class loads these artifacts and performs consistent transformation and prediction.
❤️ Contributing


Contributions are welcome!
If you want to:

✔ Fix bugs
✔ Improve interface
✔ Add model performance metrics
✔ Extend CI/CD or deployment

…please open an issue or pull request.
