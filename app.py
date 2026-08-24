import base64
import streamlit as st

# ==========================================
# SECTION 1: PAGE SETUP & CORE THEME
# ==========================================
st.set_page_config(
    page_title="Alabi Samuel | Data Analyst",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    /* Import Correct Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Work+Sans:wght@400;600&display=swap');

    /* Global Background, Grid Texture, and Default Text */
    .stApp {
        background-color: #091725;
        background-image: 
            linear-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px), 
            linear-gradient(90deg, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
        background-size: 40px 40px;
        color: #8b9eb0;
        font-family: 'Work Sans', sans-serif;
    }
    
    /* Obliterate Default Streamlit Header & Spacing */
    [data-testid="stHeader"] {
        display: none !important;
        height: 0px !important;
        padding: 0px !important;
    }
    
    /* Layout Container Settings (Flush Top, Custom Margins) */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 80px !important; /* Exactly two grid boxes */
        padding-right: 80px !important; /* Exactly two grid boxes */
        max-width: 100% !important;
    }

    /* Headings (Instrument Serif) */
    h1, h2, h3, .serif-text {
        font-family: 'Instrument Serif', serif;
        color: #ffffff;
        font-weight: 400;
        letter-spacing: 0.5px;
    }
    h1 { font-size: 3.5rem; margin-bottom: 10px; line-height: 1.1; }
    
    /* Panel / Card Backgrounds (#10212F) */
    .custom-card {
        background-color: #10212F;
        padding: 25px;
        border-radius: 4px;
        border: 1px solid rgba(55, 216, 168, 0.15); /* Faint mint border */
        height: 100%;
    }
    
    /* Neon Mint Metrics (#37D8A8) */
    .big-metric {
        font-size: 2.8rem;
        color: #37D8A8;
        font-family: 'Work Sans', sans-serif;
        font-weight: 600;
        line-height: 1.2;
        font-variant-numeric: tabular-nums;
        text-shadow: 0 0 12px rgba(55, 216, 168, 0.35); /* Subtle glow */
    }
    </style>
