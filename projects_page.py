import streamlit as st

# =============== BEAST MODE CSS + HERO ===============
PROJECTS_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

.proj-page {
    max-width: 1100px;
    margin: 0 auto;
    padding: 0 1rem;
    font-family: 'Inter', -apple-system, sans-serif;
    min-height: 100vh;
    position: relative;
    overflow-x: hidden;
}

/* Particle background */
.proj-page::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: 
        radial-gradient(2px 2px at 20px 30px, #22c55e, transparent),
        radial-gradient(2px 2px at 40px 70px, rgba(59,130,246,0.8), transparent),
        radial-gradient(1px 1px at 90px 40px, #a855f7, transparent),
        radial-gradient(1px 1px at 130px 80px, #eab308, transparent);
    background-repeat: repeat;
    background-size: 200px 100px;
    animation: particleFloat 20s linear infinite;
    pointer-events: none;
    z-index: 0;
}

/* HERO SECTION - BIG WELCOME */
.hero-section {
    position: relative;
    z-index: 1;
    min-height: 80vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 2rem 1rem;
    background: rgba(15, 15, 35, 0.95);
    backdrop-filter: blur(40px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 32px;
    margin: 2rem 0;
    box-shadow: 0 0 100px rgba(34, 197, 94, 0.1);
    animation: heroPulse 4s ease-in-out infinite;
}

.hero-kicker {
    font-size: clamp(0.9rem, 2vw, 1.1rem);
    font-weight: 600;
    letter-spacing: 0.4em;
    text-transform: uppercase;
    background: linear-gradient(135deg, #22c55e, #0ea5e9, #a855f7);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    margin-bottom: 1.5rem;
    animation: kickerFloat 3s ease-in-out infinite;
}

.hero-title {
    font-size: clamp(4rem, 10vw, 8rem);
    font-weight: 900;
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 40%, #e2e8f0 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    letter-spacing: -0.05em;
    line-height: 0.9;
    margin-bottom: 1rem;
    position: relative;
}

.hero-title::before {
    content: '';
    position: absolute;
    top: -20px;
    left: 50%;
    transform: translateX(-50%);
    width: 120px;
    height: 120px;
    background: radial-gradient(circle, rgba(34,197,94,0.4) 0%, transparent 70%);
    border-radius: 50%;
    animation: heroGlow 2s ease-in-out infinite alternate;
    z-index: -1;
}

.hero-subtitle {
    font-size: clamp(1.1rem, 3vw, 1.6rem);
    color: #94a3b8;
    font-weight: 300;
    max-width: 800px;
    line-height: 1.6;
    margin-bottom: 3rem;
}

.hero-cta {
    display: inline-flex;
    padding: 1.2rem 3rem;
    background: linear-gradient(135deg, rgba(34,197,94,0.15), rgba(14,165,233,0.15));
    backdrop-filter: blur(20px);
    border: 2px solid rgba(34,197,94,0.3);
    border-radius: 50px;
    font-size: 1.1rem;
    font-weight: 700;
    color: #22c55e;
    text-decoration: none;
    transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1);
    position: relative;
    overflow: hidden;
}

.hero-cta:hover {
    background: linear-gradient(135deg, rgba(34,197,94,0.3), rgba(14,165,233,0.3));
    border-color: #22c55e;
    transform: translateY(-4px);
    box-shadow: 0 20px 40px rgba(34,197,94,0.25);
}

/* Projects Section */
.projects-section {
    position: relative;
    z-index: 2;
    padding: 4rem 0;
}

.proj-header {
    text-align: center;
    margin-bottom: 4rem;
}

.proj-kicker {
    background: linear-gradient(135deg, #22c55e, #0ea5e9, #a855f7);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    font-size: 0.85rem;
    font-weight: 500;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    animation: kickerShimmer 3s ease-in-out infinite;
    margin-bottom: 1rem;
}

.proj-title {
    font-size: clamp(2.5rem, 6vw, 4rem);
    font-weight: 900;
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 30%, #e2e8f0 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    letter-spacing: -0.02em;
}

.proj-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(550px, 1fr));
    gap: 2rem;
}

.proj-card {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 24px;
    padding: 2.2rem;
    position: relative;
    overflow: hidden;
    transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1);
    animation: cardRise 0.8s cubic-bezier(0.23, 1, 0.32, 1) forwards;
    opacity: 0;
}

.proj-card:nth-child(1) { animation-delay: 0.4s; }
.proj-card:nth-child(2) { animation-delay: 0.5s; }
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
    animation: gradientShift 3s ease infinite;
}

