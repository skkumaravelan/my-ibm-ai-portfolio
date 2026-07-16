import streamlit as st

def render():
    st.title("🤖 Stage 5: IBM RAG and Agentic AI Professional Certificate")
    st.caption("Status: 🔒 Locked | Course Load: 11 Courses")
    st.markdown("[🔗 Official Program Link](https://www.coursera.org/professional-certificates/ibm-rag-and-agentic-ai)")
    
    c1, c2 = st.columns([1, 3])
    with c1:
        st.markdown("<div style='background-color:#0f62fe; padding:15px; border-radius:5px; color:white; font-weight:bold; text-align:center;'>🚀 APEX GOAL<br><br>Autonomous Agents</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("""
        ### Target Competencies
        * **Advanced RAG**: Implementing pre-retrieval optimization, post-retrieval re-ranking, and context validation architectures.
        * **Agentic Workflows**: Engineering systems utilizing the **ReAct design pattern** to allow LLMs to invoke native custom functions sequentially.
        * **Multi-Agent Systems**: Deploying multi-agent collaboration matrices using framework toolkits like **LangGraph** and **CrewAI**.
        """)
        
    st.markdown("---")
    st.markdown("### 🛠️ Curriculum Milestones & Applied Capabilities")
    m1, m2, m3 = st.columns(3)
    with m1:
        with st.container(border=True):
            st.markdown("#### 🗺️ LangGraph Systems")
            st.write("Structuring non-deterministic state machine loops with defined computational states and edges.")
            st.code("from langgraph.graph import StateGraph, END\nworkflow = StateGraph(AgentState)", language="python")
    with m2:
        with st.container(border=True):
            st.markdown("#### 👥 CrewAI Workflows")
            st.write("Assigning specific operational mandates, memories, and tools to collaborative execution agents.")
            st.code("from crewai import Agent, Crew\nanalyst = Agent(role='Data Analyst', goal='Parse CSV')", language="python")
    with m3:
        with st.container(border=True):
            st.markdown("#### 📁 Vector Search Systems")
            st.write("Storing, index-tracking, and querying embedding metrics within distributed Vector databases.")
            st.code("index.upsert(vectors=[('id', embedding_vector)])", language="python")

    st.markdown("### 🏆 Comprehensive Capstone Showcase")
    with st.container(border=True):
        st.markdown("#### **Autonomous Multi-Agent Market Research and Competitive Intelligence Squad**")
        st.write("**The Executive Problem:** Leadership requires zero-human monitoring systems to track product data, compile risk logs, and write intelligence briefings automatically.")
        st.write("**My Engineering Execution:** Engineered a LangGraph state network connecting three autonomous agents: a scraper agent, an analysis checker, and a technical writer. Integrated tools with defensive exceptions to protect database endpoints.")
