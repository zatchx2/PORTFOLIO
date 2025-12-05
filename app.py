import os
import requests
import streamlit as st
from projects_page import render_projects_page

# ================== AI CONFIG (SECURE) ==================
# [UNCHANGED - KEEPING YOUR EXACT API CONFIG]
GROQ_API_KEY = os.getenv("GROQ_API_KEY", None)
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama-3.1-8b-instant"

# ================== AI ASSISTANT FUNCTION (UNCHANGED) ==================
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

# =============== ABSOLUTE BEAST CSS ===============
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

/* BEAST GLOBAL LAYOUT */
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
        radial-gradient(2px 2px at 140px 120px, rgba(168,85,247,0.4), transparent),
        radial-gradient(3px 3px at 200px 50px, rgba(234,179,8,0.3), transparent);
    background-repeat: repeat;
    background-size: 250px 180px;
    opacity: 0.7;
    pointer-events: none;
    z-index: 0;
}

/* Hide defaults */
#MainMenu, footer, header {visibility: hidden;}
.section-line {display: none !important;}

/* HERO BEAST */
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
    z-index: 10;
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

/* BEAST TITLES */
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
}

.subtitle {
    font-size: 1.1rem;
    color: #020617;
    margin: 1rem 0 2rem 0;
    background: rgba(248,250,252,0.98);
    display: inline-block;
    padding: 0.8rem 2rem;
    border-radius: 999px;
    border: 1px solid rgba(255,255,255,0.3);
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    font-weight: 500;
}

/* GLASSMORPHISM SECTIONS */
.section-home, .skill-card {
    background: rgba(255,255,255,0.03);
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 2rem;
    margin-bottom: 2rem;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 20px 60px rgba(0,0,0,0.4);
    animation: sectionRise 0.8s cubic-bezier(0.23,1,0.32,1) forwards;
    opacity: 0;
    transform: translateY(30px);
}

.section-home:nth-child(1), .skill-card:nth-child(1) { animation-delay: 0.1s; }
.section-home:nth-child(2), .skill-card:nth-child(2) { animation-delay: 0.2s; }
.section-home:nth-child(3), .skill-card:nth-child(3) { animation-delay: 0.3s; }

.section-title {
    font-size: 1.4rem;
    font-weight: 800;
    margin-bottom: 1rem;
    color: #f8fafc;
    background: linear-gradient(135deg, #22c55e, #0ea5e9);
    -webkit-background-clip: text;
    background-clip: text;
}

.skill-pill {
    display: inline-flex;
    padding: 0.5rem 1.5rem;
    border-radius: 999px;
    border: 1px solid rgba(255,255,255,0.2);
    margin: 0.3rem 0.5rem 0.3rem 0;
    font-size: 0.9rem;
    font-weight: 600;
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(10px);
    color: #e5e7eb;
    transition: all 0.3s cubic-bezier(0.23,1,0.32,1);
}

.skill-pill:hover {
    background: linear-gradient(135deg, rgba(34,197,94,0.2), rgba(14,165,233,0.2));
    border-color: #22c55e;
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(34,197,94,0.2);
}

/* AI ASSISTANT BEAST */
.ai-assistant {
    background: rgba(15,15,35,0.95);
    backdrop-filter: blur(40px);
    border-radius: 28px;
    padding: 2.5rem;
    border: 1px solid rgba(34,197,94,0.3);
    box-shadow: 0 30px 80px rgba(34,197,94,0.15);
    margin-top: 3rem;
    position: relative;
    overflow: hidden;
    animation: aiPortalOpen 1.2s cubic-bezier(0.23,1,0.32,1);
}

.ai-assistant::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #22c55e, #0ea5e9, #a855f7);
    background-size: 300% 100%;
    animation: gradientShift 3s ease infinite;
}

