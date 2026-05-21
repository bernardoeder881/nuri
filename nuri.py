import streamlit as st

# Configuração da página do site
st.set_page_config(page_title="Trilha AutoData AI", page_icon="🚀", layout="centered")

# Título Principal e Introdução
st.title("🚀 Trilha de Aprendizado: Automação & Big Data")
st.subheader("O combo perfeito: Dominar o assunto, resolver problemas e se divertir.")
st.markdown("---")

st.markdown("""
Esta trilha foi desenhada para transformar conceitos teóricos de Python e IA em soluções reais de mercado, 
focando na transição de dados caóticos para inteligência de negócios.
""")

# ---- FASE 1 ----
with st.expander("🏁 FASE 1: A Base de Ferro (Onde você está agora)", expanded=True):
    st.markdown("### **Foco: Manipular, limpar e resumir tabelas**")
    st.checkbox("**Pandas & NumPy:** Filtros (`.loc`), agrupamentos (`.groupby`) e cruzamento de tabelas (`merge`).", value=True)
    st.checkbox("**Estruturas de Dados:** Lógica de Dicionários e formato JSON (essencial para conversar com IAs).")
    st.info("💡 *Nota Mental:* O Pandas é quem consolida a inteligência. A IA limpa o caos individual, o Pandas resolve o todo.")

# ---- FASE 2 ----
with st.expander("🤖 FASE 2: O Cérebro do Sistema (Introduzindo a IA)", expanded=False):
    st.markdown("### **Foco: Fazer o computador entender textos livres e contratos**")
    st.checkbox("**Biblioteca `requests`:** Entender como o Python conversa com a internet.")
    st.checkbox("**API da OpenAI (ChatGPT):** Enviar texto bruto ou extraído e receber dados estruturados.")
    st.checkbox("**Prompt Engineering para Extração:** Criar comandos que forçam a IA a responder estritamente em JSON.")

# ---- FASE 3 ----
with st.expander("🎨 FASE 3: A Fachada e a Entrega (O Produto Real)", expanded=False):
    st.markdown("### **Foco: Dar um 'botão' para o cliente usar sem ver o código**")
    st.checkbox("**Interface com Streamlit:** Criar páginas web estruturadas com inputs de usuário.")
    st.checkbox("**Componentes de Upload:** Criar o botão de 'Arraste seu PDF aqui'.")
    st.checkbox("**Componentes de Download:** Exportar os DataFrames do Pandas direto para arquivos `.xlsx` (Excel).")

# ---- FASE 4 ----
with st.expander("🔄 FASE 4: A Recorrência e Conexões (O Negócio Escalável)", expanded=False):
    st.markdown("### **Foco: Fazer o sistema rodar sozinho e gerar receita mensal**")
    st.checkbox("**Integração Google Sheets (`gspread`):** Atualizar planilhas em nuvem em tempo real.")
    st.checkbox("**APIs de WhatsApp (Ex: Make.com / Evolution API):** Automatizar o atendimento e capturar dados na origem.")
    st.checkbox("**Hospedagem em Nuvem (PythonAnywhere / Cloud):** Colocar o código para rodar 24/7 sem depender do seu PC.")

# Rodapé Motivacional
st.markdown("---")
st.caption("Desenvolvido com Python & Streamlit para a construção da segunda fonte de renda perfeita.")
