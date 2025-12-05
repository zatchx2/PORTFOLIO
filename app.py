import os
import requests
import streamlit as st
from projects_page import render_projects_page

# ================== AI CONFIG ================== #
GROQ_API_KEY = os.getenv("GROQ_API_KEY", None)
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama-3.1-8b-instant"


# ================== PAGE CONFIG ================== #
st.set_page_config(
    page_title="Sanjay | Portfolio",
    page_icon="💻",
    layout="wide"
)


# ================== CUSTOM CSS ================== #
st.markdown("""
<style>
/* GLOBAL */
.main {
    background: radial-gradient(circle at top, #020617 0, #020617 30%, #020617 100%);
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    color: #e5e7eb;
}

/* Hide Streamlit UI */
#MainMenu, header, footer {visibility: hidden;}

/* HERO CONTAINER */
.hero {
    position: relative;
    border-radius: 26px;
    padding: 1.7rem 1.9rem;
    margin-bottom: 1.2rem;
    background: rgba(2,6,23,0.9);
    overflow: hidden;
    box-shadow: 0 24px 70px rgba(15,23,42,0.9);
    border: 1px solid rgba(148,163,184,0.5);
}

/* Neon face circle */
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
}
.face-initials {
    font-size: 2.2rem;
    font-weight: 700;
    color: #e5e7eb;
}

.big-title {
    font-size: 2.6rem;
    font-weight: 800;
    background: linear-gradient(90deg, #22c55e, #0ea5e9, #a855f7);
    -webkit-background-clip: text;
    color: transparent;
}

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

/* Sidebar */
[data-testid="stSidebar"] {
    background: #020617;
    border-right: 1px solid rgba(148,163,184,0.6);
}
</style>
""", unsafe_allow_html=True)


# ================== AI CHAT ================== #
def call_groq_assistant(message: str) -> str:
    if not GROQ_API_KEY:
        return "⚠️ API key missing. Set GROQ_API_KEY in secrets."

    try:
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": GROQ_MODEL,
            "messages": [
                {"role": "system", "content":
                 "You are a friendly AI assistant living inside Sanjay's portfolio. "
                 "Answer questions about his skills, projects, studies and goals."},
                {"role": "user", "content": message},
            ],
            "temperature": 0.4,
        }

        resp = requests.post(GROQ_API_URL, headers=headers, json=payload, timeout=20)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error: {e}"


# ================== STATE ================== #
PAGES = ["Home", "Skills & Background", "Projects", "Contact"]

if "page_index" not in st.session_state:
    st.session_state.page_index = 0

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# ================== SIDEBAR ================== #
with st.sidebar:
    current_page_name = PAGES[st.session_state.page_index]

    choice = st.radio("Navigation", PAGES, index=PAGES.index(current_page_name))
    if choice != current_page_name:
        st.session_state.page_index = PAGES.index(choice)


current_page_name = PAGES[st.session_state.page_index]


# ================== PAGE SWITCHING ================== #

# -------- HOME -------- #
if current_page_name == "Home":
    col1, col2 = st.columns([1,2])

    with col1:
        st.markdown('<div class="hero">', unsafe_allow_html=True)
        st.markdown('<div class="face-circle"><div class="face-initials">SP</div></div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="big-title">Yo, I\'m Sanjay.</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="subtitle">Programmer · AI & automation enjoyer · Turning raw data into useful tools.</div>',
            unsafe_allow_html=True,
        )

        st.write("""
- I build things fast  
- I automate boring processes  
- I like stuff that feels powerful but clean  

Currently exploring ML + automation + cloud.
""")

    st.markdown("### 🧠 Ask my AI assistant")

    for role, text in st.session_state.chat_history:
        with st.chat_message(role):
            st.write(text)

    user_q = st.chat_input("Ask anything about me")
    if user_q:
        st.session_state.chat_history.append(("user", user_q))
        reply = call_groq_assistant(user_q)
        st.session_state.chat_history.append(("assistant", reply))
        with st.chat_message("assistant"):
            st.write(reply)


# -------- SKILLS -------- #
elif current_page_name == "Skills & Background":
    st.markdown('<div class="big-title">Skills & Background</div>', unsafe_allow_html=True)

    st.subheader("💻 Programming")
    st.markdown("""
<span class="skill-pill">Python</span>
<span class="skill-pill">C</span>
<span class="skill-pill">SQL</span>
<span class="skill-pill">JavaScript</span>
<span class="skill-pill">Dart / Flutter</span>
""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🧠 Data, AI & Tools")
        st.markdown("""
<span class="skill-pill">Pandas</span>
<span class="skill-pill">NumPy</span>
<span class="skill-pill">Scikit-learn</span>
<span class="skill-pill">OpenCV</span>
<span class="skill-pill">Streamlit</span>
""", unsafe_allow_html=True)

    with col2:
        st.subheader("☁️ Cloud & Networking")
        st.markdown("""
<span class="skill-pill">AWS (learning)</span>
<span class="skill-pill">Networking Basics</span>
""", unsafe_allow_html=True)

    st.subheader("🎓 Education")
    st.write("""
Diploma in Computer Engineering  
BCA at Amity University Online (in progress)
""")

    st.subheader("🧪 Experience")
    st.write("""
Flutter Developer Intern @ Zoople Technologies
""")


# -------- PROJECTS -------- #
elif current_page_name == "Projects":
    render_projects_page()


# -------- CONTACT -------- #
elif current_page_name == "Contact":
    st.markdown('<div class="big-title">Let\'s talk.</div>', unsafe_allow_html=True)

    st.write("""
📧 Email: **sanjayps.dev@gmail.com**  
💼 LinkedIn: https://www.linkedin.com/in/sanjay-p-s-932224272  
🐙 GitHub: https://github.com/zatchx2  
""")

