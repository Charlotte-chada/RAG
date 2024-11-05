import streamlit as st
import pandas as pd
import numpy as np
import time
import pickle

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

st.title('Real-Time Machine Failure Prediction (Simulated Data)')

# Simulate real-time data input (replace this with real data when available)
def get_simulated_data():
    # Simulating random values within a reasonable range
    data = {
        'Air temperature [K]': np.random.uniform(290, 310),
        'Process temperature [K]': np.random.uniform(300, 320),
        'Rotational speed [rpm]': np.random.uniform(1200, 1500),
        'Torque [Nm]': np.random.uniform(30, 50),
        'Tool wear [min]': np.random.uniform(0, 300)
    }
    return pd.DataFrame([data])

# Simulate real-time data updates
while True:
    # Get simulated data
    data = get_simulated_data()

    st.write("Real-Time Data Input (Simulated):")
    st.write(data)

    # Make predictions based on real-time simulated data
    prediction = model.predict(data)

    # Display the prediction
    st.write(f'Prediction (0 = No Failure, 1 = Failure): {prediction[0]}')

    # Add a condition for an alert
    if prediction[0] == 1:
        st.error("Warning: Machine Failure Predicted!")
    else:
        st.success("Machine is running normally.")

    # Wait for 5 seconds to simulate real-time prediction updates
    time.sleep(5)
