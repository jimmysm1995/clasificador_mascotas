import streamlit as st
import pandas as pd
import joblib
import json

st.title("Classipet")
st.write("Clasificador de mascotas. Introduzca los datos de su mascota y le diremos a que clase pertenece.")
st.image("img/pets_images.jpg", use_container_width=True)

# Carga el modelo
model = joblib.load("model/pets_model.joblib")
with open("model/category_mappings.json", "r") as f:
    category_mapping = json.load(f)

# Extrae los valores categóricos
eye_color_values = category_mapping["eye_color"]
fur_length_values = category_mapping["fur_length"]

# Pide los datos de la mascota
weight = st.number_input("Peso (kg)", min_value=0.0, max_value=100.0, value=0.0)
height = st.number_input("Altura (cm)", min_value=0.0, max_value=100.0, value=0.0)
eye_color = st.selectbox("Color de ojos", ["Azul", "Marrón", "Gris", "Verde"])
fur_lenght = st.selectbox("Largo del pelo", ["Largo", "Medio", "Corto"])

# Mapea la seleccion de color de ojos y largo del pelo al español
eye_color_map = {"Azul": "blue", "Marrón": "brown", "Gris": "gray", "Verde": "green"}
fur_length_map = {"Largo": "long", "Medio": "medium", "Corto": "short"}

selected_eye_color = eye_color_map[eye_color]
selected_fur_length = fur_length_map[fur_lenght]

# Genera las columnas binarias para el color de ojos y largo del pelo
eye_color_binary = [int(color == selected_eye_color) for color in eye_color_values]
fur_length_cols = [int(length == selected_fur_length) for length in fur_length_values]

# Crear el dataframe con los datos de la mascota
input_data = [weight, height] + eye_color_binary + fur_length_cols
columns = (["weight_kg", "height_cm"] +
           [f"eye_color_{color}" for color in eye_color_values] +
           [f"fur_length_{length}" for length in fur_length_values])
input_df = pd.DataFrame([input_data], columns=columns)

# Realiza la predicción
if st.button("Clasificar mascota"):
    prediction = model.predict(input_df)[0]
    prediction_map = {"dog": "Perro", "cat": "Gato", "rabbit": "Conejo"}
    st.success(f"La mascota es un {prediction_map[prediction]}", icon="🐶")

