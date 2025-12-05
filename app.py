import os
import requests
import streamlit as st
from projects_page import render_projects_page

# ================== AI CONFIG (SECURE) ==================
GROQ_API_KEY = os.getenv("GROQ_API_KEY", None)
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama-3.1-8b-instant"

# --------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Sanjay | Portfolio",
    page_icon="💻",
    layout="wide"
)

# --------- CUSTOM CSS (UPDATED FOR PROJECTS HERO) ----------
st.markdown("""
<style>
/* GLOBAL LAYOUT */
.main {
    background: radial-gradient(circle at top, #020617 0, #020617 30%, #020617 100%);
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    color: #e5e7eb;
}

/* Hide Streamlit default menu & footer */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* HERO / FACE SCAN SECTION */
.hero {
    position: relative;
    border-radius: 26px;
    padding: 1.7rem 1.9rem;
    margin-bottom: 1.2rem;
    background: radial-gradient(circle at top, #020617 0, #020617 35%, #020617 100%);
    overflow: hidden;
    box-shadow: 0 24px 70px rgba(15,23,42,0.9);
    border: 1px solid rgba(148,163,184,0.5);
    color: #e5e7eb;
}
.section-line{
    display: none !important;
}

/* Magic / arcane ambience */
.magic-orb {
    position: absolute;
    width: 220px;
    height: 220px;
    border-radius: 999px;
    background: radial-gradient(circle, rgba(59,130,246,0.25), transparent 60%);
    top: -40px;
    right: -40px;
    filter: blur(3px);
    animation: orbPulse 5s ease-in-out infinite;
    pointer-events: none;
}
.magic-sparks {
    position: absolute;
    inset: 0;
    background-image:
      radial-gradient(circle at 10% 10%, rgba(248,250,252,0.5) 0, transparent 45%),
      radial-gradient(circle at 80% 30%, rgba(56,189,248,0.45) 0, transparent 55%),
      radial-gradient(circle at 30% 80%, rgba(34,197,94,0.4) 0, transparent 55%);
    opacity: 0.18;
    mix-blend-mode: screen;
    pointer-events: none;
}

/* Fake face scan grid */
.scan-grid {
    position: absolute;
    inset: -40px;
    background-image: linear-gradient(transparent 90%, rgba(15,23,42,0.8) 90%),
                      linear-gradient(90deg, transparent 90%, rgba(15,23,42,0.8) 90%);
    background-size: 26px 26px;
    opacity: 0.18;
    mix-blend-mode: screen;
}

/* Moving scan line */
.scan-line {
    position: absolute;
    left: 0;
    right: 0;
    height: 110%;
    top: -10%;
    background: linear-gradient(90deg, transparent, rgba(34,197,94,0.18), transparent);
    animation: scanMove 4s linear infinite;
}

/* Neon circle "face" */
.face-circle {
    position: relative;
    width: 130px;
    height: 130px;
    border-radius: 999px;
    border: 2px solid rgba(94,234,212,0.9);
    box-shadow: 0 0 40px rgba(34,197,94,0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 0.4rem;
}
.face-circle::before {
    content: "";
    position: absolute;
    inset: 18px;
    border-radius: inherit;
    border: 1px dashed rgba(94,234,212,0.9);
    opacity: 0.7;
}
.face-initials {
    font-size: 2.2rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    color: #e5e7eb;
}

/* "Face recognized" text */
.access-text {
    font-size: 0.8rem;
    letter-spacing: 0.24em;
    text-transform: uppercase;
    color: #a5f3fc;
    opacity: 0.9;
}
.access-status {
    margin-top: 0.3rem;
    font-size: 0.95rem;
    font-weight: 600;
    color: #22c55e;
}

/* Big animated title */
.big-title {
    font-size: 2.6rem;
    font-weight: 800;
    background: linear-gradient(90deg, #22c55e, #0ea5e9, #a855f7);
    -webkit-background-clip: text;
    color: transparent;
    animation: fadeDown 0.7s ease-out;
}

/* Subtitle under main title: BLACK text on light pill */
.subtitle {
    font-size: 0.95rem;
    color: #020617;
    margin-top: 0.5rem;
    margin-bottom: 1.1rem;
    background: rgba(248,250,252,0.97);
    display: inline-block;
    padding: 0.4rem 1.0rem;
    border-radius: 999px;
    border: 1px solid rgba(148,163,184,0.4);
}

/* PROJECTS PAGE OVERRIDE - Ensure hero fits main theme */
.proj-page {
    max-width: 1100px;
    margin: 0 auto;
    padding: 0 1rem;
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
    min-height: 100vh;
    position: relative;
    overflow-x: hidden;
    background: transparent;
}

/* Override particle background to match main theme */
.proj-page::before {
    background-image: 
        radial-gradient(2px 2px at 20px 30px, rgba(34,197,94,0.6), transparent),
        radial-gradient(2px 2px at 40px 70px, rgba(59,130,246,0.5), transparent),
        radial-gradient(1px 1px at 90px 40px, rgba(168,85,247,0.7), transparent),
        radial-gradient(1px 1px at 130px 80px, rgba(234,179,8,0.6), transparent);
}

/* HERO SECTION - Match main dark theme */
.hero-section {
    position: relative;
    z-index: 1;
    min-height: 80vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 3rem 2rem;
    background: rgba(2, 6, 23, 0.95);
    backdrop-filter: blur(40px);
    border: 1px solid rgba(148,163,184,0.15);
    border-radius: 32px;
    margin: 1rem 0;
    box-shadow: 0 0 100px rgba(34, 197, 94, 0.12);
    animation: heroPulse 4s ease-in-out infinite;
}

.hero-kicker {
    font-size: clamp(0.9rem, 2vw, 1.1rem);
    font-weight: 600;
    letter-spacing: 0.4em;
    text-transform: uppercase;
    background: linear-gradient(135deg, #22c55e, #0ea5e9, #a855f7);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    margin-bottom: 1.5rem;
    animation: kickerFloat 3s ease-in-out infinite;
}

.hero-title {
    font-size: clamp(4rem, 10vw, 8rem);
    font-weight: 900;
    background: linear-gradient(135deg, #e5e7eb 0%, #f8fafc 40%, #e2e8f0 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    letter-spacing: -0.05em;
    line-height: 0.9;
    margin-bottom: 1rem;
    position: relative;
}

.hero-subtitle {
    font-size: clamp(1.1rem, 3vw, 1.6rem);
    color: #94a3b8;
    font-weight: 300;
    max-width: 800px;
    line-height: 1.6;
    margin-bottom: 3rem;
}

.hero-cta {
    display: inline-flex;
    padding: 1.2rem 3rem;
    background: linear-gradient(135deg, rgba(34,197,94,0.18), rgba(14,165,233,0.18));
    backdrop-filter: blur(20px);
    border: 2px solid rgba(34,197,94,0.25);
    border-radius: 50px;
    font-size: 1.1rem;
    font-weight: 700;
    color: #22c55e;
    text-decoration: none;
    transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1);
    position: relative;
    overflow: hidden;
}

.hero-cta:hover {
    background: linear-gradient(135deg, rgba(34,197,94,0.35), rgba(14,165,233,0.35));
    border-color: #22c55e;
    transform: translateY(-4px);
    box-shadow: 0 20px 40px rgba(34,197,94,0.3);
}

/* Rest of your existing styles remain unchanged... */
.skill-card, .section-home {
    background: transparent;
    border-radius: 0;
    padding: 0;
    border: none;
    box-shadow: none;
    margin-bottom: 0.5rem;
    max-width: 100%;
}

.section-title {
    font-size: 1.2rem;
    font-weight: 700;
    margin-bottom: 0.4rem;
    color: #e5e7eb;
}

.skill-pill {
    display: inline-block;
    padding: 0.32rem 0.9rem;
    border-radius: 999px;
    border: 1px solid rgba(148,163,184,0.7);
    margin: 0.15rem 0.25rem;
    font-size: 0.85rem;
    background: rgba(15,23,42,0.9);
    color: #e5e7eb;
}

/* Animations */
@keyframes revealUp {
    from { opacity: 0; transform: translateY(12px); }
    to   { opacity: 1; transform: translateY(0px); }
}
@keyframes fadeDown {
    from { opacity: 0; transform: translateY(-10px); }
    to   { opacity: 1; transform: translateY(0px); }
}
@keyframes scanMove {
    0% { transform: translateX(-70%); opacity: 0; }
    15% { opacity: 1; }
    50% { transform: translateX(70%); opacity: 1; }
    85% { opacity: 1; }
    100% { transform: translateX(120%); opacity: 0; }
}
@keyframes orbPulse {
    0%   { opacity: 0.2; transform: scale(1); }
    50%  { opacity: 0.55; transform: scale(1.07); }
    100% { opacity: 0.2; transform: scale(1); }
}
@keyframes heroPulse {
    0%, 100% { 
        box-shadow: 0 0 100px rgba(34,197,94,0.12);
        transform: scale(1);
    }
    50% { 
        box-shadow: 0 0 150px rgba(34,197,94,0.25), 0 0 200px rgba(14,165,233,0.15);
        transform: scale(1.02);
    }
}
@keyframes kickerFloat {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-8px); }
}

/* Mobile */
@media (max-width: 768px) {
    .hero-section { margin: 1rem; padding: 2rem 1rem; min-height: 70vh; }
}
</style>
""", unsafe_allow_html=True)

