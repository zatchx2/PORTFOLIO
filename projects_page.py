import streamlit as st

# =============== CSS ===============
PROJECTS_CSS = """
<style>
.proj-page {
    max-width: 950px;
    margin: 0 auto;
    padding-top: 0.5rem;
    animation: projPageFade 0.5s ease-out;
}

/* Header / Title */
.proj-kicker {
    font-size: 0.8rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #9ca3af;
    margin-bottom: 0.4rem;
}

.proj-title {
    font-size: 2.1rem;
    font-weight: 800;
    margin-bottom: 0.2rem;
    background: linear-gradient(90deg, #0ea5e9, #22c55e, #a855f7);
    -webkit-background-clip: text;
    color: transparent;
}

.proj-subtitle {
    font-size: 0.95rem;
    color: #94a3b8;
    margin-bottom: 1.6rem;
    max-width: 600px;
}

/* Projects list */
.proj-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

/* Each project row – 2-column layout on desktop */
.proj-row {
    display: grid;
    grid-template-columns: minmax(0, 2fr) minmax(0, 3fr);
    gap: 1.2rem;
    padding: 0.9rem 0.2rem;
    border-bottom: 1px solid rgba(148,163,184,0.35);
    position: relative;
    overflow: hidden;
    animation: projRowUp 0.45s ease-out;
}

/* Accent bar on left */
.proj-row::before {
    content: "";
    position: absolute;
    left: 0;
    top: 0.9rem;
    bottom: 0.9rem;
    width: 2px;
    border-radius: 999px;
    background: linear-gradient(#22c55e, #0ea5e9);
    opacity: 0;
    transform: translateX(-4px);
    transition: all 0.18s ease-out;
}

.proj-row:hover::before {
    opacity: 1;
    transform: translateX(0);
}

/* Left side (title, meta) */
.proj-left-label {
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.16em;
    color: #6b7280;
    margin-bottom: 0.15rem;
}

.proj-name {
    font-size: 1.05rem;
    font-weight: 650;
    color: #e5e7eb;
    position: relative;
    display: inline-block;
}

/* Animated underline on hover */
.proj-name::after {
    content: "";
    position: absolute;
    left: 0;
    bottom: -2px;
    height: 2px;
    width: 100%;
    background: linear-gradient(90deg, #22c55e, #0ea5e9);
    transform-origin: left;
    transform: scaleX(0);
    transition: transform 0.16s ease-out;
}
.proj-row:hover .proj-name::after {
    transform: scaleX(1);
}

/* Chips row */
.proj-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.25rem;
    margin-top: 0.4rem;
    margin-bottom: 0.4rem;
}

.proj-tag {
    font-size: 0.7rem;
    padding: 0.18rem 0.5rem;
    border-radius: 999px;
    border: 1px solid rgba(148,163,184,0.6);
    color: #cbd5f5;
    background: rgba(15,23,42,0.9);
}

/* Right side (stack + description) */
.proj-tech {
    font-size: 0.82rem;
    color: #9ca3af;
    margin-bottom: 0.25rem;
}

.proj-desc {
    font-size: 0.9rem;
    color: #e5e7eb;
    line-height: 1.45rem;
}

/* ========== Animations ========== */
@keyframes projPageFade {
    from { opacity: 0; transform: translateY(8px); }
    to   { opacity: 1; transform: translateY(0); }
}

@keyframes projRowUp {
    from { opacity: 0; transform: translateY(10px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* Responsive — stack columns on mobile */
@media (max-width: 720px) {
    .proj-row {
        grid-template-columns: minmax(0, 1fr);
        padding: 0.7rem 0;
    }
}
</style>
"""

# =============== YOUR PROJECT DATA ===============
PROJECTS = [
    {
        "label": "MAJOR PROJECT",
        "title": "AI Data Analyst",
        "tags": ["AI / Automation", "Data Tools"],
        "tech": "Python · Pandas · NumPy · Streamlit",
        "desc": (
            "Upload messy CSV files and get cleaned tables, quick summaries and visualizations. "
            "Built to kill manual Excel work and make data exploration feel fast and simple."
        ),
    },
    {
        "label": "ACADEMIC PROJECT",
        "title": "Stress Detection Web App",
        "tags": ["Computer Vision", "OpenCV"],
        "tech": "Python · OpenCV · basic ML · Streamlit",
        "desc": (
            "Web app that uses a webcam feed, extracts facial features and estimates stress levels "
            "using lightweight models. Focused on real-time feedback and simple UX."
        ),
    },
    {
        "label": "SIDE PROJECT",
        "title": "Event / E-commerce Helper",
        "tags": ["Recommendation Logic", "Web App"],
        "tech": "JavaScript · PHP · Simple heuristics",
        "desc": (
            "Helps compare and rank products/events based on user preferences. "
            "Uses scoring logic instead of heavy ML so it stays fast and easy to deploy."
        ),
    },
]

# =============== RENDER FUNCTION ===============
def render_projects_page():
    # inject CSS
    st.markdown(PROJECTS_CSS, unsafe_allow_html=True)

    # main wrapper
    st.markdown('<div class="proj-page">', unsafe_allow_html=True)

    # header
    st.markdown('<div class="proj-kicker">PROJECTS</div>', unsafe_allow_html=True)
    st.markdown('<div class="proj-title">Things I\'ve built</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="proj-subtitle">'
        'A mix of academic work and side projects where I used Python, AI and automation '
        'to turn ideas into working tools.'
        '</div>',
        unsafe_allow_html=True,
    )

    # list
    st.markdown('<div class="proj-list">', unsafe_allow_html=True)

    for p in PROJECTS:
        st.markdown('<div class="proj-row">', unsafe_allow_html=True)

        # LEFT SIDE
        left_html = f"""
        <div>
            <div class="proj-left-label">{p['label']}</div>
            <div class="proj-name">{p['title']}</div>
            <div class="proj-tags">
                {''.join(f'<span class="proj-tag">{tag}</span>' for tag in p['tags'])}
            </div>
        </div>
        """
        st.markdown(left_html, unsafe_allow_html=True)

        # RIGHT SIDE
        right_html = f"""
        <div>
            <div class="proj-tech">{p['tech']}</div>
            <div class="proj-desc">{p['desc']}</div>
        </div>
        """
        st.markdown(right_html, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)  # end proj-row

    st.markdown('</div>', unsafe_allow_html=True)  # end proj-list
    st.markdown('</div>', unsafe_allow_html=True)  # end proj-page
