import streamlit as st

st.title("Calculadora de IMC")

peso = st.number_input("Digite seu peso (kg):", min_value=0.0, step=0.1)
altura = st.number_input("Digite sua altura (m):", min_value=0.0, step=0.01)

if peso > 0 and altura > 0:
    imc = peso / (altura ** 2)
    st.write(f"Seu IMC é: {imc:.2f}")
    if imc < 18.5:
        st.warning("Você está abaixo do peso.")
        st.write(imc)
    elif 18.5 <= imc <= 24.9:
        st.success("Você está no peso ideal.")
        st.write(imc)
    else:
        st.error("Você está acima do peso.")
        st.write(imc)
