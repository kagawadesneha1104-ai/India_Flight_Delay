# ✈️ India Flight Delay Prediction

A Machine Learning project that predicts flight delay using flight schedule, airline, airport, weather, congestion, previous flight delay, and turnaround risk information.

## 📌 Project Overview

Flight delays can occur due to various factors such as weather conditions, airport congestion, previous flight delays, and turnaround risk.

This project uses Machine Learning to predict the `Delay_Target` for Indian flights. The trained model is integrated with a Flask REST API and tested using Postman.

## 🎯 Objective

- Analyze flight delay data
- Perform data cleaning and preprocessing
- Perform Exploratory Data Analysis (EDA)
- Select relevant features
- Encode categorical variables
- Train a Machine Learning model
- Evaluate model performance
- Save the trained model using Pickle
- Build a Flask REST API
- Test the API using Postman
- Deploy the application using Render

## 📊 Dataset

The dataset contains flight-related information such as:

- Airline
- Flight Number
- Origin Airport
- Destination Airport
- Scheduled Departure Time
- Day of Week
- Month
- Weekend Indicator
- Peak Hour
- Weather
- Temperature
- Humidity
- Wind Speed
- Visibility
- Rainfall
- Cloud Cover
- Origin Congestion Index
- Previous Flight Delay
- Turnaround Risk Index

### Target Variable

`Delay_Target`

The target variable represents the flight delay status.

## 🤖 Machine Learning

### Model Used

**Linear Regression**

### Preprocessing Steps

1. Data Cleaning
2. Date Feature Extraction
3. Feature Selection
4. One-Hot Encoding
5. Train-Test Split
6. Model Training
7. Prediction
8. Model Evaluation

## 📈 Model Performance

| Metric | Score |
|--------|------:|
| MAE | 0.2001 |
| MSE | 0.0832 |
| RMSE | 0.2885 |
| R² Score | 0.2805 |

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Flask
- Postman
- Google Colab
- Visual Studio Code
- Git
- GitHub
- Render

## 📁 Project Structure

India_Flight_Delay/
│
├── dataset/
│   └── india_flight_delay_model_input.csv
│
├── documentation/
│   └── India_Flight_Delay_Report.pdf
│
├── notebook/
│   └── India_Flight_Delay.ipynb
│
├── presentation/
│   └── India_Flight_Delay_Presentation.pptx
│
├── screenshots/
│   ├── actual_vs_predicted.png
│   ├── correlation_heatmap.png
│   ├── postman_prediction.png
│   ├── previous_flight_vs_departure_delay.png
│   └── render_deployment.png
│
├── .gitignore
├── app.py
├── flight_delay_model.pkl
├── README.md
└── requirements.txt
```

## 🌐 Flask API

The trained Machine Learning model is integrated with a Flask REST API.

### Home Endpoint

    GET /

Response:

    Flight Delay Prediction API is Running!

### Prediction Endpoint

    POST /predict

The `/predict` endpoint accepts flight details in JSON format and returns the predicted delay target.

### Example Request

    {
        "Flight_Date": "2024-04-03",
        "Airline": "Air India",
        "Flight_Number": 0,
        "Origin_Airport": "BOM",
        "Destination_Airport": "GWL",
        "Scheduled_Departure_Hour": 22,
        "Scheduled_Departure_Minute": 2,
        "Day_of_Week": 2,
        "Month": 4,
        "Is_Weekend": 0,
        "Peak_Hour": 0,
        "Weather": "Clear/Partly Cloudy",
        "Temperature_C": 29.1,
        "Humidity_pct": 64.7,
        "Wind_Speed_kmh": 0.8,
        "Visibility_km": 10.9,
        "Rainfall_mm": 0.0,
        "Cloud_Cover_pct": 28.1,
        "Origin_Congestion_Index": 51.6,
        "Previous_Flight_Delay_Minutes": 29,
        "Turnaround_Risk_Index": 48.3
    }

### Example Response

    {
        "prediction": 0.8712641439479869
    }

## ▶️ How to Run Locally

### 1. Clone the Repository

    git clone https://github.com/kagawadesneha1104-ai/India_Flight_Delay.git

### 2. Navigate to the Project

    cd India_Flight_Delay

### 3. Install Dependencies

    pip install -r requirements.txt

### 4. Run the Flask Application

    python app.py

### 5. Open in Browser

    http://127.0.0.1:5000

## 🧪 API Testing

The Flask REST API was tested using Postman.

The `/predict` endpoint was tested using a POST request with JSON input, and the trained Machine Learning model successfully returned the prediction.


## 🚀 Deployment

The Flask application is successfully deployed on Render and tested using Postman.

**Live API:** https://india-flight-delay.onrender.com

**Build Command**
```bash
pip install -r requirements.txt
```

**Start Command**
```bash
gunicorn app:app
```

## 🔄 Project Workflow

    Dataset
       ↓
    Data Preprocessing
       ↓
    Exploratory Data Analysis
       ↓
    Feature Engineering
       ↓
    One-Hot Encoding
       ↓
    Train-Test Split
       ↓
    Linear Regression
       ↓
    Model Evaluation
       ↓
    Pickle Model
       ↓
    Flask API
       ↓
    Postman Testing
       ↓
    GitHub
       ↓
    Render Deployment

## 👩‍💻 Author

**Sneha Kagawade**

MCA – Data Science

GitHub: https://github.com/kagawadesneha1104-ai