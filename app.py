import streamlit as st
# Dynamic routing imports
from modules import data_science, machine_learning, ai_engineering, gen_ai, agentic_ai

# Page Configuration
st.set_page_config(
    page_title="IBM AI Roadmap & Capstone Ledger",
    page_icon="🤖",
    layout="wide"
)

# Sidebar Navigation Design
st.sidebar.markdown("# 🗺️ Staging Dashboard")
st.sidebar.write("This sandbox tracks my execution roadmap through advanced IBM learning sequences.")

# Radio selectors organized in your optimized sequence path
page = st.sidebar.radio(
    "Select Learning Stage Path:",
    [
        "Main Hub: System Overview",
        "Stage 1: IBM Data Science",
        "Stage 2: IBM Machine Learning",
        "Stage 3: IBM AI Engineering",
        "Stage 4: IBM Generative AI Engineering",
        "Stage 5: IBM RAG & Agentic AI"
    ]
)

# --- ROUTING LOGIC ENGINE ---
if page == "Main Hub: System Overview":
    st.title("👨‍💻 AI Engineering & Data Science Portfolio Sandbox")
    st.subheader("An Intentional Learning Journey Mapping Frameworks to Production")
    st.write(
        "Welcome! This interactive portfolio acts as a live ledger of my commitment to mastering the "
        "AI ecosystem. Below is the multi-stage certification roadmap I am aggressively executing. "
        "Each section tracks core architectural concepts and the practical applications built to prove them."
    )
    st.markdown("---")
    st.markdown("### 🗺️ The Strategic 5-Stage IBM Sequential Roadmap (450-500 Net Hours)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Stage 1: Core Foundations**\n\n* **Program:** IBM Data Science\n* **Focus:** Statistics, SQL, Python, Classic ML")
        st.warning("**Stage 2: Modeling Mastery**\n\n* **Program:** IBM Machine Learning\n* **Focus:** Supervised, Unsupervised, & Time Series Tracking")
        st.error("**Stage 3: Deep Architecture**\n\n* **Program:** IBM AI Engineering\n* **Focus:** Neural Networks, PyTorch, Keras, TensorFlow")
    with col2:
        st.success("**Stage 4: LLM Mechanics**\n\n* **Program:** IBM Generative AI Engineering\n* **Focus:** Transformers, Fine-Tuning, Prompt Frameworks")
        with st.container(border=True):
            st.markdown("<p style='color:#0f62fe; font-weight:bold; margin-bottom:0;'>STAGE 5: APEX GOAL</p>", unsafe_allow_html=True)
            st.markdown("### IBM RAG & Agentic AI")
            st.caption("Frameworks: LangGraph / CrewAI / Vector Architectures")

elif page == "Stage 1: IBM Data Science":
    data_science.render()

elif page == "Stage 2: IBM Machine Learning":
    machine_learning.render()

elif page == "Stage 3: IBM AI Engineering":
    ai_engineering.render()

elif page == "Stage 4: IBM Generative AI Engineering":
    gen_ai.render()

elif page == "Stage 5: IBM RAG & Agentic AI":
    agentic_ai.render()