.ai-title {
    font-size: 1.6rem;
    font-weight: 900;
    background: linear-gradient(135deg, #22c55e, #0ea5e9);
    -webkit-background-clip: text;
    background-clip: text;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 1rem;
}

/* CHAT MESSAGES */
.chat-user {
    background: linear-gradient(135deg, rgba(34,197,94,0.2), rgba(14,165,233,0.2));
    border: 1px solid rgba(34,197,94,0.4);
    border-radius: 20px;
    padding: 1.2rem;
    margin-bottom: 1rem;
    animation: messageSlideIn 0.4s ease-out;
}

.chat-assistant {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 20px;
    padding: 1.2rem;
    margin-bottom: 1rem;
    animation: messageSlideIn 0.4s ease-out 0.1s both;
}

.stChatMessage {
    margin-bottom: 1rem !important;
}

[data-testid="stChatInput"] {
    background: rgba(15,15,35,0.9);
    backdrop-filter: blur(20px);
    border-radius: 20px;
    border: 1px solid rgba(34,197,94,0.3);
    padding: 1rem;
}

/* BUTTONS BEAST */
.stButton > button {
    border-radius: 999px;
    padding: 1rem 2.5rem;
    border: 2px solid transparent;
    background: linear-gradient(135deg, #22c55e, #0ea5e9);
    color: white;
    font-weight: 700;
    font-size: 1rem;
    transition: all 0.4s cubic-bezier(0.23,1,0.32,1);
    position: relative;
    overflow: hidden;
}

.stButton > button:hover {
    transform: translateY(-4px) scale(1.05);
    box-shadow: 0 25px 50px rgba(34,197,94,0.4);
    border-color: rgba(34,197,94,0.6);
}

/* SIDEBAR BEAST */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, rgba(10,10,26,0.95) 0%, rgba(15,15,35,0.95) 100%);
    backdrop-filter: blur(30px);
    border-right: 1px solid rgba(255,255,255,0.1);
}

.sidebar-title {
    font-size: 1.2rem;
    font-weight: 800;
    background: linear-gradient(135deg, #22c55e, #0ea5e9);
    -webkit-background-clip: text;
    background-clip: text;
    margin-bottom: 1rem;
}

.status-chip, .social-pill {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.15);
    transition: all 0.3s ease;
}

.status-chip:hover, .social-pill:hover {
    transform: translateX(8px);
    box-shadow: 0 10px 30px rgba(34,197,94,0.2);
}

