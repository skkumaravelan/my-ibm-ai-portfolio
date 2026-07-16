import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="IBM AI & Data Science Portfolio",
    page_icon="🤖",
    layout="wide"
)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home Profile", "1. IBM Data Science", "2. Future Tracks"])

# ----------------- HOME PROFILE PAGE -----------------
if page == "Home Profile":
    st.title("👨‍💻 AI Engineering & Data Science Portfolio")
    st.subheader("An Intentional Learning Journey Mapping Frameworks to Production")
    
    st.write(
        "Welcome! This interactive portfolio acts as a live ledger of my commitment to mastering the "
        "AI ecosystem. Below is the multi-stage certification roadmap I am aggressively executing. "
        "Each section tracks core architectural concepts and the practical applications built to prove them."
    )
    
    st.markdown("---")
    st.markdown("### 🗺️ The Strategic 5-Stage IBM Roadmap")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Stage 1: Core Foundations**\n* Program: IBM Data Science\n* Focus: Statistics, SQL, Python, Classic ML")
        st.warning("**Stage 2: Modeling Mastery**\n* Program: IBM Machine Learning\n* Focus: Supervised, Unsupervised, & Reinforcement Learning")
        st.error("**Stage 3: Deep Architecture**\n* Program: IBM AI Engineering\n* Focus: Neural Networks, PyTorch, Keras, TensorFlow")
    with col2:
        st.success("**Stage 4: LLM Mechanics**\n* Program: IBM Generative AI Engineering\n* Focus: Transformers, Fine-Tuning, Prompt Engineering")
        st.metric(label="The Advanced Apex Target", value="Stage 5: RAG & Agentic AI", delta="LangGraph / CrewAI")

# ----------------- STAGE 1: IBM DATA SCIENCE -----------------
elif page == "1. IBM Data Science":
    st.title("📘 Stage 1: IBM Data Science Professional Certificate")
    st.caption("Status: ⏳ In Progress | Expected Target: 3 Months")
    
    # Credly Badge Row Placeholder
    col_badge, col_info = st.columns([1, 3])
    with col_badge:
        # Placeholder visual until you earn your badge
        st.image("https://placehold.co", use_column_width=True)
    with col_info:
        st.markdown("""
        ### Certified Capabilities Breakdown
        * **Mathematical Base**: Statistical analysis, exploratory data analysis (EDA), and predictive modeling.
        * **Core Stack**: Data collection and processing using **Python**, **SQL**, **Pandas**, and **Numpy**.
        * **Classical Modeling**: Linear and logistic regression, decision trees, KNN, and clustering algorithms using **Scikit-learn**.
        """)
        
    st.markdown("---")
    st.markdown("### 🛠️ Curriculum Milestones & Applied Capabilities")
    
    # Core Milestones
    m1, m2, m3 = st.columns(3)
    with m1:
        with st.container(border=True):
            st.markdown("#### 🐍 Python & SQL Core")
            st.write("**Concept Learned:** Relational database schemas, advanced JOIN operations, and analytical Python data processing structures.")
            st.code("# Code Pattern Proved\nimport pandas as pd\ndf = pd.read_sql_query(query, conn)")
    with m2:
        with st.container(border=True):
            st.markdown("#### 📊 Exploratory Analysis")
            st.write("**Concept Learned:** Data cleaning pipelines, handling missing values, correlation analysis, and data visualization.")
            st.code("# Code Pattern Proved\nsns.heatmap(df.corr(), annot=True)")
    with m3:
        with st.container(border=True):
            st.markdown("#### 🤖 Predictive Modeling")
            st.write("**Concept Learned:** Model selection, splitting training/test datasets, hyperparameter tuning, and model evaluation metrics.")
            st.code("# Code Pattern Proved\nmodel.fit(X_train, y_train)")

    st.markdown("### 🏆 Comprehensive Capstone Showcase")
    with st.container(border=True):
        st.markdown("#### **SpaceX Falcon 9 First Stage Landing Prediction**")
        st.write(
            "**The Executive Problem:** SpaceX saves millions by reusing rocket boosters. To compete with them, an alternative "
            "aerospace firm wants to predict whether the first stage of Falcon 9 will land successfully."
        )
        st.write(
            "**My Engineering Execution:** I ingested data via web scraping (BeautifulSoup) and REST APIs. I performed "
            "EDA using SQL and Folium maps to spot geographical launch site trends. Finally, I trained multiple machine "
            "learning classifiers (SVM, Trees, Logistic Regression) to predict booster landing accuracy, comparing metrics to optimize precision."
        )
        # Link placeholders for your code
        st.markdown("[🔗 GitHub Code Repository Placeholder] | [🔗 Interactive Folium Map Notebook Placeholder]")

# ----------------- STAGE 2-5 PLACEHOLDER -----------------
elif page == "2. Future Tracks":
    st.title("🚀 Next-Generation AI Horizons")
    st.write("These tabs represent the specialized modules that will unlock automatically as code foundations are achieved.")
    
    tab1, tab2, tab3 = st.tabs(["Machine Learning & Deep Learning", "Generative AI Engineering", "RAG & Agentic AI"])
    
    with tab1:
        st.markdown("### Deep Learning Systems")
        st.write("Focus areas will include Convolutional Neural Networks (CNNs), Recurrent Neural Networks (RNNs), and training models using PyTorch.")
    with tab2:
        st.markdown("### Large Language Model Foundations")
        st.write("Focus areas will include Transformer architectures, Attention mechanisms, and context manipulation.")
    with tab3:
        st.markdown("### Multi-Agent Systems & Frameworks")
        st.write("Focus areas will include building autonomous chains using LangGraph, building collaborative crews using CrewAI, and designing memory-backed vector systems.")
