import streamlit as st

# =============== ULTRA STABLE BEAST CSS ===============
PROJECTS_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

/* STABLE FULLSCREEN BACKGROUND - FIXED */
.stApp {
    background: linear-gradient(135deg, #020617 0%, #0f0f23 50%, #1a1a2e 100%);
    position: relative;
    overflow-x: hidden;
}

/* NO MORE REVOLVING PARTICLES - SUBTLE GLOW DOTS */
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
    background-size: 200px 150px;
    opacity: 0.6;
    pointer-events: none;
    z-index: 0;
}

.proj-page {
    max-width: 1100px;
    margin: 0 auto;
    padding: 1rem;
    font-family: 'Inter', sans-serif;
    min-height: 100vh;
    position: relative;
    z-index: 1;
}

/* HERO SECTION - ROCK SOLID */
.hero-section {
    position: relative;
    z-index: 2;
    min-height: 85vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 4rem 2rem;
    background: rgba(2, 6, 23, 0.92);
    backdrop-filter: blur(30px);
    border: 1px solid rgba(148,163,184,0.12);
    border-radius: 28px;
    margin: 2rem 0;
    box-shadow: 
        0 0 60px rgba(34,197,94,0.15),
        inset 0 1px 0 rgba(255,255,255,0.1);
    animation: heroBreath 6s ease-in-out infinite;
}

.hero-kicker {
    font-size: clamp(0.95rem, 2.5vw, 1.2rem);
    font-weight: 700;
    letter-spacing: 0.35em;
    text-transform: uppercase;
    background: linear-gradient(135deg, #22c55e, #0ea5e9, #a855f7);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    margin-bottom: 2rem;
    animation: kickerShimmer 4s ease-in-out infinite;
}

.hero-title {
    font-size: clamp(4.5rem, 12vw, 9rem);
    font-weight: 900;
    background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 50%, #cbd5e1 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    letter-spacing: -0.04em;
    line-height: 0.92;
    margin-bottom: 1.5rem;
    text-shadow: 0 0 40px rgba(255,255,255,0.1);
}

.hero-subtitle {
    font-size: clamp(1.2rem, 3.5vw, 1.8rem);
    color: #94a3b8;
    font-weight: 400;
    max-width: 850px;
    line-height: 1.7;
    margin-bottom: 4rem;
}

.hero-cta {
    display: inline-flex;
    padding: 1.4rem 3.5rem;
    background: linear-gradient(135deg, rgba(34,197,94,0.2), rgba(14,165,233,0.2));
    backdrop-filter: blur(20px);
    border: 2px solid rgba(34,197,94,0.4);
    border-radius: 50px;
    font-size: 1.15rem;
    font-weight: 700;
    color: #22c55e;
    text-decoration: none;
    transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1);
    position: relative;
    overflow: hidden;
}

.hero-cta:hover {
    background: linear-gradient(135deg, rgba(34,197,94,0.4), rgba(14,165,233,0.4));
    border-color: #22c55e;
    transform: translateY(-6px);
    box-shadow: 0 25px 50px rgba(34,197,94,0.3);
}

/* PROJECTS SECTION */
.projects-section {
    position: relative;
    z-index: 2;
    padding: 5rem 0;
}

.proj-header {
    text-align: center;
    margin-bottom: 5rem;
}

.proj-kicker {
    background: linear-gradient(135deg, #22c55e, #0ea5e9, #a855f7);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    font-size: 1rem;
    font-weight: 600;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    animation: kickerShimmer 3s ease-in-out infinite;
    margin-bottom: 1.5rem;
}

.proj-title {
    font-size: clamp(2.8rem, 7vw, 5rem);
    font-weight: 900;
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 30%, #e2e8f0 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    letter-spacing: -0.03em;
}

.proj-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(600px, 1fr));
    gap: 2.5rem;
}

.proj-card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(25px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 28px;
    padding: 2.5rem;
    position: relative;
    overflow: hidden;
    transition: all 0.5s cubic-bezier(0.23, 1, 0.32, 1);
    animation: cardSlideUp 0.8s cubic-bezier(0.23, 1, 0.32, 1) forwards;
    opacity: 0;
}

.proj-card:nth-child(1) { animation-delay: 0.3s; }
.proj-card:nth-child(2) { animation-delay: 0.45s; }
.proj-card:nth-child(3) { animation-delay: 0.6s; }

.proj-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #22c55e, #0ea5e9, #a855f7, #eab308);
    background-size: 300% 100%;
    animation: gradientShift 4s ease infinite;
}

.proj-card:hover {
    transform: translateY(-16px) scale(1.03);
    box-shadow: 0 40px 80px rgba(34, 197, 94, 0.2);
    border-color: rgba(34, 197, 94, 0.4);
}

