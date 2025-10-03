# Game777game
Hangman Game 
import streamlit as st
import random

palavras = ["perfume", "banana", "python", "computador", "praia", "tenis"]


if "palavra" not in st.session_state:
    st.session_state.palavra = random.choice(palavras)
    st.session_state.letras = []
    st.session_state.tentativas = 6

palavra = st.session_state.palavra
letras = st.session_state.letras
tentativas = st.session_state.tentativas


palavra_formada = "".join([letra if letra in letras else "*" for letra in palavra])

st.title("🎮 Jogo da Forca")
st.write(f"Palavra: {palavra_formada}")
st.write(f"Tentativas restantes: {tentativas}")


letra = st.text_input("Digite uma letra: ").lower()

if st.button("Enviar letra"):
    if letra and letra not in letras:
        letras.append(letra)
        if letra not in palavra:
            st.session_state.tentativas -= 1


if palavra_formada == palavra:
    st.success("🎉 Você ganhou!")
    if st.button("Jogar novamente"):
        st.session_state.clear()

elif st.session_state.tentativas == 0:
    st.error(f"💀 Você perdeu! A palavra era: {palavra}")
    if st.button("Jogar novamente"):
        st.session_state.clear()