.side-arrow-wrapper .stButton > button {
    font-size: 1.8rem;
    padding: 0.8rem;
    background: linear-gradient(135deg, #22c55e, #0ea5e9);
    box-shadow: 0 10px 30px rgba(34,197,94,0.3);
}

.side-arrow-wrapper:hover .stButton > button {
    transform: scale(1.2) rotate(10deg);
}

/* ANIMATIONS BEAST */
@keyframes heroPulse {
    0%, 100% { box-shadow: 0 40px 100px rgba(15,23,42,0.95); transform: scale(1); }
    50% { box-shadow: 0 60px 140px rgba(34,197,94,0.2); transform: scale(1.02); }
}

@keyframes orbFloat { 0%, 100% { transform: scale(1) translateY(0); } 50% { transform: scale(1.1) translateY(-10px); } }
@keyframes scanSweep {
    0% { transform: translateX(-100%); opacity: 0; }
    20% { opacity: 1; }
    80% { opacity: 1; }
    100% { transform: translateX(100%); opacity: 0; }
}

@keyframes facePulse {
    0%, 100% { box-shadow: 0 0 60px rgba(34,197,94,0.6); }
    50% { box-shadow: 0 0 80px rgba(34,197,94,0.9), 0 0 120px rgba(34,197,94,0.4); }
}

@keyframes innerRingSpin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
@keyframes titleShimmer {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

@keyframes sectionRise {
    to { opacity: 1; transform: translateY(0); }
}

@keyframes aiPortalOpen {
    from { opacity: 0; transform: scale(0.9) translateY(50px); }
    to { opacity: 1; transform: scale(1) translateY(0); }
}

@keyframes messageSlideIn {
    from { opacity: 0; transform: translateX(30px); }
    to { opacity: 1; transform: translateX(0); }
}

@keyframes gradientShift {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

/* RESPONSIVE BEAST */
@media (max-width: 900px) {
    .hero { padding: 2rem; }
    .big-title { font-size: 3rem; }
    .face-circle { width: 140px; height: 140px; }
    .section-home, .skill-card { padding: 1.5rem; }
}

@media (max-width: 600px) {
    .side-arrow-wrapper { display: none; }
    .big-title { font-size: 2.5rem; }
}
</style>
""", unsafe_allow_html=True)

# ================== STATE (UNCHANGED) ==================
PAGES = ["Home", "Skills & Background", "Projects", "Contact"]
if "page_index" not in st.session_state:
    st.session_state.page_index = 0
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --------- SIDEBAR (UNCHANGED) ----------
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

current_page_name = PAGES[st.session_state.page_index]

# --------- SIDE ARROWS (UNCHANGED) ----------
left_arrow_col, center_dummy, right_arrow_col = st.columns([0.07, 0.86, 0.07])
with left_arrow_col:
    st.markdown('<div class="side-arrow-wrapper">', unsafe_allow_html=True)
    if st.button("⟵", key="prev_page_arrow"):
        st.session_state.page_index = (st.session_state.page_index - 1) % len(PAGES)
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
with right_arrow_col:
    st.markdown('<div class="side-arrow-wrapper">', unsafe_allow_html=True)
    if st.button("⟶", key="next_page_arrow"):
        st.session_state.page_index = (st.session_state.page_index + 1) % len(PAGES)
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ================== PAGES ==================

# --------- HOME PAGE ----------
if current_page_name == "Home":
    col_hero_left, col_hero_right = st.columns([1.1, 2])
    with col_hero_left:
        st.markdown('<div class="hero">', unsafe_allow_html=True)
        st.markdown('<div class="magic-orb"></div>', unsafe_allow_html=True)
        st.markdown('<div class="magic-sparks"></div>', unsafe_allow_html=True)
        st.markdown('<div class="scan-grid"></div>', unsafe_allow_html=True)
        st.markdown('<div class="scan-line"></div>', unsafe_allow_html=True)
        st.markdown('<div class="face-circle"><div class="face-initials">SP</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="access-text">IDENTITY VERIFIED</div>', unsafe_allow_html=True)
        st.markdown('<div class="access-status">ACCESS GRANTED · PORTFOLIO UNLOCKED</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_hero_right:
        st.markdown('<div class="big-title">Yo, I\'m Sanjay.</div>', unsafe_allow_html=True)
        st.markdown('<div class="subtitle">Programmer · AI & automation enjoyer · Turning raw data & ideas into things that actually feel powerful.</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-home">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">👋 About me</div>', unsafe_allow_html=True)
        st.markdown("I'm a developer who prefers **building real tools** instead of just checking boxes for assignments.<br><br>I like:<br>- Turning **messy data** into clean dashboards<br>- Automating **boring human clicks**<br>- Making stuff that feels smooth, fast and a little overpowered")
        st.markdown('</div>', unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown('<div class="section-home">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">🎯 What I\'m into</div>', unsafe_allow_html=True)
        st.markdown("- AI / ML for useful things, not toy demos<br>- Data analysis & auto-report style tools<br>- Clean, simple experiences (Streamlit enjoyer)")
        st.markdown('</div>', unsafe_allow_html=True)
    with col_b:
        st.markdown('<div class="section-home">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">🚀 What I\'m looking for</div>', unsafe_allow_html=True)
        st.markdown("- Internships / roles where I can ship features fast<br>- Teams working on AI, data or automation<br>- People who care about product, not just buzzwords")
        st.markdown('</div>', unsafe_allow_html=True)

    # --- AI ASSISTANT BEAST ---
    st.markdown('<div class="ai-assistant">', unsafe_allow_html=True)
    st.markdown('<div class="ai-title">🪄 Portfolio AI Assistant</div>', unsafe_allow_html=True)
    st.markdown('<div style="color: #94a3b8; font-size: 1rem; line-height: 1.6;">Ask this assistant anything about me, my skills, projects, studies or what I’m looking for.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    for role, msg in st.session_state.chat_history:
        with st.chat_message(role):
            if role == "user":
                st.markdown(f'<div class="chat-user">{msg}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="chat-assistant">{msg}</div>', unsafe_allow_html=True)

    user_q = st.chat_input("Ask something like: 'What projects has Sanjay done?'")
    if user_q:
        st.session_state.chat_history.append(("user", user_q))
        reply = call_groq_assistant(user_q)
        st.session_state.chat_history.append(("assistant", reply))
        st.rerun()

# --------- SKILLS & BACKGROUND PAGE ----------
elif current_page_name == "Skills & Background":
    st.markdown('<div class="big-title">Skills & Background</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle" style="font-size: 1.2rem; color: #94a3b8; margin-bottom: 3rem; text-align: center;">The toolkit and the journey behind the magic.</div>', unsafe_allow_html=True)

    st.markdown('<div class="skill-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">💻 Programming</div>', unsafe_allow_html=True)
    st.markdown('<span class="skill-pill">Python</span><span class="skill-pill">C</span><span class="skill-pill">SQL</span><span class="skill-pill">JavaScript (basic)</span><span class="skill-pill">Dart / Flutter (basic)</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="skill-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">🧠 Data, AI & Tools</div>', unsafe_allow_html=True)
        st.markdown('<span class="skill-pill">Pandas</span><span class="skill-pill">NumPy</span><span class="skill-pill">Scikit-learn (basic)</span><span class="skill-pill">OpenCV (basic)</span><span class="skill-pill">Streamlit</span><span class="skill-pill">Git & GitHub</span><span class="skill-pill">VS Code</span><span class="skill-pill">Linux</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="skill-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">☁️ Cloud & Networking</div>', unsafe_allow_html=True)
        st.markdown('<span class="skill-pill">AWS (learning)</span><span class="skill-pill">Networking basics</span><span class="skill-pill">HTTP / APIs</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="skill-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎓 Education</div>', unsafe_allow_html=True)
    st.markdown("**Diploma in Computer Engineering**<br>Kuttukaran Polytechnic College — *Completed*<br><br>**Bachelor of Computer Applications (BCA)**<br>Amity University Online — *In progress*")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="skill-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🧪 Experience</div>', unsafe_allow_html=True)
    st.markdown("**Flutter Developer Intern — Zoople Technologies**<br>- Built and tested mobile app features using Flutter & Dart<br>- Integrated Firebase backend services<br>- Implemented UI components from Figma designs<br>- Debugged issues & collaborated with the dev team")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="skill-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📜 Certifications</div>', unsafe_allow_html=True)
    st.markdown("**AWS Solutions Architect – Associate** *(In progress)*<br>- Learning EC2, S3, IAM, VPC, networking and cost optimization.<br><br>**Basics of AI — Certificate**<br>- Intro to AI concepts, use cases and industry relevance.")
    st.markdown('</div>', unsafe_allow_html=True)

# --------- PROJECTS PAGE ----------
elif current_page_name == "Projects":
    render_projects_page()

# --------- CONTACT PAGE ----------
elif current_page_name == "Contact":
    st.markdown('<div class="big-title">Let\'s talk.</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle" style="font-size: 1.2rem; color: #94a3b8; margin-bottom: 3rem; text-align: center;">If you\'re building something fun or hiring, I\'m down to chat.</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-home">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📬 Contact details</div>', unsafe_allow_html=True)
    st.markdown("- 📧 Email: **sanjayps.dev@gmail.com**<br>- 💼 LinkedIn: [Sanjay P S](https://www.linkedin.com/in/sanjay-p-s-932224272)<br>- 🧑‍💻 GitHub: [github.com/zatchx2](https://github.com/zatchx2)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-home">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🤝 What I can help with</div>', unsafe_allow_html=True)
    st.markdown("- Building small AI / automation tools<br>- Cleaning data and generating quick dashboards<br>- Turning rough ideas into working prototypes")
    st.markdown('</div>', unsafe_allow_html=True)
