import streamlit as st
import time

# --- Configuração da Página e Tema ---
st.set_page_config(
    page_title="NOSSA HISTÓRIA: 7 Anos de Pura Lenda!",
    page_icon="💜",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CSS para o Tema Roxo com Vermelho Clean e Borda Azul ---
st.markdown("""
    <style>
    /* Fundo Roxo com Vermelho Clean */
    body {
        background: linear-gradient(135deg, #6a0572 0%, #ab0020 100%); /* Roxo Escuro para Vermelho Vinho */
        background-attachment: fixed;
        color: #f0f2f6; /* Cor do texto padrão */
        font-family: 'Montserrat', sans-serif;
    }
    .main {
        background: linear-gradient(135deg, #6a0572 0%, #ab0020 100%); /* Mantém o gradiente para o main container */
    }
    .stApp {
        background: linear-gradient(135deg, #6a0572 0%, #ab0020 100%);
        background-attachment: fixed;
    }

    /* Título Principal */
    .title-h1 {
        font-family: 'Lobster', cursive; /* Fonte mais decorativa para o título */
        font-size: 3.5em; /* Aumenta o tamanho */
        color: #FFD700; /* Dourado para o destaque */
        text-align: center;
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.7);
        margin-bottom: 25px;
        line-height: 1.2;
    }

    /* Card da Mensagem Principal */
    .card-message {
        background: rgba(255, 255, 255, 0.15); /* Fundo semi-transparente para o card */
        padding: 35px;
        border-radius: 20px;
        border: 3px solid #00BFFF; /* Borda Azul Claro */
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5); /* Sombra mais forte */
        margin-bottom: 30px;
        text-align: justify;
        color: #f0f2f6; /* Cor do texto no card */
        font-size: 1.15em;
        line-height: 1.8;
    }
    .card-message strong {
        color: #FFD700; /* Dourado para negritos */
    }
    .card-message em {
        color: #FFA07A; /* Salmão para ênfase (piadas/lembranças) */
    }

    /* Subtítulos */
    .subtitle-h2 {
        font-size: 2.2em;
        color: #FF69B4; /* Rosa Choque para subtítulos */
        text-align: center;
        margin-top: 40px;
        margin-bottom: 20px;
        border-bottom: 2px solid #FF69B4;
        padding-bottom: 10px;
    }

    /* Botões */
    .stButton>button {
        background-color: #00BFFF; /* Azul Claro para o botão */
        color: white;
        border-radius: 12px;
        padding: 12px 25px;
        font-size: 1.1em;
        font-weight: bold;
        transition: all 0.3s ease;
        width: 100%;
        margin-top: 20px;
    }
    .stButton>button:hover {
        background-color: #FF69B4; /* Rosa Choque no hover */
        border-color: #FF69B4;
        transform: scale(1.03);
    }
    
    /* Fontes externas para o visual */
    @import url('https://fonts.googleapis.com/css2?family=Lobster&family=Montserrat:wght@400;700&display=swap');
    </style>
""", unsafe_allow_html=True)

# --- Efeitos de Entrada ---
st.balloons() # Balões coloridos no início

# --- Título Principal ---
st.markdown("<h1 class='title-h1'> NOSSA HISTÓRIA:<br>7 Anos de Pura Lenda! 🎉</h1>", unsafe_allow_html=True)

st.markdown("<div class='card-message'>", unsafe_allow_html=True)

st.write("## Fiuta, se liga na fita...")

st.write("""
    Sete anos! Parece que foi ontem que a gente se trombou nessa vida, 
    mas ao mesmo tempo, parece que te conheço de todas as vidas passadas. 
    E que sorte a minha de ter uma fiota como você nessa jornada louca que a gente chama de existência.
    Não é só mais um aniversário, é a celebração de uma amizade que já virou lenda, 
    uma história com mais plot twist que novela das nove e mais risada que comédia de stand-up.
""")

st.write("---")

st.markdown("<h3>Nossa Galeria de Pérolas (Os Momentos Inesquecíveis)</h3>", unsafe_allow_html=True)

st.write("""
    Pensa em tudo que a gente já passou? É filme, é série, é documentário\!
    Desde as primeiras resenhas, as <strong class='destaque'>calls de 24/48 horas</strong> que a gente fazia,
    onde o único objetivo era sobreviver ao sono e à sanidade, mas a gente sempre saía com uma história nova
    e, claro, com a voz embargada de tanto rir. A gente não só jogava junto, a gente <strong class='destaque'>VIVIA</strong>
    junto no mundo virtual, né? Que época...
""")

st.write("""
    E quem consegue esquecer a fase dos seus <em class='destaque'>namoradinhos</em>? KKKKKKK!
    Ainda lembro de você namorando *o viado* (que era engraçado demais, diga-se de passagem!) e, como se não bastasse,
    ainda metendo um <em class='destaque'>web irmão</em> na jogada! Cara, só a gente pra criar essas histórias
    que ninguém acreditaria se contasse. Mas a gente tava lá, vivendo cada surto, cada drama,
    e transformando tudo em piada interna que dura até hoje.
""")

st.write("""
    Você é a prova viva de que as melhores amizades nascem dos lugares mais inesperados
    e das situações mais aleatórias. Ver você crescer, amadurecer (ou não, dependendo do dia kkkk),
    superar cada perrengue e conquistar seus sonhos... isso é um presente pra mim.
    Sua força, seu jeito único de ser, sua risada contagiante (mesmo nas piores horas),
    tudo isso faz de você uma pessoa <strong class='destaque'>incrivelmente foda!</strong>
""")

st.write("""
    E por falar em "incrivelmente foda", esse é só um pequeno "APK" (ou web-app, né? rs)
    pra te lembrar o quanto você é importante pra mim. Que a gente continue acumulando mais
    milhares de horas de call, mais centenas de piadas internas e mais infinitos motivos
    pra celebrar essa amizade que é mais forte que qualquer Wi-Fi caindo.
""")

st.write("</div>", unsafe_allow_html=True) # Fecha o card-message

st.write("---")

st.markdown("<h2 class='subtitle-h2'>O que eu desejo pra você?</h2>", unsafe_allow_html=True)

# Expansor para uma mensagem extra (abre e fecha)
with st.expander("Clique aqui para a próxima fase da nossa amizade! 💖"):
    st.write("""
        Desejo que a vida te surpreenda com as maiores alegrias, que cada obstáculo vire escada,
        e que você continue irradiando essa energia que só você tem.
        Que todos os seus objetivos se realizem e que nunca te falte motivos para sorrir,
        para jogar, para viver intensamente cada segundo.
        Conte comigo, sempre! Para as risadas, para os perrengues, para tudo.
    """)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3NpaWZ0aGg1OW1oZWR1a3FpN3R3NGI5ZGFnZjY3NGU5bGFwd3B2eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kUtK78L72o60s/giphy.gif", caption="Você é pura luz!", use_column_width=True)


if st.button('Mandar mais um burst de carinho! ✨'):
    st.snow()
    st.toast("Parabéns, minha fiota!", icon="🥳")
    st.success("Que seu dia seja tão incrível quanto você!")
    # Adicionando um áudio suave de parabéns, se desejar
    # st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", format="audio/mp3", start_time=0)


st.markdown("""
    <div style='text-align: center; margin-top: 50px; color: #f0f2f6;'>
        <small>Criado com muito carinho para a melhor fiota do mundo.</small><br>
        <small>7 anos e contando...</small>
    </div>
""", unsafe_allow_html=True)
