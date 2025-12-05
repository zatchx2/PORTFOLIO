import os
import requests
import streamlit as st

# ================== AI CONFIG (SECURE) ==================
# IMPORTANT:
# - Do NOT hard-code your real key here.
# - On Streamlit Cloud, set a secret named GROQ_API_KEY.
#   In "Edit secrets":
#   GROQ_API_KEY = "gsk_your_real_key_here"
GROQ_API_KEY = os.getenv("GROQ_API_KEY", None)

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama-3.1-8b-instant"   # change if your account uses a different model
# ========================================================


# --------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Sanjay | Portfolio",
    page_icon="💻",
    layout="wide"
)

# --------- CUSTOM CSS ----------
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

/* Generic sections (dark glass cards) */
             /* 🔥 limit width */


.skill-card {
    background: transparent;
    border-radius: 0;
    padding: 0;
    border: none;
    box-shadow: none;
    margin-bottom: 0.5rem;
    max-width: 100%;
}             /* 🔥 narrower card */


/* Home page inline sections */
.section-home {
    background: transparent;
    border-radius: 0;
    padding: 0.4rem 0;
    margin-bottom: 0.5rem;
    border: none;
    box-shadow: none;
    color: #e5e7eb;
}
.section-home .section-title {
    color: #e5e7eb;
}

/* Titles */
.section-title {
    font-size: 1.2rem;
    font-weight: 700;
    margin-bottom: 0.4rem;
    color: #e5e7eb;
}

.section-subtitle {
    font-size: 1rem;
    color: #a5b4fc;
    margin-bottom: 0.8rem;
}

/* Skill card */
.skill-card {
    background: rgba(15,23,42,0.9);
    border-radius: 18px;
    padding: 1rem 1.2rem;
    border: 1px solid rgba(148,163,184,0.5);
    box-shadow: 0 14px 35px rgba(15,23,42,0.9);
    margin-bottom: 1rem;
}

/* Skill pill */
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
.skill-pill:hover {
    background: rgba(37,99,235,0.25);
    border-color: rgba(129,140,248,0.9);
}

