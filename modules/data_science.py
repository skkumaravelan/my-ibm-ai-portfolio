import streamlit as st

def render():
    st.title("📘 Stage 1: IBM Data Science Professional Certificate")
    st.caption("Status: ⏳ In Progress | Expected Target: 3 Months")
    st.markdown("[🔗 Official Program Link](https://coursera.org)")
    
    c1, c2 = st.columns([1, 3])
    with c1:
        st.info("**Track Status:**\n\nActive Sandbox\n\n🎯 Foundations Base")
    with c2:
        st.markdown("""
        ### Target Competencies
        * **Core Stack**: Relational databases, dataset cleaning, and analytical processing using **Python**, **SQL**, **Pandas**, and **Numpy**.
        * **Classical Modeling**: Implementation of basic regression, classification, and clustering systems using **Scikit-learn**.
        """)
        
    st.markdown("---")
    st.markdown("### 🛠️ Curriculum Milestones & Applied Capabilities")
    m1, m2, m3 = st.columns(3)
    with m1:
        with st.container(border=True):
            st.markdown("#### 🐍 Python & SQL Core")
            st.write("Relational database schemas and querying matrix architectures.")
            st.code("import pandas as pd\ndf = pd.read_sql_query(query, conn)", language="python")
    with m2:
        with st.container(border=True):
            st.markdown("#### 📊 Exploratory Analysis")
            st.write("Data cleaning pipelines, handling missing values, and visualization layouts.")
            st.code("import seaborn as sns\nsns.heatmap(df.corr(), annot=True)", language="python")
    with m3:
        with st.container(border=True):
            st.markdown("#### 🤖 Predictive Modeling")
            st.write("Model selection, train/test splitting, and evaluation metrics.")
            st.code("from sklearn.linear_model import LogisticRegression\nmodel.fit(X_train, y_train)", language="python")

    st.markdown("### 🏆 Comprehensive Capstone Showcase")
    with st.container(border=True):
        st.markdown("#### **SpaceX Falcon 9 First Stage Landing Prediction**")
        st.write("**The Executive Problem:** Predict whether the first stage of Falcon 9 will land successfully to assess competitive launch pricing models.")
        st.write("**My Engineering Execution:** Data ingestion via REST APIs and web scraping. Geospatial analysis using Folium maps. Trained multiple classification algorithms (SVM, Trees) to predict booster landing profiles.")
