import streamlit as st

def render():
    st.title("📘 IBM Data Science Professional Certificate")
    st.caption("Target Focus: SQL Queries, Exploratory Visual Analytics, and Foundational Pipelines")
    st.markdown("---")
    
    tab_notes, tab_repo = st.tabs(["📝 Core Takeaways & Snippets", "🏆 Active Project Logs"])
    
    with tab_notes:
        st.markdown("### 💾 Personal Engineering Notes")
        st.write("Edit this module block inside `modules/data_science.py` to log your notes as you learn.")
        
        with st.container(border=True):
            st.markdown("#### **Data Wrangling & API Ingestion Check**")
            st.code("# Paste your verified extraction and data cleaning snippets here\nimport pandas as pd\n\n# Example template placeholder:\n# df = pd.read_csv('your_source.csv').dropna()", language="python")

    with tab_repo:
        st.markdown("### 🚀 Production Repositories")
        with st.container(border=True):
            st.markdown("#### **SpaceX Falcon 9 Booster Landing Prediction Pipeline**")
            st.write("Combine web extraction scripts, relational database queries, and exploratory graphs to solve the landing optimization problem.")
            st.markdown("⚙️ *Staging Info: Paste your GitHub repository and deployment URLs here once built.*")