/* Project card */
.project-card {
    border-radius: 18px;
    padding: 0.9rem 1rem;
    border: 1px solid rgba(148,163,184,0.6);
    background: rgba(15,23,42,0.95);
    margin-bottom: 0.7rem;
    color: #e5e7eb;
    box-shadow: 0 14px 35px rgba(15,23,42,0.9);
}
.project-title {
    font-weight: 650;
    font-size: 1rem;
    color: #e5e7eb;
}
.project-tech {
    font-size: 0.8rem;
    color: #9ca3af;
    margin-bottom: 0.2rem;
}
.project-desc {
    font-size: 0.9rem;
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

/* Buttons */
.stButton>button {
    border-radius: 999px;
    padding: 0.45rem 1.4rem;
    border: 1px solid rgba(148,163,184,0.7);
    background: linear-gradient(135deg, #22c55e, #0ea5e9);
    color: white;
    font-weight: 600;
    cursor: pointer;
}
.stButton>button:hover {
    transform: translateY(-1px) scale(1.01);
    box-shadow: 0 18px 40px rgba(34,197,94,0.4);
}

/* Links */
a {
    color: #38bdf8;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}

/* SIDEBAR STYLING */
[data-testid="stSidebar"] {
    background: radial-gradient(circle at top, #020617 0, #020617 60%, #020617 100%);
    border-right: 1px solid rgba(148,163,184,0.6);
}
.sidebar-title {
    font-size: 1rem;
    font-weight: 600;
    color: #e5e7eb;
    margin-bottom: 0.4rem;
}
.nav-note {
    font-size: 0.75rem;
    color: #9ca3af;
    margin-bottom: 0.7rem;
}

/* creative little "status chip" instead of separation line */
.status-chip {
    margin-top: 0.8rem;
    margin-bottom: 0.8rem;
    padding: 0.35rem 0.7rem;
    border-radius: 999px;
    border: 1px solid rgba(45,212,191,0.7);
    background: rgba(15,23,42,0.9);
    font-size: 0.75rem;
    color: #a5f3fc;
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
}

/* Social pills */
.social-pill {
    padding: 0.35rem 0.6rem;
    border-radius: 999px;
    border: 1px solid rgba(148,163,184,0.7);
    background: rgba(15,23,42,0.9);
    font-size: 0.8rem;
    margin-bottom: 0.3rem;
}
.social-pill a {
    color: #e5e7eb !important;
}

/* SIDE ARROW CONTAINERS */
.side-arrow-wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
}
.side-arrow-wrapper .stButton>button {
    font-size: 1.6rem;
    padding: 0.1rem 0.5rem;
    border-radius: 999px;
    background: radial-gradient(circle at top left, #22c55e, #0ea5e9);
    border: 1px solid rgba(148,163,184,0.5);
}
.side-arrow-wrapper {
    opacity: 0.35;
    transition: opacity 0.2s ease-out, transform 0.2s ease-out;
}
.side-arrow-wrapper:hover {
    opacity: 1;
    transform: translateY(-1px);
}

/* Remove thick default horizontal rules */
hr {
    border: none;
    margin: 0;
}

/* ================= RESPONSIVENESS ================= */
@media (max-width: 900px) {
    .hero {
        padding: 1.1rem 1.2rem;
        margin-bottom: 1.0rem;
    }
    .big-title {
        font-size: 2rem;
    }
    .subtitle {
        font-size: 0.85rem;
        padding: 0.3rem 0.8rem;
    }
    .face-circle {
        width: 110px;
        height: 110px;
    }
    .magic-orb {
        width: 150px;
        height: 150px;
        top: -20px;
        right: -20px;
    }
}

/* super-small screens */
@media (max-width: 600px) {
    .big-title {
        font-size: 1.7rem;
    }
    .hero {
        padding: 0.9rem 1rem;
    }
    .subtitle {
        max-width: 100%;
    }
    /* hide side arrows on small screens */
    .side-arrow-wrapper {
        display: none;
    }
}
</style>
""", unsafe_allow_html=True)


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


# ================== STATE: PAGE + CHAT ==================
PAGES = ["Home", "Skills & Background", "Projects", "Contact"]

if "page_index" not in st.session_state:
    st.session_state.page_index = 0

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# --------- SIDEBAR (NAVIGATION) ----------
with st.sidebar:
    st.markdown('<div class="sidebar-title">🧭 Navigation</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-note">Use this panel or the side arrows to switch scenes.</div>', unsafe_allow_html=True)

    current_page_name = PAGES[st.session_state.page_index]
    choice = st.radio("", PAGES, index=PAGES.index(current_page_name), label_visibility="collapsed")
    if choice != current_page_name:
        st.session_state.page_index = PAGES.index(choice)

    st.markdown(
        '<div class="status-chip">🟢 <span>STATUS: ONLINE · SCAN VERIFIED</span></div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="sidebar-title">🌐 Socials</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="social-pill">💼 '
        '<a href="https://www.linkedin.com/in/sanjay-p-s-932224272" target="_blank">LinkedIn</a></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="social-pill">🐙 '
        '<a href="https://github.com/zatchx2" target="_blank">GitHub</a></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="social-pill">✉️ '
        '<a href="mailto:sanjayps.dev@gmail.com">Email</a></div>',
        unsafe_allow_html=True,
    )

current_page_name = PAGES[st.session_state.page_index]

# --------- BIG SIDE ARROWS (TOP OF MAIN PAGE) ----------
left_arrow_col, center_dummy, right_arrow_col = st.columns([0.07, 0.86, 0.07])

with left_arrow_col:
    st.markdown('<div class="side-arrow-wrapper">', unsafe_allow_html=True)
    if st.button("⟵", key="prev_page_arrow"):
        st.session_state.page_index = (st.session_state.page_index - 1) % len(PAGES)
        current_page_name = PAGES[st.session_state.page_index]
    st.markdown('</div>', unsafe_allow_html=True)

with right_arrow_col:
    st.markdown('<div class="side-arrow-wrapper">', unsafe_allow_html=True)
    if st.button("⟶", key="next_page_arrow"):
        st.session_state.page_index = (st.session_state.page_index + 1) % len(PAGES)
        current_page_name = PAGES[st.session_state.page_index]
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

        st.markdown("</div>", unsafe_allow_html=True)

    with col_hero_right:
        st.markdown('<div class="big-title">Yo, I\'m Sanjay.</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="subtitle">'
            'Programmer · AI & automation enjoyer · Turning raw data & ideas into things that actually feel powerful.'
            '</div>',
            unsafe_allow_html=True,
        )

        st.markdown('<div class="section-home">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">👋 About me</div>', unsafe_allow_html=True)
        st.markdown(
            """
I'm a developer who prefers **building real tools** instead of just checking boxes for assignments.

I like:
- Turning **messy data** into clean dashboards  
- Automating **boring human clicks**  
- Making stuff that feels smooth, fast and a little overpowered  
            """
        )
        st.markdown("</div>", unsafe_allow_html=True)

    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown('<div class="section-home">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">🎯 What I\'m into</div>', unsafe_allow_html=True)
        st.markdown(
            """
- AI / ML for useful things, not toy demos  
- Data analysis & auto-report style tools  
- Clean, simple experiences (Streamlit enjoyer)  
            """
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col_b:
        st.markdown('<div class="section-home">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">🚀 What I\'m looking for</div>', unsafe_allow_html=True)
        st.markdown(
            """
- Internships / roles where I can ship features fast  
- Teams working on AI, data or automation  
- People who care about product, not just buzzwords  
            """
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # --- AI ASSISTANT CARD ---
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🪄 Portfolio AI Assistant</div>', unsafe_allow_html=True)
    st.write(
        "Ask this assistant anything about me, my skills, projects, studies or what I’m looking for. "
       
    )

    for role, msg in st.session_state.chat_history:
        with st.chat_message(role):
            st.write(msg)

    user_q = st.chat_input("Ask something like: 'What projects has Sanjay done?'")
    if user_q:
        st.session_state.chat_history.append(("user", user_q))
        reply = call_groq_assistant(user_q)
        st.session_state.chat_history.append(("assistant", reply))
        with st.chat_message("assistant"):
            st.write(reply)

    st.markdown("</div>", unsafe_allow_html=True)


# --------- SKILLS & BACKGROUND PAGE ----------
elif current_page_name == "Skills & Background":
    st.markdown('<div class="big-title">Skills & Background</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">The toolkit and the journey behind the magic.</div>',
        unsafe_allow_html=True,
    )

    # Programming
    st.markdown('<div class="skill-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">💻 Programming</div>', unsafe_allow_html=True)
    st.markdown(
        """
<span class="skill-pill">Python</span>
<span class="skill-pill">C</span>
<span class="skill-pill">SQL</span>
<span class="skill-pill">JavaScript (basic)</span>
<span class="skill-pill">Dart / Flutter (basic)</span>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="skill-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">🧠 Data, AI & Tools</div>', unsafe_allow_html=True)
        st.markdown(
            """
<span class="skill-pill">Pandas</span>
<span class="skill-pill">NumPy</span>
<span class="skill-pill">Scikit-learn (basic)</span>
<span class="skill-pill">OpenCV (basic)</span>
<span class="skill-pill">Streamlit</span>
<span class="skill-pill">Git & GitHub</span>
<span class="skill-pill">VS Code</span>
<span class="skill-pill">Linux</span>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="skill-card">', unsafe_allow_html=True)
        st.markmarkdown = st.markdown
        st.markmarkdown('<div class="section-title">☁️ Cloud & Networking</div>', unsafe_allow_html=True)
        st.markmarkdown(
            """
<span class="skill-pill">AWS (learning)</span>
<span class="skill-pill">Networking basics</span>
<span class="skill-pill">HTTP / APIs</span>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # Education
    st.markdown('<div class="skill-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎓 Education</div>', unsafe_allow_html=True)
    st.markdown(
        """
**Diploma in Computer Engineering**  
Kuttukaran Polytechnic College — *Completed*

**Bachelor of Computer Applications (BCA)**  
Amity University Online — *In progress*
        """
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # Experience
    st.markdown('<div class="skill-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🧪 Experience</div>', unsafe_allow_html=True)
    st.markdown(
        """
**Flutter Developer Intern — Zoople Technologies**  
- Built and tested mobile app features using Flutter & Dart  
- Integrated Firebase backend services  
- Implemented UI components from Figma designs  
- Debugged issues & collaborated with the dev team  
        """
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # Certifications
    st.markdown('<div class="skill-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📜 Certifications</div>', unsafe_allow_html=True)
    st.markdown(
        """
**AWS Solutions Architect – Associate** *(In progress)*  
- Learning EC2, S3, IAM, VPC, networking and cost optimization.

**Basics of AI — Certificate**  
- Intro to AI concepts, use cases and industry relevance.
        """
    )
    st.markdown("</div>", unsafe_allow_html=True)


# --------- PROJECTS PAGE ----------
elif current_page_name == "Projects":
    st.markdown('<div class="big-title">Things I\'ve built</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Projects that actually do something, not just print "Hello World".</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🧠 AI / Data</div>', unsafe_allow_html=True)

    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown('<div class="project-title">AI Data Analyst</div>', unsafe_allow_html=True)
    st.markdown('<div class="project-tech">Python · Pandas · Streamlit</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="project-desc">Upload raw CSV → app automatically cleans, structures and visualizes data with summary insights. Goal: kill messy manual Excel work.</div>',
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown('<div class="project-title">Stress Detection Web App</div>', unsafe_allow_html=True)
    st.markdown('<div class="project-tech">Python · OpenCV · ML</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="project-desc">Real-time facial analysis through webcam to estimate stress levels using basic models and an OpenCV pipeline.</div>',
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown('<div class="project-title">Event / E-commerce Helper</div>', unsafe_allow_html=True)
    st.markdown('<div class="project-tech">JavaScript · PHP · Basic ML / heuristics</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="project-desc">Platform logic for managing events / products and ranking options based on simple user-like signals.</div>',
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# --------- CONTACT PAGE ----------
elif current_page_name == "Contact":
    st.markdown('<div class="big-title">Let\'s talk.</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">If you\'re building something fun or hiring, I\'m down to chat.</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📬 Contact details</div>', unsafe_allow_html=True)
    st.markdown(
        """
- 📧 Email: **sanjayps.dev@gmail.com**  
- 💼 LinkedIn: [Sanjay P S](https://www.linkedin.com/in/sanjay-p-s-932224272)  
- 🧑‍💻 GitHub: [github.com/zatchx2](https://github.com/zatchx2)  
        """
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🤝 What I can help with</div>', unsafe_allow_html=True)
    st.markdown(
        """
- Building small AI / automation tools  
- Cleaning data and generating quick dashboards  
- Turning rough ideas into working prototypes  
        """
    )
    st.markdown("</div>", unsafe_allow_html=True)





