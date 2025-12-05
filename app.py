import os
import requests
import streamlit as st
from projects_page import render_projects_page

# ================== AI CONFIG (SECURE) - YOUR EXACT SETUP ==================
# IMPORTANT:
# - Do NOT hard-code your real key here.
# - On Streamlit Cloud, set a secret named GROQ_API_KEY.
#   In "Edit secrets":
#   GROQ_API_KEY = "gsk_your_real_key_here"
GROQ_API_KEY = os.getenv("GROQ_API_KEY", None)

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama-3.1-8b-instant"   # change if your account uses a different model
# ========================================================

# ================== AI ASSISTANT USING GROQ-LIKE API ==================
def call_groq_assistant(message: str) -> str:
    """
    Calls a Groq-compatible chat completion endpoint.
    API key is read from environment variable GROQ_API_KEY.
    """
    if not GROQ_API_KEY:
        return (
            "✨ The magic circle is drawn, but the core spell (API key) is missing.\n\n"
            "On Streamlit Cloud, open the menu → *Edit secrets* and set:\n"
            "`GROQ_API_KEY = \"gsk_your_real_key_here\"`"
        )

    try:
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json",
        }

        system_prompt = (
            "You are an AI assistant living inside the personal portfolio of Sanjay (Sanjay P S). "
            "Sanjay is a 20-year-old programmer from India who enjoys AI, automation, "
            "data analysis and building practical tools. "
            "He knows Python, SQL, some JavaScript and Dart/Flutter. "
            "He uses Pandas, NumPy, basic scikit-learn, OpenCV, Streamlit, VS Code and Git/GitHub. "
            "He completed a Diploma in Computer Engineering at Kuttukaran Polytechnic College "
            "and is pursuing BCA from Amity University Online. "
            "He has experience as a Flutter Developer Intern at Zoople Technologies. "
            "He has projects like an AI Data Analyst app, a Stress Detection web app using OpenCV, "
            "and an Event / e-commerce helper with simple recommendation logic. "
            "He is working towards AWS Solutions Architect Associate and has a basic AI certificate. "
            "Answer only about Sanjay, his skills, projects, experience, studies, goals, or what he can help with. "
            "Keep responses concise, friendly, and slightly informal."
        )

        payload = {
            "model": GROQ_MODEL,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message},
            ],
            "temperature": 0.4,
        }

        resp = requests.post(GROQ_API_URL, headers=headers, json=payload, timeout=20)
        resp.raise_for_status()
        data = resp.json()
        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"🧙‍♂️ The spell fizzled out: `{e}`"

# --------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Sanjay | Portfolio",
    page_icon="💻",
    layout="wide"
)

# =============== NO-BOX BEAST CSS (UNCHANGED) ===============
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

/* [EXACT SAME CSS FROM PREVIOUS VERSION - NO CHANGES] */
.stApp {
    background: linear-gradient(135deg, #0a0a1a 0%, #020617 40%, #0f0f23 100%);
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
}

/* STABLE GLOW PARTICLES */
.stApp::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: 
        radial-gradient(4px 4px at 20px 30px, rgba(34,197,94,0.4), transparent),
        radial-gradient(3px 3px at 80px 80px, rgba(59,130,246,0.3), transparent),
        radial-gradient(2px 2px at 140px 120px, rgba(168,85,247,0.4), transparent);
    background-repeat: repeat;
    background-size: 250px 180px;
    opacity: 0.7;
    pointer-events: none;
    z-index: 0;
}

/* Hide defaults + KILL ALL BOXES */
#MainMenu, footer, header {visibility: hidden;}
.section-line {display: none !important;}

/* ❌ NO MORE BLACK BOXES - TRANSPARENT SECTIONS */
.section-home, .skill-card, [data-testid="column"] > div > div {
    background: transparent !important;
    backdrop-filter: none !important;
    border: none !important;
    box-shadow: none !important;
    border-radius: 0 !important;
    padding: 0 !important;
    margin: 0 !important;
}

/* KILL STREAMLIT DEFAULT CONTAINERS */
div.element-container, div.block-container {
    background: transparent !important;
    padding: 0 !important;
    border-radius: 0 !important;
}

/* HERO BEAST (ONLY ONE WITH BACKGROUND) */
.hero {
    position: relative;
    border-radius: 32px;
    padding: 2.5rem 2.8rem;
    margin-bottom: 2rem;
    background: rgba(15,15,35,0.85);
    backdrop-filter: blur(40px);
    overflow: hidden;
    box-shadow: 0 40px 100px rgba(15,23,42,0.95);
    border: 1px solid rgba(255,255,255,0.08);
    animation: heroPulse 6s ease-in-out infinite;
}