""", unsafe_allow_html=True)
# ==========================================
# SECTION 2: TOP NAVIGATION BAR
# ==========================================
st.markdown("""
<style>
.nav-link {
color: oklch(0.71 0.025 200);
font-weight: 400;
font-size: 12px;
line-height: 18px;
letter-spacing: 1.5px;
padding: 4px 10px;
cursor: pointer;
transition: color 0.2s ease-in-out;
}
.nav-link:hover {
color: #ffffff;
}
.active-link {
color: #37D8A8;
font-weight: 400;
font-size: 14px;
line-height: 18px;
letter-spacing: 1.5px;
padding: 4px 10px;
cursor: default;
}
</style>
<div style="position: sticky; top: 0; background-color: #091725; z-index: 1000; display: flex; justify-content: space-between; align-items: center; padding: 0px 80px 10px 80px; margin: 0 -80px 40px -80px; border-bottom: 1px solid rgba(255, 255, 255, 0.08);">
<div style="display: flex; align-items: center; gap: 8px;">
<span style="color: #37D8A8; font-size: 17px;">●</span> 
<span style="color: oklch(0.95 0.012 180); font-weight: 500; font-size: 14px; line-height: 22px;">Alabi Samuel</span> 
<span style="color: oklch(0.71 0.025 200); font-weight: 400; font-size: 13px; line-height: 18px;">/ Data Analyst</span>
</div>
<div style="display: flex; gap: 12px; align-items: center;">
<span class="active-link">DASHBOARD</span>
<span class="nav-link">CASE STUDIES</span>
<span class="nav-link">ABOUT</span>
<span class="nav-link">CONTACT</span>
</div>
</div>
""", unsafe_allow_html=True)
# ==========================================
# SECTION 3: HERO AREA & METRICS GRID
# ==========================================
import base64

# Convert local image to base64 string so Streamlit HTML can render it
try:
    # Pointing exactly to the folder and double-extension file
    with open("assests/me.png.png", "rb") as img_file: 
        img_b64 = base64.b64encode(img_file.read()).decode()
    img_src = f"data:image/png;base64,{img_b64}"
except FileNotFoundError:
    img_src = "" # Fails gracefully if me.png is missing

html_code = """
<style>
.hero-btn {
background-color: oklch(0.79 0.147 168);
color: oklch(0.18 0.035 250);
font-weight: 500;
font-size: 14px;
line-height: 20px;
padding: 11px 23px; 
border: 1px solid transparent; 
border-radius: 2px;
cursor: pointer;
transition: all 0.3s ease;
display: inline-block;
}
.hero-btn:hover {
background-color: transparent;
border: 1px solid #37D8A8;
box-shadow: 0 0 12px rgba(55, 216, 168, 0.6), inset 0 0 8px rgba(55, 216, 168, 0.3);
color: #37D8A8;
text-shadow: 0 0 8px rgba(55, 216, 168, 0.8);
}
.metric-num {
color: oklch(0.79 0.147 168);
font-weight: 400;
font-size: 30px;
line-height: 36px;
text-shadow: 0 0 10px rgba(55, 216, 168, 0.4), 0 0 20px rgba(55, 216, 168, 0.2);
display: inline-block;
}
</style>
<div style="display: flex; gap: 16px; align-items: stretch; margin-top: 0px;">
<div style="flex: 0 0 700px; min-height: 250px; background-color: #10212F; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 4px; padding: 32px 48px; display: flex; justify-content: space-between; align-items: center;">
<div style="display: flex; flex-direction: column; justify-content: space-between; height: 100%; max-width: 420px;">
<div>
<div style="color: oklch(0.79 0.147 168); font-weight: 400; font-size: 12px; line-height: 16px; letter-spacing: 2px; margin-bottom: 16px;">KPI SYSTEMS · BUSINESS ANALYSIS · RISK MODELLING</div>
<div style="color: oklch(0.95 0.012 180); font-family: 'Instrument Serif', serif; font-weight: 400; font-size: 60px; line-height: 63px; margin-bottom: 16px;">Alabi Samuel</div>
<div style="color: oklch(0.71 0.025 200); font-weight: 400; font-size: 16px; line-height: 26px;">I turn messy operational data into the two or three numbers a business can actually act on.</div>
</div>
<div style="display: flex; align-items: center; gap: 24px; margin-top: 24px;">
<div class="hero-btn">Read the case studies</div>
<div style="color: oklch(0.71 0.025 200); font-weight: 400; font-size: 12px; line-height: 16px;">Available worldwide · Remote</div>
</div>
</div>
<div style="display: flex; align-items: center; justify-content: flex-end;">
<img src="INSERT_IMAGE_HERE" style="width: 140px; height: 140px; border-radius: 50%; border: 2px solid #37D8A8; object-fit: cover; box-shadow: 0 0 15px rgba(55, 216, 168, 0.3);">
</div>
</div>
<div style="flex: 1; display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; background-color: #10212F; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 4px;">
<div style="padding: 24px 32px; border-right: 1px solid rgba(255, 255, 255, 0.08); border-bottom: 1px solid rgba(255, 255, 255, 0.08); display: flex; flex-direction: column; justify-content: center;">
<div class="metric-num">6</div>
<div style="color: oklch(0.71 0.025 200); font-weight: 400; font-size: 11px; line-height: 15px; letter-spacing: 1px; margin-top: 8px;">YEARS ANALYSING<br>DATA</div>
</div>
<div style="padding: 24px 32px; border-bottom: 1px solid rgba(255, 255, 255, 0.08); display: flex; flex-direction: column; justify-content: center;">
<div class="metric-num">38</div>
<div style="color: oklch(0.71 0.025 200); font-weight: 400; font-size: 11px; line-height: 15px; letter-spacing: 1px; margin-top: 8px;">DASHBOARDS<br>SHIPPED</div>
</div>
<div style="padding: 24px 32px; border-right: 1px solid rgba(255, 255, 255, 0.08); display: flex; flex-direction: column; justify-content: center;">
<div class="metric-num">12M+</div>
<div style="color: oklch(0.71 0.025 200); font-weight: 400; font-size: 11px; line-height: 15px; letter-spacing: 1px; margin-top: 8px;">ROWS MODELLED</div>
</div>
<div style="padding: 24px 32px; display: flex; flex-direction: column; justify-content: center;">
<div class="metric-num">9</div>
<div style="color: oklch(0.71 0.025 200); font-weight: 400; font-size: 11px; line-height: 15px; letter-spacing: 1px; margin-top: 8px;">MODELS IN<br>PRODUCTION</div>
</div>
</div>
</div>
"""

# Replace the placeholder with the actual base64 string and render
st.markdown(html_code.replace("", img_src), unsafe_allow_html=True)