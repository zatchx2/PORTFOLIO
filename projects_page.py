# projects_page.py
import streamlit as st

# 👇 Only edit this list when you add/change projects
PROJECTS = [
    {
        "title": "AI Data Analyst",
        "tech": "Python · Pandas · Streamlit",
        "desc": "Upload a CSV and get auto-cleaned tables, summaries and charts instead of manual Excel hell.",
        "link": "https://github.com/zatchx2/ai-data-analyst"  # change to your real repo
    },
    {
        "title": "Stress Detection Web App",
        "tech": "Python · OpenCV · ML",
        "desc": "Webcam-based basic stress estimation using facial features and a simple model.",
        "link": "https://github.com/zatchx2/stress-detector"   # change to your real repo
    },
    {
        "title": "Event / E-commerce Helper",
        "tech": "JavaScript · PHP · Basic ML / heuristics",
        "desc": "Helps manage events/products and ranks options based on simple user preference signals.",
        "link": "https://github.com/zatchx2/event-helper"      # change to your real repo
    },
]

def render_projects_page():
    st.markdown(
        '<div class="big-title">Things I\'ve built</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="section-subtitle">Each card links out to more details or code.</div>',
        unsafe_allow_html=True,
    )

    # You can group or filter later if you want
    for p in PROJECTS:
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="project-title">{p["title"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="project-tech">{p["tech"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="project-desc">{p["desc"]}</div>', unsafe_allow_html=True)
        st.markdown(
            f'<a href="{p["link"]}" target="_blank">🔗 View project →</a>',
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)
