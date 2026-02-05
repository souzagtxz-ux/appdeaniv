import streamlit as st

# Configurações do Site
st.set_page_config(page_title="7 Anos de Lenda", page_icon="🎈")

# CSS - Roxo, Vermelho e Borda Azul
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #4b0082 0%, #ff0000 100%);
        background-attachment: fixed;
    }
    
    .card-resenha {
        background: rgba(0, 0, 0, 0.75);
        padding: 30px;
        border-radius: 20px;
        border: 3px solid #00ffff;
        color: white;
        font-family: 'sans-serif';
        font-size: 19px;
        line-height: 1.5;
    }

    h1 {
        text-align: center;
        color: #00ffff;
        text-shadow: 2px 2px #000;
        font-size: 40px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>FELIZ NIVER, FIOTA! 🎉</h1>", unsafe_allow_html=True)

# Texto sem frescura e sem parecer IA
st.markdown(f"""
<div class='card-resenha'>

Papo reto, 7 anos já... nem parece q passou tanto tempo kkkkk. 

Se a gente fosse contar tudo q já rolou dava um documentário muito doido. 
Lembro até hoje das nossas primeiras resenhas e daquelas **calls de 24h, 48h** q a gente fazia... só os loucos sobreviviam sem dormir, rindo de qualquer merda na call kkkkk.
A gente não só jogava junto, a gente **VIVIA** no mundo virtual, né? Mó saudade dessa época, era bom demais.

E mano, impossível esquecer a fase dos seus namoradinhos KKKKKKK. 
Você namorando o viado (ele era muito engraçado namoral) e do nada você ainda **PEGOU MEU WEB IRMÃO??** Só você msm pra ter essa audácia kkkkkkk. A gente passou por cada surto e cada drama q virou tudo piada interna hoje.

Tu é a prova q as melhores amizades vem dos lugares mais aleatórios. 
Ver vc crescendo e conquistando suas paradas é muito foda, de vdd. 
Mesmo q vc seja meio surtada as vezes (kkkkk), vc é uma pessoa **incrivelmente foda** e merece o mundo, fiota.

Fiz esse **site** aqui só pra marcar a data e te lembrar q tamo junto. 
Bora acumular mais mil horas de call e foda-se kkkkk. É nois sempre! 🤙🔥

</div>
""", unsafe_allow_html=True)

# Botão de Interação
if st.button('Clica pra ver a mágica'):
    st.balloons()
    st.snow()
    st.toast("7 anos aguentando essa talarica kkkk", icon="🔥")

st.markdown("<p style='text-align: center; color: white; opacity: 0.6; margin-top: 20px;'>7 anos e contando...</p>", unsafe_allow_html=True)
