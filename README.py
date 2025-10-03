# Game777game
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
