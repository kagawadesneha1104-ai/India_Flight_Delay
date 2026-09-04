from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load model
with open('flight_delay_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load training dataset
df = pd.read_csv('dataset/india_flight_delay_model_input.csv')

# Same preprocessing used during training
df['Flight_Date'] = pd.to_datetime(df['Flight_Date'])
df['Year'] = df['Flight_Date'].dt.year
df['Day'] = df['Flight_Date'].dt.day

df.drop(['Flight_Date', 'Flight_Number'], axis=1, inplace=True)

X = df.drop(['Delay_Target', 'Departure_Delay'], axis=1)

categorical_columns = [
    'Airline',
    'Origin_Airport',
    'Destination_Airport',
    'Weather'
]

# Save categories from training data
categories = {}

for col in categorical_columns:
    categories[col] = sorted(df[col].dropna().unique())

# Encode training data
X = pd.get_dummies(
    X,
    columns=categorical_columns,
    drop_first=True
)

X = X.astype(float)

# Save exact feature columns
feature_columns = X.columns


@app.route('/')
def home():
    return "Flight Delay Prediction API is Running!"


@app.route('/data')
def data():
    return "Flight Delay Prediction API Data Endpoint!"


@app.route('/status')
def status():
    return "Flight Delay Prediction API is Running Successfully!"


@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json()

    input_df = pd.DataFrame([data])

    # Date processing
    input_df['Flight_Date'] = pd.to_datetime(input_df['Flight_Date'])
    input_df['Year'] = input_df['Flight_Date'].dt.year
    input_df['Day'] = input_df['Flight_Date'].dt.day

    input_df.drop(['Flight_Date', 'Flight_Number'], axis=1, inplace=True)

    # IMPORTANT:
    # Use training categories for encoding
    for col in categorical_columns:
        input_df[col] = pd.Categorical(
            input_df[col],
            categories=categories[col]
        )

    # Same encoding as training
    input_df = pd.get_dummies(
        input_df,
        columns=categorical_columns,
        drop_first=True
    )

    # Make columns exactly same as training
    input_df = input_df.reindex(
        columns=feature_columns,
        fill_value=0
    )

    input_df = input_df.astype(float)

    prediction = model.predict(input_df)

    return jsonify({
        "prediction": float(prediction[0])
    })


if __name__ == '__main__':
    app.run(debug=True)