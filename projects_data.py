# projects_data.py

DASHBOARD_STYLES = """
<style>
[data-testid="stHeader"], footer, #MainMenu, header {
    visibility: hidden !important;
    height: 0px !important;
}
.block-container {
    max-width: 95% !important;
    padding: 3rem 4rem 2rem 4rem !important;
}
html, body, [data-testid="stAppViewContainer"] {
    background-color: #111111 !important;
    color: #FFFFFF !important;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}
.flip-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 24px;
    width: 100%;
    margin-top: 2rem;
}
.card-link {
    text-decoration: none !important;
    color: inherit !important;
}
.flip-card {
    background-color: transparent;
    height: 220px;
    perspective: 1000px;
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
.flip-card:hover .flip-card-inner, .flip-card:focus .flip-card-inner {
    transform: rotateY(180deg);
}
.flip-card-front, .flip-card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    border-radius: 12px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 24px;
    box-sizing: border-box;
}
.flip-card-front {
    background-color: #1B1B1B;
    border: 1px solid #2D2D2D;
    color: white;
}
.flip-card-back {
    background-color: #E0533C;
    color: white;
    transform: rotateY(180deg);
}
.card-icon { font-size: 2.5rem; margin-bottom: 12px; }
.card-title { font-size: 1.15rem; font-weight: 700; letter-spacing: -0.3px; margin: 0; line-height: 1.2; }
.card-subtitle { color: #888888; font-size: 0.8rem; margin-top: 6px; text-transform: uppercase; letter-spacing: 1px; }
.card-back-text { font-size: 0.95rem; font-weight: 500; line-height: 1.5; }

div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #1B1B1B !important;
    border: 1px solid #2D2D2D !important;
    border-radius: 12px !important;
}
.stCodeBlock, div[data-testid="stCodeBlock"] pre {
    background-color: #0E0E0E !important;
    border: 1px solid #252525 !important;
}
</style>
"""

PROJECTS_HTML_GRID = """
<div class="flip-grid">
<a href="?project=0" target="_self" class="card-link"><div class="flip-card" tabindex="0"><div class="flip-card-inner"><div class="flip-card-front"><div class="card-icon">🧠</div><div class="card-title">Cognitive Layer Router</div><div class="card-subtitle">Architecture Blueprint</div></div><div class="flip-card-back"><div class="card-back-text">Dynamic prompt routing engine optimized for Claude 3.5 multi-turn state evaluations.</div></div></div></div></a>
<a href="?project=1" target="_self" class="card-link"><div class="flip-card" tabindex="0"><div class="flip-card-inner"><div class="flip-card-front"><div class="card-icon">🔌</div><div class="card-title">Custom MCP Gateway</div><div class="card-subtitle">Integration Node</div></div><div class="flip-card-back"><div class="card-back-text">Decoupled protocol runtime mapping structured local context to target tool payloads safely.</div></div></div></div></a>
<a href="?project=2" target="_self" class="card-link"><div class="flip-card" tabindex="0"><div class="flip-card-inner"><div class="flip-card-front"><div class="card-icon">🗂️</div><div class="card-title">Context Synthesizer</div><div class="card-subtitle">Data Worker</div></div><div class="flip-card-back"><div class="card-back-text">Autonomous pipeline transforming unorganized repository files into strict prompt window segments.</div></div></div></div></a>
<a href="?project=3" target="_self" class="card-link"><div class="flip-card" tabindex="0"><div class="flip-card-inner"><div class="flip-card-front"><div class="card-icon">🛠️</div><div class="card-title">Self-Correcting Loop</div><div class="card-subtitle">Execution Pipeline</div></div><div class="flip-card-back"><div class="card-back-text">Error isolation wrapper designed to catch, analyze, and correct tool invocation failures live.</div></div></div></div></a>
<a href="?project=4" target="_self" class="card-link"><div class="flip-card" tabindex="0"><div class="flip-card-inner"><div class="flip-card-front"><div class="card-icon">📊</div><div class="card-title">Token Budget Guardian</div><div class="card-subtitle">Cost Optimizer</div></div><div class="flip-card-back"><div class="card-back-text">Middleware analytics tracker calculating context window decay and optimizing caching parameters.</div></div></div></div></a>
<a href="?project=5" target="_self" class="card-link"><div class="flip-card" tabindex="0"><div class="flip-card-inner"><div class="flip-card-front"><div class="card-icon">🔄</div><div class="card-title">Multi-Agent Swarm Sync</div><div class="card-subtitle">Orchestration Mesh</div></div><div class="flip-card-back"><div class="card-back-text">Hierarchical supervisor model executing safe sub-task distribution across specialized API endpoints.</div></div></div></div></a>
<a href="?project=6" target="_self" class="card-link"><div class="flip-card" tabindex="0"><div class="flip-card-inner"><div class="flip-card-front"><div class="card-icon">🔐</div><div class="card-title">Zero-Trust Guardrail</div><div class="card-subtitle">Security Layer</div></div><div class="flip-card-back"><div class="card-back-text">Real-time outbound payload interceptor ensuring PII scrubbing and strict prompt injection defenses.</div></div></div></div></a>
<a href="?project=7" target="_self" class="card-link"><div class="flip-card" tabindex="0"><div class="flip-card-inner"><div class="flip-card-front"><div class="card-icon">📋</div><div class="card-title">Agentic Audit Logger</div><div class="card-subtitle">Compliance Node</div></div><div class="flip-card-back"><div class="card-back-text">Immutable execution tracing system mapping tool parameters, model reasoning, and system latency.</div></div></div></div></a>
</div>
"""