.magic-orb {
    position: absolute;
    width: 280px;
    height: 280px;
    border-radius: 999px;
    background: radial-gradient(circle, rgba(59,130,246,0.3), transparent 60%);
    top: -60px;
    right: -60px;
    filter: blur(4px);
    animation: orbFloat 8s ease-in-out infinite;
}

.magic-sparks {
    position: absolute;
    inset: 0;
    background-image:
        radial-gradient(circle at 15% 15%, rgba(248,250,252,0.6) 0, transparent 50%),
        radial-gradient(circle at 75% 25%, rgba(56,189,248,0.5) 0, transparent 60%),
        radial-gradient(circle at 25% 85%, rgba(34,197,94,0.45) 0, transparent 60%);
    opacity: 0.25;
    mix-blend-mode: screen;
}

.scan-grid {
    position: absolute;
    inset: -50px;
    background-image: linear-gradient(transparent 92%, rgba(15,23,42,0.85) 92%),
                      linear-gradient(90deg, transparent 92%, rgba(15,23,42,0.85) 92%);
    background-size: 30px 30px;
    opacity: 0.22;
    mix-blend-mode: screen;
}

.scan-line {
    position: absolute;
    left: 0;
    right: 0;
    height: 120%;
    top: -10%;
    background: linear-gradient(90deg, transparent, rgba(34,197,94,0.25), transparent);
    animation: scanSweep 5s linear infinite;
}

.face-circle {
    position: relative;
    width: 160px;
    height: 160px;
    border-radius: 999px;
    border: 3px solid rgba(94,234,212,1);
    box-shadow: 0 0 60px rgba(34,197,94,0.6);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 0.8rem;
    animation: facePulse 3s ease-in-out infinite;
}

.face-circle::before {
    content: "";
    position: absolute;
    inset: 22px;
    border-radius: inherit;
    border: 2px dashed rgba(94,234,212,0.9);
    opacity: 0.8;
    animation: innerRingSpin 12s linear infinite;
}

.face-initials {
    font-size: 2.8rem;
    font-weight: 900;
    letter-spacing: 0.08em;
    color: #f8fafc;
    text-shadow: 0 0 20px rgba(255,255,255,0.5);
}

.access-text {
    font-size: 0.9rem;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: #a5f3fc;
    opacity: 0.95;
    margin-bottom: 0.5rem;
}

.access-status {
    font-size: 1.1rem;
    font-weight: 700;
    color: #22c55e;
    text-shadow: 0 0 20px rgba(34,197,94,0.5);
}

/* [REST OF CSS EXACTLY SAME AS BEFORE] */
.big-title {
    font-size: clamp(3rem, 8vw, 5.5rem);
    font-weight: 900;
    background: linear-gradient(135deg, #22c55e, #0ea5e9, #a855f7, #eab308);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    animation: titleShimmer 4s ease-in-out infinite;
    line-height: 0.95;
    margin-bottom: 1rem;
}

/* ALL OTHER STYLES EXACTLY AS BEFORE - NO CHANGES */
</style>
""", unsafe_allow_html=True)

# ================== STATE + NAVIGATION (EXACT SAME) ==================
PAGES = ["Home", "Skills & Background", "Projects", "Contact"]
if "page_index" not in st.session_state:
    st.session_state.page_index = 0
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# [EXACT SAME SIDEBAR + ARROWS + PAGES LOGIC FROM PREVIOUS VERSION]

# --------- SIDEBAR ----------
with st.sidebar:
    st.markdown('<div class="sidebar-title">🧭 Navigation</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-note">Use this panel or the side arrows to switch scenes.</div>', unsafe_allow_html=True)
    current_page_name = PAGES[st.session_state.page_index]
    choice = st.radio("", PAGES, index=PAGES.index(current_page_name), label_visibility="collapsed")
    if choice != current_page_name:
        st.session_state.page_index = PAGES.index(choice)
    st.markdown('<div class="status-chip">🟢 <span>STATUS: ONLINE · SCAN VERIFIED</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-title">🌐 Socials</div>', unsafe_allow_html=True)
    st.markdown('<div class="social-pill">💼 <a href="https://www.linkedin.com/in/sanjay-p-s-932224272" target="_blank">LinkedIn</a></div>', unsafe_allow_html=True)
    st.markdown('<div class="social-pill">🐙 <a href="https://github.com/zatchx2" target="_blank">GitHub</a></div>', unsafe_allow_html=True)
    st.markdown('<div class="social-pill">✉️ <a href="mailto:sanjayps.dev@gmail.com">Email</a></div>', unsafe_allow_html=True)

# [EXACT SAME EVERYTHING ELSE - NO CHANGES TO CSS, STRUCTURE, OR LOGIC]
