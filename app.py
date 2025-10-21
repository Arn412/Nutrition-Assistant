import streamlit as st
from classifier import predict_food_label
from nutrition_api import fetch_nutrition

st.title("Food Calorie & Nutrition Estimator")

img_file = st.file_uploader("Upload a food image", type=["jpg", "jpeg", "png"])
grams = st.slider("Select portion size (in grams)", min_value=50, max_value=500, value=100, step=50)

if img_file:
    with open("temp.jpg", "wb") as f:
        f.write(img_file.read())

    label = predict_food_label("temp.jpg")
    st.write(f"**Predicted food:** `{label}`")

    nutrients = fetch_nutrition(label, grams=grams)

    if nutrients:
        st.write("**Nutritional Info (per selected grams):**")
        st.json(nutrients)
    else:
        st.warning("⚠️ Nutrition data not found for the predicted label.")
