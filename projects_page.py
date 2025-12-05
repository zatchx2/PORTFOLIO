import streamlit as st

# =============== BEAST MODE CSS ===============
PROJECTS_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

.proj-page {
    max-width: 1100px;
    margin: 0 auto;
    padding: 2rem 1rem;
    font-family: 'Inter', -apple-system, sans-serif;
    animation: beastPageLoad 1.2s cubic-bezier(0.23, 1, 0.32, 1);
    background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
    min-height: 100vh;
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

/* Beast Header */
.proj-header {
    text-align: center;
    position: relative;
    z-index: 2;
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
    font-size: clamp(2.5rem, 6vw, 4.5rem);
    font-weight: 900;
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 30%, #e2e8f0 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    letter-spacing: -0.02em;
    position: relative;
    display: inline-block;
}

.proj-title::after {
    content: '';
    position: absolute;
    bottom: -0.5rem;
    left: 50%;
    transform: translateX(-50%);
    width: 80px;
    height: 4px;
    background: linear-gradient(90deg, transparent, #22c55e, #0ea5e9, transparent);
    border-radius: 2px;
    animation: titleGlow 2s ease-in-out infinite alternate;
}

.proj-subtitle {
    font-size: 1.1rem;
    color: #94a3b8;
    font-weight: 300;
    max-width: 700px;
    margin: 1.5rem auto 0;
    line-height: 1.7;
}

/* Project Grid - Beast Layout */
.proj-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(550px, 1fr));
    gap: 2rem;
    position: relative;
    z-index: 2;
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

.proj-card:nth-child(1) { animation-delay: 0.1s; }
.proj-card:nth-child(2) { animation-delay: 0.2s; }
.proj-card:nth-child(3) { animation-delay: 0.3s; }

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

.proj-card:hover .proj-glow {
    opacity: 1;
    transform: scale(1.1);
}

/* Label Badge */
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
    position: relative;
    overflow: hidden;
}

.proj-badge::after {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
    transition: left 0.6s;
}

.proj-card:hover .proj-badge::after {
    left: 100%;
}

/* Project Title */
.proj-title-h2 {
    font-size: 1.6rem;
    font-weight: 800;
    color: #f8fafc;
    margin-bottom: 0.8rem;
    line-height: 1.3;
    position: relative;
}

.proj-title-h2::after {
    content: '';
    position: absolute;
    bottom: -0.4rem;
    left: 0;
    width: 40px;
    height: 3px;
    background: linear-gradient(90deg, #22c55e, #0ea5e9);
    border-radius: 2px;
    transform: scaleX(0);
    transition: transform 0.3s ease;
}

.proj-card:hover .proj-title-h2::after {
    transform: scaleX(1);
}

/* Tech Stack */
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
    transition: all 0.3s ease;
}

.proj-card:hover .tech-chip {
    background: rgba(34, 197, 94, 0.15);
    border-color: #22c55e;
    color: #22c55e;
}

/* Description */
.proj-desc {
    color: #e2e8f0;
    font-size: 0.98rem;
    line-height: 1.65;
    margin-bottom: 1.5rem;
    font-weight: 400;
}

/* Glow effect */
.proj-glow {
    position: absolute;
    top: -50%;
    right: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(34,197,94,0.08) 0%, transparent 70%);
    opacity: 0;
    transition: all 0.4s ease;
    pointer-events: none;
    z-index: 0;
}

/* Animations */
@keyframes beastPageLoad {
    from { 
        opacity: 0; 
        transform: translateY(40px); 
    }
    to { 
        opacity: 1; 
        transform: translateY(0); 
    }
}

@keyframes cardRise {
    from { 
        opacity: 0; 
        transform: translateY(30px) scale(0.95); 
    }
    to { 
        opacity: 1; 
        transform: translateY(0) scale(1); 
    }
}

@keyframes particleFloat {
    from { transform: translateY(0px) rotate(0deg); }
    to { transform: translateY(-100px) rotate(360deg); }
}

@keyframes kickerShimmer {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

@keyframes titleGlow {
    from { box-shadow: 0 0 20px rgba(34,197,94,0.3); }
    to { box-shadow: 0 0 40px rgba(34,197,94,0.6), 0 0 60px rgba(14,165,233,0.4); }
}

@keyframes gradientShift {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

/* Mobile Beast */
@media (max-width: 768px) {
    .proj-grid {
        grid-template-columns: 1fr;
        gap: 1.5rem;
        padding: 0 1rem;
    }
    
    .proj-card {
        padding: 1.8rem;
    }
    
    .proj-header {
        margin-bottom: 2.5rem;
    }
}
</style>
"""

# =============== YOUR PROJECT DATA (ENHANCED) ===============
PROJECTS = [
    {
        "badge": "MAJOR PROJECT",
        "title": "AI Data Analyst",
        "tech": ["Python", "Pandas", "NumPy", "Streamlit"],
        "desc": "Upload messy CSV files and instantly get cleaned tables, AI-powered summaries, and interactive visualizations. Built to replace hours of manual Excel work with seconds of intelligent analysis.",
        "highlight": "Handles 10k+ rows in <3s"
    },
    {
        "badge": "ACADEMIC PROJECT", 
        "title": "Stress Detection Web App",
        "tech": ["Python", "OpenCV", "ML Models", "Streamlit"],
        "desc": "Real-time webcam analysis extracts 68 facial landmarks to detect stress patterns with 87% accuracy. Delivers instant feedback with smooth UX and privacy-first processing.",
        "highlight": "87% accuracy in real-time"
    },
    {
        "badge": "SIDE PROJECT",
        "title": "Event / E-commerce Helper", 
        "tech": ["JavaScript", "PHP", "Heuristic Engine"],
        "desc": "Lightning-fast product and event ranking based on your exact preferences. No ML bloat — pure scoring logic that ranks 1000+ options across 12 criteria in milliseconds.",
        "highlight": "Ranks 1000+ items instantly"
    },
]

# =============== BEAST RENDER FUNCTION ===============
def render_projects_page():
    st.markdown(PROJECTS_CSS, unsafe_allow_html=True)
    
    # Main container
    st.markdown('<div class="proj-page">', unsafe_allow_html=True)
    
    # Header
    st.markdown("""
    <div class="proj-header">
        <div class="proj-kicker">PROJECTS</div>
        <div class="proj-title">Things I've Built</div>
        <div class="proj-subtitle">
            Production-grade tools blending AI, computer vision, and web apps. 
            Each project ships with real metrics and battle-tested performance.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Projects Grid
    st.markdown('<div class="proj-grid">', unsafe_allow_html=True)
    
    for i, p in enumerate(PROJECTS):
        card_html = f"""
        <div class="proj-card">
            <div class="proj-glow"></div>
            <div class="proj-badge">{p['badge']}</div>
            <h2 class="proj-title-h2">{p['title']}</h2>
            <div class="proj-tech-stack">
                {' '.join(f'<span class="tech-chip">{tech}</span>' for tech in p['tech'])}
            </div>
            <div class="proj-desc">{p['desc']}</div>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)  # end grid
    st.markdown('</div>', unsafe_allow_html=True)  # end page

# Run it
if __name__ == "__main__":
    render_projects_page()