.proj-badge {
    display: inline-flex;
    padding: 0.5rem 1.2rem;
    background: linear-gradient(135deg, rgba(34,197,94,0.25), rgba(14,165,233,0.25));
    border: 1px solid rgba(34,197,94,0.4);
    border-radius: 16px;
    font-size: 0.85rem;
    font-weight: 700;
    color: #22c55e;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    margin-bottom: 1.5rem;
}

.proj-title-h2 {
    font-size: 1.8rem;
    font-weight: 900;
    color: #f8fafc;
    margin-bottom: 1rem;
    line-height: 1.3;
}

.proj-tech-stack {
    display: flex;
    flex-wrap: wrap;
    gap: 0.8rem;
    margin: 1.5rem 0;
}

.tech-chip {
    padding: 0.4rem 1.2rem;
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 16px;
    font-size: 0.85rem;
    font-weight: 600;
    color: #cbd5e1;
    transition: all 0.3s ease;
}

.proj-desc {
    color: #e2e8f0;
    font-size: 1rem;
    line-height: 1.7;
}

/* STABLE ANIMATIONS */
@keyframes heroBreath {
    0%, 100% { 
        box-shadow: 0 0 60px rgba(34,197,94,0.15);
        transform: scale(1);
    }
    50% { 
        box-shadow: 0 0 100px rgba(34,197,94,0.3);
        transform: scale(1.01);
    }
}

@keyframes kickerShimmer {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

@keyframes cardSlideUp {
    from { opacity: 0; transform: translateY(40px) scale(0.95); }
    to { opacity: 1; transform: translateY(0) scale(1); }
}

@keyframes gradientShift {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

/* PERFECT MOBILE */
@media (max-width: 768px) {
    .proj-grid { grid-template-columns: 1fr; gap: 2rem; }
    .proj-card { padding: 2rem; }
    .hero-section { margin: 1rem; padding: 2.5rem 1.5rem; min-height: 75vh; }
}
</style>
"""

# =============== PROJECT DATA ===============
PROJECTS = [
    {
        "badge": "MAJOR PROJECT",
        "title": "AI Data Analyst",
        "tech": ["Python", "Pandas", "NumPy", "Streamlit"],
        "desc": "Upload messy CSV files and instantly get cleaned tables, AI-powered summaries, and interactive visualizations. Built to replace hours of manual Excel work with seconds of intelligent analysis."
    },
    {
        "badge": "ACADEMIC PROJECT", 
        "title": "Stress Detection Web App",
        "tech": ["Python", "OpenCV", "ML Models", "Streamlit"],
        "desc": "Real-time webcam analysis extracts 68 facial landmarks to detect stress patterns with 87% accuracy. Delivers instant feedback with smooth UX and privacy-first processing."
    },
    {
        "badge": "SIDE PROJECT",
        "title": "Event / E-commerce Helper", 
        "tech": ["JavaScript", "PHP", "Heuristic Engine"],
        "desc": "Lightning-fast product and event ranking based on your exact preferences. No ML bloat — pure scoring logic that ranks 1000+ options across 12 criteria in milliseconds."
    },
]

# =============== ROCK SOLID RENDER ===============
def render_projects_page():
    st.markdown(PROJECTS_CSS, unsafe_allow_html=True)
    
    st.markdown('<div class="proj-page">', unsafe_allow_html=True)
    
    # MASSIVE HERO
    st.markdown("""
    <div class="hero-section">
        <div class="hero-kicker">PORTFOLIO</div>
        <h1 class="hero-title">WELCOME TO PROJECTS</h1>
        <div class="hero-subtitle">
            Production-grade tools blending AI, computer vision, and web development. 
            Each project ships with real metrics and battle-tested performance.
        </div>
        <a href="#projects-list" class="hero-cta">EXPLORE PROJECTS ↓</a>
    </div>
    """, unsafe_allow_html=True)
    
    # PROJECTS GRID
    st.markdown('<div class="projects-section" id="projects-list">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="proj-header">
        <div class="proj-kicker">RECENT WORK</div>
        <div class="proj-title">Things I've Built</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="proj-grid">', unsafe_allow_html=True)
    
    for i, p in enumerate(PROJECTS):
        card_html = f"""
        <div class="proj-card">
            <div class="proj-badge">{p['badge']}</div>
            <h2 class="proj-title-h2">{p['title']}</h2>
            <div class="proj-tech-stack">
                {' '.join(f'<span class="tech-chip">{tech}</span>' for tech in p['tech'])}
            </div>
            <div class="proj-desc">{p['desc']}</div>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
    
    st.markdown('</div></div></div>', unsafe_allow_html=True)

if __name__ == "__main__":
    render_projects_page()
