import streamlit as st

def render():
    st.title("📘 Stage 1: IBM Data Science Professional Certificate")
    st.markdown("🔗 **Official Track Link:** [coursera.org/professional-certificates/ibm-data-science](https://coursera.org)")
    
    # Metrics Header
    c1, c2, c3 = st.columns(3)
    with c1: st.metric(label="Total Curriculum Load", value="12 Courses")
    with c2: st.metric(label="Estimated Study Time", value="~179 Hours")
    with c3: st.metric(label="College Transfer Value", value="12 ACE Credits")

    st.markdown("---")
    st.subheader("📚 12-Course Syllabus Breakdown")

    # Courses 1-4
    with st.expander("📂 Phase 1: Foundational Literacy & Setup (Courses 1 - 4)", expanded=True):
        st.markdown("1. What is Data Science? / 2. Tools for Data Science / 3. Data Science Methodology / 4. Python for Data Science")

    # Courses 5-8
    with st.expander("📂 Phase 2: Data Engineering & Analytics (Courses 5 - 8)", expanded=False):
        st.markdown("5. Python Project / 6. Databases and SQL / 7. Data Analysis / 8. Data Visualization")

    # Courses 9-12
    with st.expander("📂 Phase 3: Applied Machine Learning & Capstone (Courses 9 - 12)", expanded=False):
        st.markdown("9. Machine Learning with Python / 10. Applied Capstone / 11. Generative AI / 12. Career Guide")

    st.markdown("---")
    st.subheader("🛠️ Core Stack & Capstone")
    st.code("import pandas as pd\nimport sklearn\nimport matplotlib.pyplot as plt", language="python")
    st.info("Capstone: SpaceX Falcon 9 First Stage Landing Prediction Pipeline")
