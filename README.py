# Game777game
import streamlit as st
import random

palavras = ["perfume", "banana", "python", "computador", "praia", "tenis"].lower().upper()

def reset_game():
    st.session_state.palavra = random.choice(palavras)
    st.session_state.letras = []
    st.session_state.tentativas = 6

if "palavra" not in st.session_state:
    reset_game()

palavra = st.session_state.palavra
letras = st.session_state.letras
tentativas = st.session_state.tentativas

st.title("🎮 Jogo da Forca")

letra = st.text_input("Digite uma letra: ").lower()
if st.button("Enviar letra"):
    if letra and letra not in letras:
        letras.append(letra)
        if letra not in palavra:
            st.session_state.tentativas -= 1

palavra_formada = "".join([l if l in letras else "*" for l in palavra])

st.write(f"Palavra: {palavra_formada}")
st.write(f"Tentativas restantes: {st.session_state.tentativas}")

if palavra_formada == palavra:
    st.success("🎉 Você ganhou!")
    if st.button("Jogar novamente"):
        reset_game()

elif st.session_state.tentativas == 0:
    st.error(f"💀 Você perdeu! A palavra era: {palavra}")
    if st.button("Jogar novamente"):
        reset_game()
