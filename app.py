from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load ML model
with open('car_price_model.pkl', 'rb') as f:
    model = pickle.load(f)  

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form
    Car_Name = data['Car_Name']
    Year = int(data['Year'])
    Present_Price = float(data['Present_Price'])
    Kms_Driven = int(data['Kms_Driven'])
    Fuel_Type = data['Fuel_Type']
    Seller_Type = data['Seller_Type']
    Transmission = data['Transmission']
    Owner = int(data['Owner'])

    input_df = pd.DataFrame([[Car_Name, Year, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission,Owner]],
                                columns=['Car_Name', 'Year', 'Present_Price', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission','Owner'])

    prediction = model.predict(input_df)[0]
    output = round(prediction, 2)

    return render_template('index.html', prediction_text=f"Estimated Selling Price: ₹ {output} Lakhs")

if __name__ == '__main__':
    app.run(debug=True)
