# projects_page.py
import streamlit as st

# 👇 Inject CSS only for this page
PROJECTS_CSS = """
<style>
.project-wrapper {
    margin-top: 1.5rem;
}

/* project card */
.project-card {
    background: rgba(22, 28, 41, 0.85);
    border: 1px solid rgba(148,163,184,0.4);
    border-radius: 14px;
    padding: 1rem 1.25rem;
    margin-bottom: 1rem;
    box-shadow: 0 8px 24px rgba(0,0,0,0.45);
    transition: transform 0.2s ease, background 0.2s ease;
}

/* hover effect */
.project-card:hover {
    transform: translateY(-3px);
    background: rgba(30, 40, 60, 0.9);
}

/* title */
.project-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: #e5e7eb;
    margin-bottom: 0.2rem;
}

/* tech text */
.project-tech {
    font-size: 0.85rem;
    color: #9ca3af;
    margin-bottom: 0.5rem;
}

/* description */
.project-desc {
    font-size: 0.92rem;
    color: #d1d5db;
}
</style>
"""

# 👇 project data
PROJECTS = [
    {
        "title": "AI Data Analyst",
        "tech": "Python · Pandas · Streamlit",
        "desc": "Upload CSV → auto-clean, summarize and visualize data in seconds.",
    },
    {
        "title": "Stress Detection Web App",
        "tech": "Python · OpenCV · ML",
        "desc": "Real-time webcam facial analysis estimating stress levels.",
    },
    {
        "title": "Event / E-commerce Helper",
        "tech": "JavaScript · PHP · Simple ML",
        "desc": "Ranks products/events based on lightweight preference logic.",
    },
]


def render_projects_page():
    # inject CSS for this page only
    st.markdown(PROJECTS_CSS, unsafe_allow_html=True)

    st.markdown(
        '<div class="big-title">Things I\'ve built</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="section-subtitle">Small tools, big vibes.</div>',
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
