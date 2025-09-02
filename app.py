import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("model.pkl")

# Page setup
st.set_page_config(page_title="House Price Prediction", page_icon="🏡", layout="wide")

st.title("🏡 House Price Prediction App")
st.write("Fill in the details of the house to estimate its price.")

# --- INPUT FORM ---
st.sidebar.header("House Features")

Square_Footage = st.sidebar.number_input("Square_Footage", min_value=0.0, step=1.0)
Num_Bedrooms = st.sidebar.number_input("Num_Bedrooms", min_value=0.0, step=1.0)
Num_Bathrooms = st.sidebar.number_input("Num_Bathrooms", min_value=0.0, step=1.0)
Year_Built = st.sidebar.number_input("Year_Built", min_value=0.0, step=1.0)
Lot_Size = st.sidebar.number_input("Lot_Size", min_value=0.0, step=1.0)
Garage_Size = st.sidebar.number_input("Garage_Size", min_value=0.0, step=1.0)
Neighborhood_Quality = st.sidebar.number_input("Neighborhood_Quality", min_value=0.0, step=1.0)


features = np.array([[Square_Footage, Num_Bedrooms, Num_Bathrooms, Year_Built, Lot_Size, Garage_Size, Neighborhood_Quality]])

# Prediction
if st.sidebar.button("🔮 Predict Price"):
    prediction = model.predict(features)
    st.success(f"Estimated House Price: ${prediction[0]:,.2f}")


