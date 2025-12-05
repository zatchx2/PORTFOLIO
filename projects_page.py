# projects_page.py
import streamlit as st

# =============== CSS (ONLY FOR PROJECT PAGE) ===============
PROJECTS_CSS = """
<style>
/* Whole project page container */
.project-page {
    animation: pageFade 0.6s ease-out;
}

/* Title styling (reuse portfolio vibe) */
.project-page-title {
    font-size: 2.1rem;
    font-weight: 800;
    background: linear-gradient(90deg, #0ea5e9, #22c55e, #a855f7);
    -webkit-background-clip: text;
    color: transparent;
    margin-bottom: 0.3rem;
}

.project-page-subtitle {
    font-size: 0.95rem;
    color: #94a3b8;
    margin-bottom: 1.4rem;
    opacity: 0.9;
}

/* List container */
.project-list {
    display: flex;
    flex-direction: column;
    gap: 0.9rem;
}

/* Each project row (no big bar, just text + thin line) */
.project-row {
    padding: 0.55rem 0;
    border-bottom: 1px solid rgba(148,163,184,0.35);
    position: relative;
    overflow: hidden;
    animation: rowUp 0.4s ease-out;
}

/* subtle hover motion */
.project-row:hover {
    transform: translateY(-1px);
}

/* Left accent line */
.project-row::before {
    content: "";
    position: absolute;
    left: 0;
    top: 0.55rem;
    bottom: 0.55rem;
    width: 2px;
    background: linear-gradient(#22c55e, #0ea5e9);
    opacity: 0.0;
    transform: translateX(-4px);
    transition: all 0.2s ease-out;
}

/* On hover, show accent line */
.project-row:hover::before {
    opacity: 1;
    transform: translateX(0);
}

/* Title text */
.project-title {
    font-size: 1.05rem;
    font-weight: 650;
    color: #e5e7eb;
    position: relative;
    display: inline-block;
}

/* Animated underline under title */
.project-title::after {
    content: "";
    position: absolute;
    left: 0;
    bottom: -2px;
    height: 2px;
    width: 100%;
    background: linear-gradient(90deg, #22c55e, #0ea5e9);
    transform-origin: left;
    transform: scaleX(0);
    transition: transform 0.18s ease-out;
}

.project-row:hover .project-title::after {
    transform: scaleX(1);
}

/* Tech line */
.project-tech {
    font-size: 0.8rem;
    color: #9ca3af;
    margin-top: 0.15rem;
    margin-bottom: 0.22rem;
}

/* Description */
.project-desc {
    font-size: 0.9rem;
    color: #cbd5e1;
    max-width: 680px;
    line-height: 1.45rem;
}

/* ========== Animations ========== */
@keyframes pageFade {
    from { opacity: 0; transform: translateY(6px); }
    to   { opacity: 1; transform: translateY(0); }
}

@keyframes rowUp {
    from { opacity: 0; transform: translateY(8px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* Mobile tweaks */
@media (max-width: 600px) {
    .project-page-title {
        font-size: 1.7rem;
    }
    .project-desc {
        font-size: 0.88rem;
    }
}
</style>
"""

# =============== DATA ===============
PROJECTS = [
    {
        "title": "AI Data Analyst",
        "tech": "Python · Pandas · Streamlit",
        "desc": "Upload a CSV and get auto-cleaned tables, summaries and charts instead of manual Excel hell.",
    },
    {
        "title": "Stress Detection Web App",
        "tech": "Python · OpenCV · ML",
        "desc": "Real-time webcam-based basic stress estimation using facial features and a lightweight model.",
    },
    {
        "title": "Event / E-commerce Helper",
        "tech": "JavaScript · PHP · Simple ML / heuristics",
        "desc": "Helps manage products/events and ranks options based on simple user preference logic.",
    },
]

# =============== RENDER FUNCTION ===============
def render_projects_page():
    # inject CSS
    st.markdown(PROJECTS_CSS, unsafe_allow_html=True)

    # page container
    st.markdown('<div class="project-page">', unsafe_allow_html=True)

    # title + subtitle
    st.markdown('<div class="project-page-title">Things I\'ve built</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="project-page-subtitle">'
        'A few projects where I stopped overthinking and just shipped something useful.'
        '</div>',
        unsafe_allow_html=True,
    )

    # list
    st.markdown('<div class="project-list">', unsafe_allow_html=True)

    for p in PROJECTS:
        st.markdown('<div class="project-row">', unsafe_allow_html=True)

        st.markdown(f'<div class="project-title">{p["title"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="project-tech">{p["tech"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="project-desc">{p["desc"]}</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)  # end project-row

    st.markdown('</div>', unsafe_allow_html=True)  # end project-list
    st.markdown('</div>', unsafe_allow_html=True)  # end project-page

