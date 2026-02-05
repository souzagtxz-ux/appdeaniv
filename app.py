import streamlit as st

# Configurações da página
st.set_page_config(page_title="7 Anos de Lenda", page_icon="🎈")

# CSS - O visual roxo/vermelho/azul que você pediu
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #4b0082 0%, #ff0000 100%);
        background-attachment: fixed;
    }
    
    /* Card da Mensagem */
    .card-resenha {
        background: rgba(0, 0, 0, 0.6);
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #00ffff; /* Borda Azul Claro / Ciano */
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin-top: 20px;
    }

    .destaque-azul { color: #00ffff; font-weight: bold; }
    .destaque-vermelho { color: #ff4b4b; font-weight: bold; }
    
    h1 {
        text-align: center;
        color: white;
        text-shadow: 2px 2px #4b0082;
    }
    </style>
""", unsafe_allow_html=True)

# Título
st.markdown("<h1>FELIZ NIVER, FIOTA! 🎉</h1>", unsafe_allow_html=True)

# O texto com cara de 16 anos
st.markdown(f"""
<div class='card-resenha'>
    Papo reto, 7 anos já... nem parece q passou tanto tempo kkkkk. 
    Se a gente fosse contar tudo q já rolou dava um documentário muito doido. 
    Lembro até hoje das nossas primeiras resenhas e daquelas 
    <span class='destaque-azul'>calls de 24h, 48h</span> q a gente fazia... 
    só os loucos sobreviviam sem dormir, rindo de qualquer merda na call kkkkk.
    A gente não só jogava junto, a gente <span class='destaque-azul'>VIVIA</span> no mundo virtual, né? 
    Mó saudade dessa época, era bom demais.<br><br>

    E mano, impossível esquecer a fase dos seus <span class='destaque-vermelho'>namoradinhos</span> KKKKKKK. 
    Você namorando o viado (ele era muito engraçado namoral) e do nada você ainda meteu 
    um <span class='destaque-vermelho'>web irmão</span> na parada?? Só a gente msm pra ter essas histórias 
    q ninguém acredita kkkkk. A gente passou por cada surto e cada drama q virou tudo piada interna hoje.<br><br>

    Tu é a prova q as melhores amizades vem dos lugares mais aleatórios. 
    Ver vc crescendo e conquistando suas paradas é muito foda, de vdd. 
    Mesmo q vc seja meio surtada as vezes (kkkkk), vc é uma pessoa <span class='destaque-azul'>incrivelmente foda</span> 
    e merece o mundo, fiota.<br><br>

    Fiz esse "app" aqui só pra te lembrar q vc é importante pra mim e q 
    essa amizade aqui é mais forte q qualquer Wi-Fi caindo no meio da partida. 
    Bora acumular mais mil horas de call ainda! Tmj sempre! 🤙🔥
</div>
""", unsafe_allow_html=True)

# Efeitos
if st.button('Clica aqui pra ver a mágica'):
    st.balloons()
    st.snow()
    st.toast("Parabéns, lenda!", icon="🔥")

st.markdown("<p style='text-align: center; color: white; opacity: 0.6; margin-top: 20px;'>7 anos e contando...</p>", unsafe_allow_html=True)
    </div>
""", unsafe_allow_html=True)
