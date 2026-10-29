import streamlit as st

st.set_page_config(
    page_title="Mi primera app",
    page_icon="🚀",
    layout="centered"
)

st.title("🚀 Mi primera aplicación")
st.write("Bienvenido a mi aplicación desplegada con Streamlit.")

st.divider()

# Formulario
st.subheader("Formulario de usuario")

nombre = st.text_input("¿Cómo te llamas?")
edad = st.number_input(
    "¿Cuántos años tienes?",
    min_value=0,
    max_value=120,
    value=18
)

if st.button("Enviar"):
    if nombre.strip():
        st.success(f"¡Hola, {nombre}!")
        st.write(f"Tu edad es: {edad} años.")
    else:
        st.warning("Por favor, introduce tu nombre.")

st.divider()

# Calculadora
st.subheader("Calculadora")

a = st.number_input("Primer número", value=10.0)
b = st.number_input("Segundo número", value=5.0)

operacion = st.selectbox(
    "Operación",
    ["Suma", "Resta", "Multiplicación", "División"]
)

if st.button("Calcular"):
    if operacion == "Suma":
        resultado = a + b
    elif operacion == "Resta":
        resultado = a - b
    elif operacion == "Multiplicación":
        resultado = a * b
    else:
        resultado = a / b if b != 0 else None

    if resultado is None:
        st.error("No se puede dividir entre cero.")
    else:
        st.metric("Resultado", resultado)