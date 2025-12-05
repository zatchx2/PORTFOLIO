# projects_page.py
import streamlit as st

# ================== STYLES ==================
PROJECT_CSS = """
<style>

/* Page wrapper animation */
.page-fade {
    animation: fadeIn 0.6s ease-out;
}

/* Title styling */
.big-title {
    font-size: 2.4rem;
    font-weight: 800;
    margin-bottom: 0.4rem;
    background: linear-gradient(90deg, #0ea5e9, #22c55e, #a855f7);
    -webkit-background-clip: text;
    color: transparent;
    animation: slideDown 0.6s ease-out;
}

/* Subtitle */
.section-subtitle {
    font-size: 0.95rem;
    color: #94a3b8;
    margin-bottom: 1.8rem;
    opacity: 0.9;
}

/* Project layout grid */
.project-wrapper {
    display: flex;
    flex-direction: column;
    gap: 1.2rem;
}

/* Card */
.project-card {
    background: rgba(15, 23, 42, 0.85);
    border: 1px solid rgba(148,163,184,0.25);
    border-radius: 18px;
    padding: 1.1rem 1.3rem;
    box-shadow: 0 15px 40px rgba(0,0,0,0.55);
    backdrop-filter: blur(12px);
    transition: transform 0.18s ease, box-shadow 0.18s ease;
    position: relative;
    overflow: hidden;
}

/* Glow hover */
.project-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 25px 60px rgba(14, 165, 233, 0.25);
}

/* Scan line effect */
.project-card::before {
    content: "";
    position: absolute;
    top: -60%;
    left: 0;
    right: 0;
    height: 200%;
    background: linear-gradient(transparent, rgba(56, 189, 248, 0.08), transparent);
    animation: scan 5s linear infinite;
}

/* Title */
.project-title {
    font-size: 1.2rem;
    font-weight: 700;
    color: #e2e8f0;
    margin-bottom: 0.2rem;
}

/* Tech */
.project-tech {
    font-size: 0.83rem;
    color: #94a3b8;
    margin-bottom: 0.45rem;
}

/* Description */
.project-desc {
    font-size: 0.96rem;
    color: #cbd5e1;
    line-height: 1.45rem;
}

/* ---- Animations ---- */
@keyframes fadeIn {
    from { opacity: 0; }
    to   { opacity: 1; }
}

@keyframes slideDown {
    from { opacity: 0; transform: translateY(-12px); }
    to   { opacity: 1; transform: translateY(0); }
}

@keyframes scan {
    0% { transform: translateY(-80%); opacity: 0; }
    30% { opacity: 1; }
    60% { transform: translateY(80%); opacity: 0; }
    100% { opacity: 0; }
}

</style>
"""

# ================== PROJECT DATA ==================
PROJECTS = [
    {
        "title": "AI Data Analyst",
        "tech": "Python · Pandas · Streamlit",
        "desc": "Upload CSV → get auto-cleaned summaries, charts, insights. Unblocks fast analysis without Excel headaches.",
    },
    {
        "title": "Stress Detection Web App",
        "tech": "Python · OpenCV · ML",
        "desc": "Real-time facial stress estimation with webcam. Uses lightweight models and heuristic analysis.",
    },
    {
        "title": "Event / E-commerce Helper",
        "tech": "JavaScript · PHP · Simple ML",
        "desc": "Ranks products or events based on user preference signals using heuristic scoring instead of complex ML.",
    },
]

# ================== PAGE RENDER ==================
def render_projects_page():
    st.markdown(PROJECT_CSS, unsafe_allow_html=True)

    st.markdown('<div class="page-fade">', unsafe_allow_html=True)

    st.markdown(
        '<div class="big-title">Things I\'ve built</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="section-subtitle">Small tools, built fast — made to solve real problems.</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="project-wrapper">', unsafe_allow_html=True)

    for p in PROJECTS:
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="project-title">{p["title"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="project-tech">{p["tech"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="project-desc">{p["desc"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
