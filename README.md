# 🎓 Student Performance Predictor

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20App-000000)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E)](https://scikit-learn.org/)
[![CatBoost](https://img.shields.io/badge/CatBoost-Model-FFCC00)](https://catboost.ai/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED)](https://www.docker.com/)
[![AWS Elastic Beanstalk](https://img.shields.io/badge/AWS-Elastic%20Beanstalk-FF9900)](https://aws.amazon.com/elasticbeanstalk/)

An end-to-end machine learning web application that predicts a student's **math score** from demographic and academic inputs. The project covers the full workflow: exploratory analysis, data transformation, model training, artifact persistence, and real-time inference through a Flask web interface, with Docker and AWS Elastic Beanstalk deployment support.

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Input Features](#-input-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Model Training](#-model-training)
- [Deployment](#-deployment)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

## 🔎 Overview

Understanding which factors influence academic performance helps educators identify students who may need additional support. This project trains a regression model on student exam data and serves it through a simple web form: enter a student's details and receive a predicted math score instantly.

The training logic is separated from the serving logic. Fitted preprocessing and model objects are saved as artifacts (`preprocessor.pkl`, `model.pkl`) and reloaded by a prediction pipeline, which guarantees that new inputs are transformed exactly as the training data was.

## ✨ Features

- **Complete ML pipeline** – data ingestion, transformation, model training, and evaluation
- **Consistent preprocessing** – encoding and scaling handled by a persisted preprocessor
- **Multi-model comparison** – candidate regressors evaluated to select the best performer (CatBoost is among the libraries used)
- **Real-time predictions** via a Flask web interface
- **Custom exception handling and logging** for easier debugging
- **Deployment ready** – includes a `Dockerfile` and AWS Elastic Beanstalk configuration (`.ebextensions/`, `application.py`)
- **Notebooks** for EDA and model experimentation

## 🧾 Input Features

| Feature | Type | Description |
|---|---|---|
| `gender` | Categorical | Student's gender |
| `race_ethnicity` | Categorical | Ethnicity group |
| `parental_level_of_education` | Categorical | Highest education level of parent(s) |
| `lunch` | Categorical | Standard or free/reduced lunch |
| `test_preparation_course` | Categorical | Whether the course was completed |
| `reading_score` | Numeric | Reading exam score |
| `writing_score` | Numeric | Writing exam score |

**Target:** `math_score`

## 🧰 Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.8+ |
| Web Framework | Flask |
| ML | scikit-learn, CatBoost |
| Data | pandas, numpy |
| Frontend | HTML, CSS (Jinja2 templates) |
| Persistence | Pickle / dill-style serialization |
| Deployment | Docker, AWS Elastic Beanstalk |

## 📂 Project Structure

```
Student_Performance_Predictor/
├── .ebextensions/          # AWS Elastic Beanstalk configuration
├── artifacts/              # Saved model, preprocessor, and data splits
├── catboost_info/          # CatBoost training logs
├── notebook/               # EDA and model-training notebooks
├── src/
│   ├── components/         # Data ingestion, transformation, model trainer
│   ├── pipeline/           # Training and prediction pipelines
│   ├── exception.py        # Custom exception handling
│   ├── logger.py           # Logging configuration
│   └── utils.py            # Helper functions (save/load objects, evaluation)
├── templates/              # HTML templates (home, result)
├── app.py                  # Flask app entry point
├── application.py          # Flask app entry point for Elastic Beanstalk
├── Dockerfile              # Container definition
├── requirements.txt        # Dependencies
├── setup.py                # Package setup
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Madhavkumaryadav/Student_Performance_Predictor.git
cd Student_Performance_Predictor

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
python application.py
```

Open **http://127.0.0.1:5000** in your browser.

## 🧪 Usage

1. Open the app in your browser.
2. Navigate to the prediction form (`/predictor`).
3. Fill in gender, ethnicity, parental education, lunch type, test-preparation status, reading score and writing score.
4. Click **Predict** to see the estimated math score, rounded to two decimals.

## 📦 Model Training

Training is performed in the following stages:

1. **Data ingestion** – load the dataset and create train/test splits
2. **Data transformation** – impute missing values, one-hot encode categorical features, scale numeric features
3. **Model training** – fit and compare several regressors, then keep the best-performing model
4. **Artifact saving** – store `preprocessor.pkl` and `model.pkl` in `artifacts/`

At prediction time, `PredictPipeline` loads these artifacts and applies the same transformations to the user's input before predicting.

To retrain, run the training pipeline script or the notebooks in `notebook/`.

## ☁️ Deployment

**Docker**

```bash
docker build -t student-performance-predictor .
docker run -p 5000:5000 student-performance-predictor
```

**AWS Elastic Beanstalk**

The repository includes `application.py` (exposing the `application` object Elastic Beanstalk expects) and an `.ebextensions/` folder for environment configuration.

```bash
eb init
eb create student-performance-env
eb deploy
```

## 🗺️ Roadmap

- [ ] Display model metrics (R², MAE, RMSE) in the README or UI
- [ ] Add input validation and friendly error messages
- [ ] Add feature-importance / explainability view
- [ ] Add unit tests and a CI pipeline
- [ ] Add a REST API endpoint for programmatic predictions
- [ ] Add screenshots and a live demo link

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push and open a Pull Request

Bug reports and ideas can be submitted through [Issues](https://github.com/Madhavkumaryadav/Student_Performance_Predictor/issues).

## 📄 License

Distributed under the MIT License. Add a `LICENSE` file to the repository to make this official.

## 👤 Author

**Madhav Kumar Yadav**
GitHub: [@Madhavkumaryadav](https://github.com/Madhavkumaryadav)

---

⭐ If you found this project helpful, please consider starring the repository.
