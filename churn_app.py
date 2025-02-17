import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('churn_model.pkl', 'rb'))

# Input fields for features
age = st.number_input("Age", min_value=18, max_value=100)
account_type = st.selectbox("Account Type", ["Basic", "Premium"])
monthly_usage = st.slider("Monthly Usage", min_value=0, max_value=500)

# Convert categorical input to numeric if necessary
account_type_numeric = 0 if account_type == "Basic" else 1

# Prepare input data for prediction
input_data = np.array([age, account_type_numeric, monthly_usage]).reshape(1, -1)

# Predict when the button is clicked
if st.button("Predict"):
    prediction = model.predict(input_data)  # Model prediction
    if prediction[0] == 1:
        st.write("Customer will churn!")
    else:
        st.write("Customer will not churn!")




'''import streamlit as st
import pickle
import numpy as np
import joblib

# Load the trained model
model = pickle.load(open("churn_model.pkl", "rb"))

# Streamlit UI
st.title("Customer Churn Prediction App")
st.write("Enter customer details below to predict if they will churn.")

# User Inputs
tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, max_value=200.0, value=50.0)
total_charges = st.number_input("Total Charges", min_value=0.0, max_value=10000.0, value=500.0)

# Predict Button
if st.button("Predict"):
    input_data = np.array([[tenure, monthly_charges, total_charges]])
    prediction = model.predict(input_data)
    result = "Churn" if prediction[0] == 1 else "Not Churn"
    st.write(f"Prediction: **{result}**")
'''