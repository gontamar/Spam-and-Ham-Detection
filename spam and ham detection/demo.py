import streamlit as st
import joblib

st.title("SPAM HAM CLASSIFIER")   #title for the webapp

# Use raw string or forward slashes for the file path
text_model = joblib.load(r'D:\samp and ham detection\spam') 
# Or
# text_model = joblib.load('C:/Users/pavan/OneDrive/Desktop/samp and ham detection/spam') 

ip = st.text_input("Enter the message :")     #Input message
op = text_model.predict([ip])                 # use the model for predicting the output
if st.button('Predict'):  
    st.title(op[0])