import pandas as pd
import numpy as np
import streamlit as st
import datetime
import pickle

cars_df = pd.read_csv("./cars24.csv")

st.write(
    """
    # Cars24 Used car Price Prediction 
    """
)

st.dataframe(cars_df.head())

col1, col2 = st.columns(2)

Fuel_type = col1.selectbox("Select the fuel type", [
                        "Diesel", "Petrol", "CNG", "LPG", "Electric"])

Engine = col1.slider("Set the Engine Power", 500, 5000, step=100)

Transmission_box = col2.selectbox(
    "Select the Transmission Type", ["Manual", "Automatic"])

Seats = col2.selectbox("Select the number of seats", [2, 4, 5, 6, 7, 8, 11])


encode_dict = {
    "Fuel_Type": {"Diesel": 1, "Petrol": 2, "CNG": 3, "LPG": 4, "Electric": 5},
    "Seller_Type": { "Dealer": 1, "Individual": 2, "Trustmark Dealer": 3},
    "Transmission_box": {"Manual": 1, "Automatic": 2},
}


def model_prediction(Fuel_type, Transmission_box, Engine, Seats):
    # loading the model
    with open("car_pred", "rb") as file:
        reg_model = pickle.load(file)
    input_features = [[2018.0, 1, 4000, Fuel_type, Transmission_box, 19.70, \
                        Engine, 86.30, Seats]]
    return reg_model.predict(input_features)


if st.button("Predict Price"):
    Fuel_type1 = encode_dict["Fuel_Type"][Fuel_type]
    Transmission_box1 = encode_dict["Transmission_box"][Transmission_box]

    Price = model_prediction(Fuel_type1, Transmission_box1, Engine, Seats)

    st.text(f"The Price of the car is {Price.round(2)} lakhs rupees.")

st.text("The model is predicting the price of the car...")
