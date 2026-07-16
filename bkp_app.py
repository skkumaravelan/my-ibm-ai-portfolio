import streamlit as st

# 1. PAGE CONFIGURATION & WIDESCREEN ENFORCEMENT
st.set_page_config(
    page_title="Frontier Agentic AI Portfolio & Architecture Log",
    page_icon="🟠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. GLOBAL STYLE, CARD FLIP ANIMATION, & LAYOUT CONSTRAINTS
st.markdown(
    """
    <style>
    /* Absolute Clean Slate: Remove Header, Footer, and Menu wrappers */
    [data-testid="stHeader"], 
    footer, 
    #MainMenu, 
    header {
        visibility: hidden !important;
        height: 0px !important;
    }
    
    /* Enforce 95% Maximum Viewport Width */
    .block-container {
        max-width: 95% !important;
        padding-top: 3rem !important;
        padding-bottom: 2rem !important;
        padding-left: 4rem !important;
        padding-right: 4rem !important;
    }
    
    /* Set Global Body & Dashboard Background Canvas */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #111111 !important;
        color: #FFFFFF !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* --- SLEEK 3D CARD FLIP ARCHITECTURE --- */
    .flip-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 24px;
        width: 100%;
        margin-top: 2rem;
    }

    .flip-card {
        background-color: transparent;
        height: 220px;
        perspective: 1000px; /* Gives 3D depth effect */
        cursor: pointer;
    }

    .flip-card-inner {
        position: relative;
        width: 100%;
        height: 100%;
        text-align: center;
        transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
        transform-style: preserve-3d;
    }

    /* Flip condition on hover/click focus */
    .flip-card:hover .flip-card-inner, .flip-card:focus .flip-card-inner {
        transform: rotateY(180deg);
    }

    .flip-card-front, .flip-card-back {
        position: absolute;
        width: 100%;
        height: 100%;
        -webkit-backface-visibility: hidden; /* Safari support */
        backface-visibility: hidden;
        border-radius: 12px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 24px;
        box-sizing: border-box;
    }

    /* Front Card Styling - Clean Minimalist Dark Surface */
    .flip-card-front {
        background-color: #1B1B1B;
        border: 1px solid #2D2D2D;
        color: white;
    }

    /* Back Card Styling - Claude Orange Accent State */
    .flip-card-back {
        background-color: #E0533C;
        color: white;
        transform: rotateY(180deg);
    }

    .card-icon {
        font-size: 2.5rem;
        margin-bottom: 12px;
    }

    .card-title {
        font-size: 1.15rem;
        font-weight: 700;
        letter-spacing: -0.3px;
        margin: 0;
        line-height: 1.2;
    }

    .card-subtitle {
        color: #888888;
        font-size: 0.8rem;
        margin-top: 6px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .card-back-text {
        font-size: 0.95rem;
        font-weight: 500;
        line-height: 1.5;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. HERO HEADER SECTION
st.title("Frontier Agentic AI Portfolio & Architecture Log")
st.caption("Documenting systems engineering, tool execution, and multi-agent workflows using the Anthropic API.")

st.markdown("---")

# 4. SLEEK AGENTIC AI PROJECTS GRID (8 FLIP CARDS)
st.markdown("### 🔬 Pipeline Agentic AI Projects")
st.markdown("Hover or click a card to flip and view the architectural vision.")

# All markup lines strictly flush to the left boundary
project_cards_html = """
<div class="flip-grid">

<!-- Card 1 -->
<div class="flip-card" tabindex="0">
<div class="flip-card-inner">
<div class="flip-card-front">
<div class="card-icon">🧠</div>
<div class="card-title">Cognitive Layer Router</div>
<div class="card-subtitle">Architecture Blueprint</div>
</div>
<div class="flip-card-back">
<div class="card-back-text">Dynamic prompt routing engine optimized for Claude 3.5 multi-turn state evaluations.</div>
</div>
</div>
</div>

<!-- Card 2 -->
<div class="flip-card" tabindex="0">
<div class="flip-card-inner">
<div class="flip-card-front">
<div class="card-icon">🔌</div>
<div class="card-title">Custom MCP Gateway</div>
<div class="card-subtitle">Integration Node</div>
</div>
<div class="flip-card-back">
<div class="card-back-text">Decoupled protocol runtime mapping structured local context to target tool payloads safely.</div>
</div>
</div>
</div>

<!-- Card 3 -->
<div class="flip-card" tabindex="0">
<div class="flip-card-inner">
<div class="flip-card-front">
<div class="card-icon">🗂️</div>
<div class="card-title">Context Synthesizer</div>
<div class="card-subtitle">Data Worker</div>
</div>
<div class="flip-card-back">
<div class="card-back-text">Autonomous pipeline transforming unorganized repository files into strict prompt window segments.</div>
</div>
</div>
</div>

<!-- Card 4 -->
<div class="flip-card" tabindex="0">
<div class="flip-card-inner">
<div class="flip-card-front">
<div class="card-icon">🛠️</div>
<div class="card-title">Self-Correcting Loop</div>
<div class="card-subtitle">Execution Pipeline</div>
</div>
<div class="flip-card-back">
<div class="card-back-text">Error isolation wrapper designed to catch, analyze, and correct tool invocation failures live.</div>
</div>
</div>
</div>

<!-- Card 5 -->
<div class="flip-card" tabindex="0">
<div class="flip-card-inner">
<div class="flip-card-front">
<div class="card-icon">📊</div>
<div class="card-title">Token Budget Guardian</div>
<div class="card-subtitle">Cost Optimizer</div>
</div>
<div class="flip-card-back">
<div class="card-back-text">Middleware analytics tracker calculating context window decay and optimizing caching parameters.</div>
</div>
</div>
</div>

<!-- Card 6 -->
<div class="flip-card" tabindex="0">
<div class="flip-card-inner">
<div class="flip-card-front">
<div class="card-icon">🔄</div>
<div class="card-title">Multi-Agent Swarm Sync</div>
<div class="card-subtitle">Orchestration Mesh</div>
</div>
<div class="flip-card-back">
<div class="card-back-text">Hierarchical supervisor model executing safe sub-task distribution across specialized API endpoints.</div>
</div>
</div>
</div>

<!-- Card 7 -->
<div class="flip-card" tabindex="0">
<div class="flip-card-inner">
<div class="flip-card-front">
<div class="card-icon">🔐</div>
<div class="card-title">Zero-Trust Guardrail</div>
<div class="card-subtitle">Security Layer</div>
</div>
<div class="flip-card-back">
<div class="card-back-text">Real-time outbound payload interceptor ensuring PII scrubbing and strict prompt injection defenses.</div>
</div>
</div>
</div>

<!-- Card 8 -->
<div class="flip-card" tabindex="0">
<div class="flip-card-inner">
<div class="flip-card-front">
<div class="card-icon">📋</div>
<div class="card-title">Agentic Audit Logger</div>
<div class="card-subtitle">Compliance Node</div>
</div>
<div class="flip-card-back">
<div class="card-back-text">Immutable execution tracing system mapping tool parameters, model reasoning, and system latency.</div>
</div>
</div>
</div>

</div>
"""

st.markdown(project_cards_html, unsafe_allow_html=True)

# 5. TECH FOOTER
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown(
    '<p style="text-align: center; color: #444444; font-size: 0.8rem; font-weight: 400; letter-spacing: 0.5px;">'
    'Architect Log Built with Streamlit &bull; Driven by Anthropic API Tokens &bull; Optimized for Developer Review'
    '</p>',
    unsafe_allow_html=True
)
