import streamlit as st

# Configuração da página
st.set_page_config(page_title="7 Anos de Loucura", page_icon="🤣")

# Estilização
st.markdown("""
    <style>
    .main { background-color: #0b0e14; }
    .titulo {
        font-size: 38px;
        font-weight: 800;
        color: #00FF7F;
        text-align: center;
        margin-bottom: 20px;
    }
    .card-historia {
        background: rgba(255, 255, 255, 0.07);
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #00FF7F;
        color: #ffffff;
        font-size: 18px;
        line-height: 1.6;
        text-align: justify;
    }
    .destaque { color: #00FF7F; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.balloons()

st.markdown("<h1 class='titulo'>7 ANOS DE HISTÓRIA, FIOTA! 🎈</h1>", unsafe_allow_html=True)

# O TEXTO LONGO E PERSONALIZADO
st.markdown(f"""
<div class='card-historia'>
    Se a gente fosse escrever um livro desses 7 anos, o povo ia achar que é ficção, porque olha... quanta história! <br><br>
    
    Eu lembro até hoje de cada fase, inclusive daquela época dos seus <span class='destaque'>namoradinhos</span>. E quem diria, hein? Você namorando o viado e ainda por cima metendo um <span class='destaque'>web irmão</span> no meio! KKKKKKK. Só a gente sabe o quanto a gente já riu dessas bizarrices que só a internet proporciona. <br><br>
    
    Mas o que ficou de verdade foram as nossas <span class='destaque'>partidas</span>, aquelas <span class='destaque'>calls de 24h, 48h</span> seguidas... Onde a gente não só jogava, mas dividia a vida, falava merda e passava o tempo do jeito que só a gente sabe. <br><br>
    
    Nesses 7 anos, eu vi você crescer, mas a essência de ser essa pessoa foda nunca mudou. Você é incrível, fiota. Obrigado por me deixar fazer parte desse enredo maluco e por ser essa parceria que aguenta as maiores doideiras. <br><br>
    
    <b>Feliz aniversário! Que venham mais 7, 14, 21 anos de muita call e muita risada.</b>
</div>
""", unsafe_allow_html=True)

st.write("---")

# Interatividade
if st.button('Relembrar é viver! 🍻'):
    st.snow()
    st.toast("7 anos não são 7 dias!", icon="🔥")
    st.write("### 🎮 Status da nossa Amizade:")
    st.info("Calls de 48h: Concluídas ✅")
    st.info("Web Irmãos: Sobrevivemos ✅")
    st.info("Parceria: Infinita ✅")

st.caption("Feito de coração pra fiota mais foda que eu conheço.")