.proj-card:hover {
    transform: translateY(-12px) scale(1.02);
    box-shadow: 0 32px 64px rgba(34, 197, 94, 0.15);
    border-color: rgba(34, 197, 94, 0.3);
}

/* Rest of card styles remain same */
.proj-badge {
    display: inline-flex;
    padding: 0.4rem 1rem;
    background: linear-gradient(135deg, rgba(34,197,94,0.2), rgba(14,165,233,0.2));
    border: 1px solid rgba(34,197,94,0.3);
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: 600;
    color: #22c55e;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 1.2rem;
}

.proj-title-h2 {
    font-size: 1.6rem;
    font-weight: 800;
    color: #f8fafc;
    margin-bottom: 0.8rem;
    line-height: 1.3;
}

.proj-tech-stack {
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem;
    margin: 1.2rem 0;
}

.tech-chip {
    padding: 0.3rem 1rem;
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 12px;
    font-size: 0.8rem;
    font-weight: 500;
    color: #cbd5e1;
}

.proj-desc {
    color: #e2e8f0;
    font-size: 0.98rem;
    line-height: 1.65;
}

/* Animations */
@keyframes heroPulse {
    0%, 100% { 
        box-shadow: 0 0 100px rgba(34,197,94,0.1);
        transform: scale(1);
    }
    50% { 
        box-shadow: 0 0 150px rgba(34,197,94,0.25), 0 0 200px rgba(14,165,233,0.15);
        transform: scale(1.02);
    }
}

@keyframes kickerFloat {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-8px); }
}

@keyframes heroGlow {
    0% { transform: translateX(-50%) scale(1); opacity: 0.4; }
    100% { transform: translateX(-50%) scale(1.3); opacity: 0.8; }
}

@keyframes cardRise {
    from { opacity: 0; transform: translateY(30px) scale(0.95); }
    to { opacity: 1; transform: translateY(0) scale(1); }
}

@keyframes particleFloat {
    from { transform: translateY(0px) rotate(0deg); }
    to { transform: translateY(-100px) rotate(360deg); }
}

/* Mobile */
@media (max-width: 768px) {
    .proj-grid { grid-template-columns: 1fr; gap: 1.5rem; }
    .hero-section { margin: 1rem; padding: 2rem 1rem; min-height: 70vh; }
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

# =============== BEAST RENDER ===============
def render_projects_page():
    st.markdown(PROJECTS_CSS, unsafe_allow_html=True)
    st.markdown('<div class="proj-page">', unsafe_allow_html=True)
    
    # 🔥 MASSIVE HERO SECTION
    st.markdown("""
    <div class="hero-section">
        <div class="hero-kicker">EXPLORE</div>
        <h1 class="hero-title">WELCOME TO PROJECTS</h1>
        <div class="hero-subtitle">
            Discover production-grade tools blending AI, computer vision, and web apps. 
            Each project ships with real metrics, battle-tested performance, and clean code.
        </div>
        <a href="#projects" class="hero-cta">SEE THE WORK ↓</a>
    </div>
    """, unsafe_allow_html=True)
    
    # Projects
    st.markdown('<div class="projects-section" id="projects">', unsafe_allow_html=True)
    st.markdown("""
    <div class="proj-header">
        <div class="proj-kicker">PORTFOLIO</div>
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
    
    st.markdown('</div></div></div>', unsafe_allow_html=True)  # grid, section, page

if __name__ == "__main__":
    render_projects_page()
