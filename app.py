# app.py
import streamlit as st
import requests

st.title("AI Image Generator")

prompt = st.text_input("Enter your prompt:")

if st.button("Generate Image"):
    if prompt:
        # Replace with your actual API endpoint and key
        api_url = "https://api.example.com/generate"
        response = requests.post(api_url, json={"prompt": prompt})
        
        if response.status_code == 200:
            image_url = response.json().get("image_url")
            st.image(image_url, caption="Generated Image")
        else:
            st.error("Failed to generate image")
    else:
        st.warning("Please enter a prompt")
