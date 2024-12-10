import streamlit as st

st.title("Operación de suma")

st.write("Esta aplicacion realiza la suma de dos números")

num1 = 0
num2 = 0


num1 = st.text_input("Ingrese el primer número")
num2 = st.text_input("Ingrese el segundo número")

if num1.isdigit() and num2.isdigit():
    suma = int(num1) + int(num2)
    st.write(f"La suma de {num1} y {num2} es {suma}")
else:
    st.write("Por favor, ingrese solo números enteros.")