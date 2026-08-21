import streamlit as st

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="Alabi Samuel | Data Analyst",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. GLOBAL CSS (Matching the Prototype)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Playfair+Display:wght@600;700&display=swap');

    /* Global Background and Text Colors */
    .stApp {
        background-color: #0b131e;
        color: #8b9eb0;
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide top header line */
    header {visibility: hidden;}
    
    /* Typography Overrides */
    h1, h2, h3, .serif-text {
        font-family: 'Playfair Display', serif;
        color: #ffffff;
    }
    h1 { font-size: 3.5rem; font-weight: 700; margin-bottom: 10px; }
    h2 { font-size: 1.8rem; margin-bottom: 20px; }
    
    /* Teal Accent Color */
    .teal-accent { color: #20c997; }
    
    /* Card Containers */
    .custom-card {
        background-color: #111d2b;
        padding: 25px;
        border-radius: 8px;
        border: 1px solid #1c2e40;
        height: 100%;
    }
    
    /* Big Metric Numbers */
    .big-metric {
        font-size: 2.5rem;
        color: #20c997;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        line-height: 1.2;
    }
    
    /* Custom Button */
    .stButton>button {
        background-color: #20c997;
        color: #0b131e;
        border: none;
        border-radius: 4px;
        font-weight: 600;
        padding: 10px 24px;
        transition: opacity 0.3s ease;
    }
    .stButton>button:hover { opacity: 0.8; color: #0b131e; }
    
    /* Progress Bars Toolbelt */
    .tool-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 15px;
        font-size: 0.9rem;
        color: #e2e8f0;
    }
    .progress-bar-bg {
        flex-grow: 1;
        height: 6px;
        background-color: #1c2e40;
        margin: 0 15px;
        border-radius: 3px;
        overflow: hidden;
    }
    .progress-bar-fill {
        height: 100%;
        background-color: #20c997;
    }
    </style>
""", unsafe_allow_html=True)

# 3. TOP NAVIGATION HEADER (Simulated)
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 20px 0; border-bottom: 1px solid #1c2e40; margin-bottom: 40px;">
        <div style="color: #fff; font-weight: 600;"><span class="teal-accent">●</span> Alabi Samuel <span style="color: #5a6b7c; font-weight: 400;">/ Data Analyst</span></div>
    </div>
""", unsafe_allow_html=True)

# 4. MAIN LAYOUT GRID
col_left, col_right = st.columns([1.2, 1])

# --- LEFT COLUMN: Hero Section & Toolbelt ---
with col_left:
    st.markdown("<p style='color: #20c997; font-size: 0.8rem; font-weight: 600; letter-spacing: 1px;'>KPI SYSTEMS • BUSINESS ANALYSIS • RISK MODELLING</p>", unsafe_allow_html=True)
    st.markdown("<h1>Alabi Samuel</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 1.2rem; color: #a0aec0; margin-bottom: 30px; max-width: 90%;'>I turn messy operational data into the two or three numbers a business can actually act on.</p>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 2])
    with c1:
        st.button("Read the case studies")
    with c2:
        st.markdown("<p style='font-size: 0.85rem; color: #5a6b7c; margin-top: 10px;'>Available worldwide • Remote</p>", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Toolbelt Section
    st.markdown("""
        <div class="custom-card">
            <p style="font-size: 0.75rem; letter-spacing: 2px; color: #5a6b7c; margin-bottom: 20px;">TOOLBELT</p>
            <div class="tool-row"><span>SQL</span><div class="progress-bar-bg"><div class="progress-bar-fill" style="width: 95%;"></div></div><span>95</span></div>
            <div class="tool-row"><span>Python</span><div class="progress-bar-bg"><div class="progress-bar-fill" style="width: 90%;"></div></div><span>90</span></div>
            <div class="tool-row"><span>Power BI</span><div class="progress-bar-bg"><div class="progress-bar-fill" style="width: 88%;"></div></div><span>88</span></div>
            <div class="tool-row"><span>Excel</span><div class="progress-bar-bg"><div class="progress-bar-fill" style="width: 92%;"></div></div><span>92</span></div>
            <div class="tool-row"><span>Tableau</span><div class="progress-bar-bg"><div class="progress-bar-fill" style="width: 84%;"></div></div><span>84</span></div>
            <div class="tool-row"><span>R</span><div class="progress-bar-bg"><div class="progress-bar-fill" style="width: 78%;"></div></div><span>78</span></div>
            <div class="tool-row"><span>Stata</span><div class="progress-bar-bg"><div class="progress-bar-fill" style="width: 72%;"></div></div><span>72</span></div>
            <div class="tool-row"><span>SPSS</span><div class="progress-bar-bg"><div class="progress-bar-fill" style="width: 68%;"></div></div><span>68</span></div>
        </div>
    """, unsafe_allow_html=True)

# --- RIGHT COLUMN: Metrics & Featured Analyses ---
with col_right:
# Featured Analyses Cards (Bulletproof HTML)
    st.markdown("""
<div class="custom-card">
    <p style="font-size: 0.75rem; letter-spacing: 2px; color: #5a6b7c; margin-bottom: 20px;">FEATURED ANALYSES</p>
    <div style="margin-bottom: 30px; border-bottom: 1px solid #1c2e40; padding-bottom: 20px;">
        <p style="color: #20c997; font-size: 0.7rem; letter-spacing: 1px; margin-bottom: 5px;">KPI FRAMEWORK</p>
        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div style="width: 70%;">
                <h3 class="serif-text" style="margin: 0 0 10px 0; font-size: 1.4rem;">KPI Command Center</h3>
                <p style="font-size: 0.85rem; margin: 0;">Replaced 14 conflicting spreadsheets with a single governed KPI layer and one executive Power BI board.</p>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 1.5rem; color: #fff; font-family: 'Inter';">14 &rarr; 1</div>
                <div style="font-size: 0.65rem; letter-spacing: 1px; color: #5a6b7c;">SOURCES OF TRUTH</div>
            </div>
        </div>
    </div>
    <div style="margin-bottom: 30px; border-bottom: 1px solid #1c2e40; padding-bottom: 20px;">
        <p style="color: #20c997; font-size: 0.7rem; letter-spacing: 1px; margin-bottom: 5px;">BUSINESS ANALYSIS</p>
        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div style="width: 70%;">
                <h3 class="serif-text" style="margin: 0 0 10px 0; font-size: 1.4rem;">Business Performance Analysis</h3>
                <p style="font-size: 0.85rem; margin: 0;">Cohort and channel margin analysis that found where growth was quietly being sold at a loss.</p>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 1.5rem; color: #fff; font-family: 'Inter';">+4.8pt</div>
                <div style="font-size: 0.65rem; letter-spacing: 1px; color: #5a6b7c;">GROSS MARGIN RECOVERED</div>
            </div>
        </div>
    </div>
    <div>
        <p style="color: #20c997; font-size: 0.7rem; letter-spacing: 1px; margin-bottom: 5px;">RISK MANAGEMENT</p>
        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div style="width: 70%;">
                <h3 class="serif-text" style="margin: 0 0 10px 0; font-size: 1.4rem;">Credit Risk Scoring</h3>
                <p style="font-size: 0.85rem; margin: 0;">A transparent logistic scorecard that beat the legacy rules engine without becoming a black box.</p>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 1.5rem; color: #fff; font-family: 'Inter';">0.81</div>
                <div style="font-size: 0.65rem; letter-spacing: 1px; color: #5a6b7c;">AUC ON HOLDOUT</div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
    
st.markdown("<br><br><br>", unsafe_allow_html=True)

# 5. FOOTER
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #1c2e40; padding-top: 20px; font-size: 0.8rem; color: #5a6b7c;">
        <div>Alabi Samuel — KPI systems • Business analysis • Risk modelling</div>
        <div>alabisamuel.analytics@gmail.com</div>
    </div>
""", unsafe_allow_html=True)