Diabetes Prediction System

This project is a Machine Learning-based web application designed to predict the likelihood of diabetes in patients based on medical attributes. It combines data preprocessing, model training, and an interactive web interface to deliver real-time predictions.

🚀 Features

Cleaned and preprocessed diabetes dataset.

Machine Learning model trained and saved as regressor_model.pkl.

Web interface built using Flask to input patient details and view predictions.

Modular codebase (model.py for training, diabeties_pred.py for serving).

Easy to extend and retrain with updated datasets.

🛠️ Tech Stack

Languages: Python

Libraries: Pandas, NumPy, Scikit-learn, Flask, Pickle

Frontend: HTML templates (Flask Jinja2)

Dataset: Diabetes_cleaned.csv

📂 Project Structure
diabeties_Project/
│── Diabetes_cleaned.csv       # Dataset  
│── model.py                   # ML model training script  
│── regressor_model.pkl        # Saved model  
│── diabeties_pred.py          # Flask web app  
│── templates/                 # HTML templates for UI  

💡 How to Run

Clone the repository

git clone https://github.com/yourusername/diabeties_Project.git
cd diabeties_Project


Install dependencies

pip install -r requirements.txt


Run the Flask app

python diabeties_pred.py


Open http://127.0.0.1:5000 in your browser.
