import streamlit as st
import sys
import os

# Inject current path helper configs
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from modules import data_science, machine_learning, ai_engineering, gen_ai, agentic_ai

st.set_page_config(
    page_title="My AI Learning Ledger & Vault",
    page_icon="🤖",
    layout="wide"
)

# Sidebar Control Console
st.sidebar.markdown("# 🛠️ Control Room")
st.sidebar.write("Navigate between the high-level roadmap and your granular code execution journals.")

page = st.sidebar.radio(
    "Active Workspace Area:",
    [
        "Roadmap Overview Hub",
        "Stage 1: Data Science Core",
        # "Stage 2: Machine Learning",
        #  "Stage 3: Deep AI Engineering",
        #"Stage 4: Generative AI",
        # "Stage 5: RAG & Agentic AI"
    ]
)

# ----------------- HOME ROADMAP HUB -----------------
if page == "Roadmap Overview Hub":
    st.title("👨‍💻 My Personal AI & Data Engineering Ledger")
    st.subheader("An Intentional Space for Storing Code Patterns and Production Deployments")
    st.write(
        "Click any card block inside the sequential learning path grid below to bring forward its "
        "target credential badge asset and official curriculum database link."
    )
    st.markdown("---")

    # Initialize Streamlit session state handlers to maintain active button click states
    if "active_card" not in st.session_state:
        st.session_state.active_card = "Stage 1: IBM Data Science" # Sets default view

    st.markdown("### 🗺️ The Strategic 5-Stage IBM Sequential Roadmap")
    
    # Render the 5 Interactive Clickable Tracker Cards Side-by-Side
    c1, c2, c3, c4, c5 = st.columns(5)
    
    with c1:
        if st.button("📘\n\n**Stage 1**\n\nData Science", use_container_width=True):
            st.session_state.active_card = "Stage 1: IBM Data Science"
    with c2:
        if st.button("🍊\n\n**Stage 2**\n\nMachine Learning", use_container_width=True):
            st.session_state.active_card = "Stage 2: IBM Machine Learning"
    with c3:
        if st.button("🧠\n\n**Stage 3**\n\nAI Engineering", use_container_width=True):
            st.session_state.active_card = "Stage 3: IBM AI Engineering"
    with c4:
        if st.button("✨\n\n**Stage 4**\n\nGenAI Engineering", use_container_width=True):
            st.session_state.active_card = "Stage 4: IBM Generative AI Engineering"
    with c5:
        if st.button("🚀\n\n**Stage 5**\n\nAgentic AI", use_container_width=True):
            st.session_state.active_card = "Stage 5: IBM RAG & Agentic AI"

    st.markdown("---")
    
    # ----------------- DYNAMIC BADGE & CARD CONTAINER RENDERER -----------------
    active = st.session_state.active_card
    
    with st.container(border=True):
        st.markdown(f"### 🎯 Brought Forward focus: **{active}**")
        
        badge_col, text_col = st.columns([1, 4])
        
        with badge_col:
            # Conditional selector matching color variables to your requested track sequence links
            if active == "Stage 1: IBM Data Science":
                st.image("https://placehold.co", use_container_width=True)
                st.markdown("[🌐 View Certification Portal](https://www.coursera.org/professional-certificates/ibm-data-science)")
                
            elif active == "Stage 2: IBM Machine Learning":
                st.image("https://placehold.co", use_container_width=True)
                st.markdown("[🌐 View Certification Portal](https://www.coursera.org/professional-certificates/ibm-machine-learning)")
                
            elif active == "Stage 3: IBM AI Engineering":
                st.image("https://placehold.co", use_container_width=True)
                st.markdown("[🌐 View Certification Portal](https://www.coursera.org/professional-certificates/ai-engineer)")
                
            elif active == "Stage 4: IBM Generative AI Engineering":
                st.image("https://placehold.co", use_container_width=True)
                st.markdown("[🌐 View Certification Portal](https://www.coursera.org/professional-certificates/ibm-generative-ai-engineering)")
                
            elif active == "Stage 5: IBM RAG & Agentic AI":
                st.image("https://placehold.co", use_container_width=True)
                st.markdown("[🌐 View Certification Portal](https://www.coursera.org/professional-certificates/ibm-rag-and-agentic-ai)")

        with text_col:
            # Informational tracking fields mapping your learning trajectory summary
            if active == "Stage 1: IBM Data Science":
                st.write("**Target Goals:** Lock down statistical analysis data models, compute SQL database aggregations, and process clear data visualization charts.")
                st.caption("📈 *Status: Starting day after tomorrow! Open 'Stage 1' in the sidebar to log technical snippets.*")
            elif active == "Stage 2: IBM Machine Learning":
                st.write("**Target Goals:** Master regression regularization parameters (Lasso/Ridge), execute PCA reductions, and build time-series arrays.")
                st.caption("🔒 *Status: Planned Next.*")
            elif active == "Stage 3: IBM AI Engineering":
                st.write("**Target Goals:** Architect fully-connected neural networks, process computer vision arrays via PyTorch, and run PySpark cluster processing pools.")
                st.caption("🔒 *Status: Planned Level 3.*")
            elif active == "Stage 4: IBM Generative AI Engineering":
                st.write("**Target Goals:** Explore attention networks, construct LangChain tracking modules, and parameter tune open models.")
                st.caption("🔒 *Status: Advanced AI Phase.*")
            elif active == "Stage 5: IBM RAG & Agentic AI":
                st.write("**Target Goals:** Build non-deterministic state graph routing paths with LangGraph, deploy multi-agent crews with CrewAI, and configure vector databases.")
                st.error("🚀 *The Ultimate Apex Milestone Target.*")

# --- LEAVE SUB-MODULES ALIVE UNDER SIDEBAR LOGIC ROUTER ---
elif page == "Stage 1: Data Science Core": data_science.render()
elif page == "Stage 2: Machine Learning": machine_learning.render()
elif page == "Stage 3: Deep AI Engineering": ai_engineering.render()
elif page == "Stage 4: Generative AI": gen_ai.render()
elif page == "Stage 5: RAG & Agentic AI": agentic_ai.render()
