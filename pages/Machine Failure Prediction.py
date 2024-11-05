import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load your trained model (ensure you saved it beforehand)
model = pickle.load(open('model.pkl', 'rb'))

# Define the mapping for Type
mapping = {'L': 0, 'M': 1, 'H': 2}

# User input for prediction
st.image("banner.png", use_column_width=True)
st.title("🔧Machine Failure Prediction App")

# Example user inputs (you can replace these with Streamlit widgets)
air_temp = st.number_input('Air temperature [K]', min_value=0.0, max_value=500.0, value=300.0)
process_temp = st.number_input('Process temperature [K]', min_value=0.0, max_value=500.0, value=300.0)
rot_speed = st.number_input('Rotational speed [rpm]', min_value=0.0, max_value=3000.0, value=100.0)
torque = st.number_input('Torque [Nm]', min_value=0.0, max_value=500.0, value=200.0)
tool_wear = st.number_input('Tool wear [min]', min_value=0.0, max_value=500.0, value=100.0)
type_input = st.selectbox('Machine Type', ['L', 'M', 'H'])

# Encode the machine type based on the mapping
type_encoded = mapping[type_input]

# Prepare the data for prediction
data = pd.DataFrame({
    'Air temperature [K]': [air_temp],
    'Process temperature [K]': [process_temp],
    'Rotational speed [rpm]': [rot_speed],
    'Torque [Nm]': [torque],
    'Tool wear [min]': [tool_wear],
    'Type_encoded': [type_encoded]
})

# Display the input data
st.write("Input data:")
st.write(data)

# List of failure mode columns
failure_modes = ['TWF', 'HDF', 'PWF', 'OSF', 'RNF']

# Make prediction when the user clicks the button
if st.button('Predict Machine Failure'):
    prediction = model.predict(data)
    
    # Check if any failure is predicted
    if prediction[0][-1] == 1:  # Assuming 'Machine failure' is the last column in your prediction
        st.write('Machine Failure Detected!')
        
        # Find which specific failure modes were predicted
        failure_detected = [failure for i, failure in enumerate(failure_modes) if prediction[0][i] == 1]
        
        if failure_detected:
            st.write(f'Failure Mode(s): {", ".join(failure_detected)}')
        else:
            st.write('No specific failure modes detected.')
    else:
        st.write('No Machine Failure Detected.')
