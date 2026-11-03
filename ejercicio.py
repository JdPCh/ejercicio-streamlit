import streamlit as st

st.set_page_config(page_title="Conversor de temperatura")

UNIDADES = ["Celsius", "Fahrenheit", "Kelvin"]
SIMBOLOS = {"Celsius": "C", "Fahrenheit": "F", "Kelvin": "K"}


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


st.session_state.setdefault("origen", "Celsius")
st.session_state.setdefault("destino", "Fahrenheit")
st.session_state.setdefault("valor", 0.0)


def intercambiar():
    st.session_state.origen, st.session_state.destino = (
        st.session_state.destino,
        st.session_state.origen,
    )

st.title("Conversor de temperatura")
st.caption("Convierte entre Celsius, Fahrenheit y Kelvin.")

col1, col2, col3 = st.columns([5, 2, 5])
with col1:
    st.selectbox("Unidad de origen", UNIDADES, key="origen")
with col2:
    st.write("")
    st.write("")
    st.button("Intercambiar", on_click=intercambiar, use_container_width=True)
with col3:
    st.selectbox("Unidad de destino", UNIDADES, key="destino")

st.number_input("Temperatura", step=0.1, format="%.2f", key="valor")

origen = st.session_state.origen
destino = st.session_state.destino
valor = st.session_state.valor

celsius = a_celsius(valor, origen)

if round(celsius, 9) < -273.15:
    st.error("La temperatura ingresada esta por debajo del cero absoluto.")
else:
    resultado = desde_celsius(celsius, destino)

    st.metric(
        label=f"{valor:.2f} {origen}",
        value=f"{resultado:.2f} {SIMBOLOS[destino]}",
    )

    with st.expander("Ver todas las conversiones"):
        for u in UNIDADES:
            st.write(f"{u}: {desde_celsius(celsius, u):.2f} {SIMBOLOS[u]}")
