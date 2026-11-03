import streamlit as st

st.set_page_config(page_title="Conversor de temperatura")

st.title("Conversor de temperatura")

unidades = ["Celsius", "Fahrenheit", "Kelvin"]


def a_celsius(valor, unidad):
    if unidad == "Celsius":
        return valor
    if unidad == "Fahrenheit":
        return (valor - 32) * 5 / 9
    return valor - 273.15


def desde_celsius(valor, unidad):
    if unidad == "Celsius":
        return valor
    if unidad == "Fahrenheit":
        return valor * 9 / 5 + 32
    return valor + 273.15


col1, col2 = st.columns(2)
with col1:
    origen = st.selectbox("Unidad de origen", unidades, index=0)
with col2:
    destino = st.selectbox("Unidad de destino", unidades, index=1)

valor = st.number_input("Temperatura", value=0.0, step=0.1, format="%.2f")

celsius = a_celsius(valor, origen)

if celsius < -273.15:
    st.error("La temperatura ingresada esta por debajo del cero absoluto.")
else:
    resultado = desde_celsius(celsius, destino)
    st.subheader("Resultado")
    st.write(f"{valor:.2f} {origen} = {resultado:.2f} {destino}")

    with st.expander("Ver todas las conversiones"):
        for u in unidades:
            st.write(f"{u}: {desde_celsius(celsius, u):.2f}")