PROJECTS_LIST = [
    {
        "title": "🧠 Cognitive Layer Router",
        "status": "🎯 Target Pipeline Stage: Core Reasoning",
        "description": "Evaluates raw client incoming request payloads and dynamically assigns optimal token sizing structures.",
        "snippet": "client.messages.create(model='claude-3-5-sonnet', system='Route traffic dynamically...')"
    },
    {
        "title": "🔌 Custom MCP Gateway",
        "status": "📡 Target Pipeline Stage: Protocol Infrastructure",
        "description": "Standardized internal server broker facilitating clean desktop file-system tool read executions.",
        "snippet": "tools=[{'name': 'mcp_gateway_fetch', 'description': 'Secure channel resource abstraction'}]"
    },
    {
        "title": "🗂️ Context Synthesizer",
        "status": "💾 Target Pipeline Stage: Memory & Embedding Management",
        "description": "Splits unorganized system log output sequences cleanly using Claude Prompt Caching parameters.",
        "snippet": "extra_headers={'anthropic-beta': 'prompt-caching-2024-07-31'}"
    },
    {
        "title": "🛠️ Self-Correcting Loop",
        "status": "🔄 Target Pipeline Stage: Exception Handling",
        "description": "Catches bad JSON formatting errors from tool parameters and auto-generates correction context sequences.",
        "snippet": "if response.stop_reason == 'tool_use':\n    # Intercept output parameters and run self-repair loops"
    },
    {
        "title": "📊 Token Budget Guardian",
        "status": "🪙 Target Pipeline Stage: Cost Architecture",
        "description": "Prevents runaway autonomous system loop execution by measuring rolling transaction limits.",
        "snippet": "total_cost = (input_tokens * 3.0 / 1000000) + (output_tokens * 15.0 / 1000000)"
    },
    {
        "title": "🔄 Multi-Agent Swarm Sync",
        "status": "👑 Target Pipeline Stage: Multi-Agent Choreography",
        "description": "Coordinates parallel workers cleanly while keeping track of single user state parameters across separate runtimes.",
        "snippet": "# Master model maps problem branches to worker channels concurrently"
    },
    {
        "title": "🔐 Zero-Trust Guardrail",
        "status": "🛡️ Target Pipeline Stage: System Verification & Security",
        "description": "Sanitizes local client inputs against advanced system instructions override patterns before sending them to the API endpoint.",
        "snippet": "assert 'system_override' not in client_input.lower()"
    },
    {
        "title": "📋 Agentic Audit Logger",
        "status": "📝 Target Pipeline Stage: Reliability Tracking",
        "description": "Logs all tool execution chains, model thoughts, latency traces, and raw JSON text outputs into an organized telemetry server.",
        "snippet": "logger.info(f'Trace ID: {response.id} | Execution Steps Completed')"
    }
]