# ================== AI ASSISTANT (UNCHANGED) ==================
def call_groq_assistant(message: str) -> str:
    if not GROQ_API_KEY:
        return (
            "✨ The magic circle is drawn, but the core spell (API key) is missing.\n\n"
            "On Streamlit Cloud, open the menu → *Edit secrets* and set:\n"
            "`GROQ_API_KEY = \"gsk_your_real_key_here\"`"
        )
    try:
        headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
        system_prompt = (
            "You are an AI assistant living inside the personal portfolio of Sanjay (Sanjay P S). "
            "Keep responses concise, friendly, and slightly informal."
        )
        payload = {
            "model": GROQ_MODEL,
            "messages": [{"role": "system", "content": system_prompt}, {"role": "user", "content": message}],
            "temperature": 0.4,
        }
        resp = requests.post(GROQ_API_URL, headers=headers, json=payload, timeout=20)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"🧙‍♂️ The spell fizzled out: `{e}`"

# ================== STATE + NAVIGATION (UNCHANGED) ==================
PAGES = ["Home", "Skills & Background", "Projects", "Contact"]

if "page_index" not in st.session_state:
    st.session_state.page_index = 0
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar (unchanged)
with st.sidebar:
    st.markdown('<div class="sidebar-title">🧭 Navigation</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-note">Use this panel or the side arrows to switch scenes.</div>', unsafe_allow_html=True)
    choice = st.radio("", PAGES, index=st.session_state.page_index, label_visibility="collapsed")
    if choice != PAGES[st.session_state.page_index]:
        st.session_state.page_index = PAGES.index(choice)
    
    st.markdown('<div class="status-chip">🟢 <span>STATUS: ONLINE · SCAN VERIFIED</span></div>', unsafe_allow_html=True)
    # Social links (unchanged)...

current_page_name = PAGES[st.session_state.page_index]

# Side arrows (unchanged)...
left_arrow_col, center_dummy, right_arrow_col = st.columns([0.07, 0.86, 0.07])
with left_arrow_col:
    if st.button("⟵", key="prev_page_arrow"):
        st.session_state.page_index = (st.session_state.page_index - 1) % len(PAGES)
        st.rerun()
with right_arrow_col:
    if st.button("⟶", key="next_page_arrow"):
        st.session_state.page_index = (st.session_state.page_index + 1) % len(PAGES)
        st.rerun()

# ================== PAGES (Home + Skills + Contact unchanged, Projects fixed) ==================

if current_page_name == "Home":
    # [Your existing Home page code unchanged...]
    pass

elif current_page_name == "Skills & Background":
    # [Your existing Skills page code unchanged...]
    pass

elif current_page_name == "Projects":
    render_projects_page()

elif current_page_name == "Contact":
    # [Your existing Contact page code unchanged...]
    pass
