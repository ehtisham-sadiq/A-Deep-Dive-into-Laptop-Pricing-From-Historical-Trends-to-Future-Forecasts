# Modify the Streamlit app to include the Flask Monitoring Dashboard
import streamlit as st
import pandas as pd
import joblib 

# Load the model and Column_Transformer
model  = joblib.load('model/finalized_model')
preprocessor = joblib.load('model/column_Transfomer')

def preprocess_input(data):
    preprocessed_data = preprocessor.transform(data)
    return preprocessed_data

# Define the app
st.title('Laptop Price Predictor')
st.write('This app predicts the price of a laptop based on its specifications.')

# Create input form for user to enter laptop specs
company = st.selectbox('Company', ['Acer', 'Apple', 'Asus', 'Dell', 'HP', 'Lenovo', 'MSI', 'Microsoft', 'Razer', 'Toshiba','Samsung'])
typename = st.selectbox('Type', ['Gaming', 'Notebook', 'Ultrabook', 'Netbook',' Workstation','2 in 1 Convertible'])
gpu_brand = st.selectbox('GPU Brand', ['AMD', 'Intel', 'Nvidia'])
os = st.selectbox('Operating System', ['Android', 'Chrome OS', 'Linux', 'Mac OS', 'No OS', 'Windows'])
cpu_brand = st.selectbox('CPU Brand', ['Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'AMD Processor', 'Other Intel Processor'])
touchscreen = st.slider('Touchscreen', 0, 1)
ips = st.slider('IPS Screen',0,1)
ram = st.sidebar.number_input('RAM (GB)', min_value=2, max_value=64, value=8, step=2)
weight = st.sidebar.number_input('Weight (kg)', min_value=0.5, max_value=5.0, value=2.0, step=0.1)
ppi = st.sidebar.number_input('PPI (pixels per inch)', min_value=50, max_value=500, value=200, step=10)
hdd = st.sidebar.number_input('HDD (GB)', min_value=0, max_value=2000, value=500, step=10)
ssd = st.sidebar.number_input('SSD (GB)', min_value=0, max_value=2000, value=256, step=10)
hybrid = st.sidebar.number_input('Hybrid Drive Capacity (in GB)', min_value= 0, max_value= 200, step=10)
flash_storage = st.sidebar.number_input('Flash Storage Capacity (in GB)', min_value=0, max_value = 100, step=10)



# Store user inputs as a dictionary
user_input = {'company': company, 'typename': typename, 'ram': ram, 'weight': weight, 'gpu_brand': gpu_brand,
                'os': os, 'cpu_brand': cpu_brand, 'touchscreen': touchscreen, 'ips': ips, 'ppi': ppi, 'HDD': hdd,
                'SSD': ssd, 'Hybrid': hybrid, 'Flash_Storage': flash_storage}

user_input_df = pd.DataFrame(user_input, index=[0])

# Preprocess the input
preprocessed_input = preprocess_input(user_input_df)

prediction = model.predict(preprocessed_input)[0]

# Display the predicted price to the user
st.subheader('Predicted Price')
st.write(f'Rs. {prediction:.2f}')
# Display the predicted price to the user
# st.write('The predicted price of this laptop is $', round(prediction[0], 2))
