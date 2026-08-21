import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import duckdb

# ---------------------------------------------------------
# 1. PAGE CONFIGURATION & CUSTOM CSS STYLING
# ---------------------------------------------------------
st.set_page_config(
    page_title="Sam | Data Analyst Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for polished UI styling
st.markdown("""
    <style>
    /* Main Background Accent */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    
    /* Card Container Styling */
    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 15px 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    div[data-testid="stMetric"]:hover {
        transform: translateY(-2px);
        border-color: #6c5ce7;
    }

    /* Primary Accent Color for Buttons & Highlights */
    .stButton>button {
        background-color: #6c5ce7;
        color: white;
        border-radius: 8px;
        border: none;
        font-weight: 600;
        padding: 8px 16px;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #5a4bcf;
        color: white;
    }

    /* Headings Styling */
    h1, h2, h3 {
        font-family: 'Inter', sans-serif;
        font-weight: 700;
    }
    
    /* Expander Container Styling */
    .streamlit-expanderHeader {
        background-color: rgba(255, 255, 255, 0.03);
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. SIDEBAR NAVIGATION & PROFILE
# ---------------------------------------------------------
with st.sidebar:
    st.image("https://api.dicebear.com/7.x/bottts/svg?seed=SamData", width=110)
    st.title("Sam")
    st.caption("🚀 Data Analyst | SQL, Python, Excel & Tableau")
    st.markdown("---")
    
    st.subheader("📬 Connect")
    st.markdown("🔗 [LinkedIn Profile](#)")
    st.markdown("🐙 [GitHub Portfolio](#)")
    st.markdown("✉️ contact@example.com")
    st.markdown("---")
    
    st.caption("Powered by Python, Streamlit & Plotly")

# ---------------------------------------------------------
# 3. HERO SECTION & KEY METRICS
# ---------------------------------------------------------
st.title("Data Analyst Portfolio 📊")
st.markdown("### *Turning raw datasets into actionable business insights.*")
st.write(
    "Welcome! Explore live interactive visualizations, execute custom SQL queries, "
    "or upload your own dataset to test the analytical workspace in real time."
)

st.markdown("<br>", unsafe_allow_html=True)

# KPI Highlight Bar
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Data Processed", value="2.5M+", delta="Rows Cleaned")
col2.metric(label="SQL Queries Run", value="1,200+", delta="Production Ready")
col3.metric(label="Portfolio Projects", value="5+", delta="Interactive")
col4.metric(label="Pipeline Runtime", value="< 2s", delta="Automated")

st.markdown("<br>---<br>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. DATASET SELECTION & UPLOAD MANAGEMENT
# ---------------------------------------------------------
st.header("📌 Interactive Data Workspace")

# Data Source Selector (Upload custom CSV OR use default dataset)
data_source = st.radio(
    "Choose Data Source:",
    ["Use Default Portfolio Dataset", "Upload My Own CSV File"],
    horizontal=True
)

@st.cache_data
def get_default_data():
    # Sample stock / revenue dataset structure
    data = {
        'Date': pd.date_range(start='2026-01-01', periods=120, freq='D'),
        'Category': ['Electronics', 'Software', 'Services', 'Hardware'] * 30,
        'Region': ['North America', 'Europe', 'Asia-Pacific', 'Latin America'] * 30,
        'Revenue_USD': [1500, 2400, 800, 3100, 1900, 4200, 1100, 2800] * 15,
        'Units_Sold': [15, 24, 8, 31, 19, 42, 11, 28] * 15,
        'Profit_Margin': [0.25, 0.40, 0.15, 0.30] * 30
    }
    return pd.DataFrame(data)

if data_source == "Upload My Own CSV File":
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.success(f"Successfully loaded uploaded dataset: **{uploaded_file.name}** ({len(df)} rows)")
        except Exception as e:
            st.error(f"Error reading CSV file: {e}")
            df = get_default_data()
    else:
        st.info("Awaiting CSV upload. Displaying default dataset in the meantime.")
        df = get_default_data()
else:
    df = get_default_data()

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 5. DYNAMIC FILTERS & ADVANCED PLOTLY CHARTS
# ---------------------------------------------------------
# Automatically pick categorical columns for filters
categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
numeric_cols = df.select_dtypes(include=['number']).columns.tolist()

if categorical_cols and numeric_cols:
    filter_col1, filter_col2 = st.columns(2)
    
    primary_cat = categorical_cols[0]
    with filter_col1:
        selected_cats = st.multiselect(
            f"Filter by {primary_cat}:",
            options=df[primary_cat].unique(),
            default=df[primary_cat].unique()
        )
    
    filtered_df = df[df[primary_cat].isin(selected_cats)] if selected_cats else df

    # Workspace Tabs
    tab1, tab2, tab3 = st.tabs(["📈 Customizable Charts", "💻 Live SQL Sandbox (DuckDB)", "📁 Data Inspection"])

    with tab1:
        c1, c2 = st.columns([1, 2])
        
        with c1:
            st.subheader("Chart Controls")
            chart_type = st.selectbox("Select Chart Type:", ["Bar Chart", "Line Chart", "Scatter Plot", "Box Plot"])
            x_axis = st.selectbox("X-Axis Variable:", options=df.columns, index=0)
            y_axis = st.selectbox("Y-Axis Variable:", options=numeric_cols, index=min(0, len(numeric_cols)-1))
            color_by = st.selectbox("Group / Color By:", options=[None] + categorical_cols, index=1 if len(categorical_cols) > 1 else 0)

        with c2:
            st.subheader("Visual Analytics")
            
            # Chart styling config
            plotly_template = "plotly_dark"
            custom_colors = px.colors.qualitative.Bold
            
            if chart_type == "Bar Chart":
                fig = px.bar(
                    filtered_df, x=x_axis, y=y_axis, color=color_by,
                    barmode="group", template=plotly_template, color_discrete_sequence=custom_colors,
                    title=f"{y_axis} by {x_axis}"
                )
            elif chart_type == "Line Chart":
                fig = px.line(
                    filtered_df, x=x_axis, y=y_axis, color=color_by,
                    template=plotly_template, color_discrete_sequence=custom_colors,
                    title=f"{y_axis} Trend over {x_axis}"
                )
            elif chart_type == "Scatter Plot":
                fig = px.scatter(
                    filtered_df, x=x_axis, y=y_axis, color=color_by,
                    template=plotly_template, color_discrete_sequence=custom_colors,
                    title=f"{y_axis} vs {x_axis}"
                )
            else:
                fig = px.box(
                    filtered_df, x=x_axis, y=y_axis, color=color_by,
                    template=plotly_template, color_discrete_sequence=custom_colors,
                    title=f"Distribution of {y_axis} across {x_axis}"
                )
                
            fig.update_layout(
                margin=dict(l=20, r=20, t=40, b=20),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)"
            )
            st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.subheader("Query the Dataset using DuckDB SQL")
        st.caption("Write standard SQL. Refer to your active dataset as `filtered_df`.")
        
        default_sql = f"SELECT {primary_cat}, SUM({numeric_cols[0]}) AS Total_{numeric_cols[0]} FROM filtered_df GROUP BY {primary_cat} ORDER BY Total_{numeric_cols[0]} DESC"
        user_sql = st.text_area("SQL Editor:", value=default_sql, height=100)
        
        if st.button("Execute SQL"):
            try:
                res = duckdb.query(user_sql).df()
                st.success("Query Executed Successfully!")
                st.dataframe(res, use_container_width=True)
            except Exception as e:
                st.error(f"SQL Error: {e}")

    with tab3:
        st.subheader("Raw Data Table")
        st.dataframe(filtered_df, use_container_width=True)

else:
    st.warning("The dataset needs at least one numeric and one text column to display analytics.")

st.markdown("<br>---<br>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 6. FEATURED CASE STUDIES
# ---------------------------------------------------------
st.header("📂 Featured Case Studies")

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Financial Ledger & Credit Extraction Pipeline")
    st.markdown("""
    * **Tools:** Python (`pandas`, `pdfplumber`), SQL
    * **Summary:** Built an automated extraction pipeline that parses credit transactions from multi-page PDF statements directly into formatted Excel ledgers.
    """)
    with st.expander("View Implementation Details"):
        st.code("""
import pdfplumber
import pandas as pd

# Automated PDF ledger extraction snippet
with pdfplumber.open("bank_statement.pdf") as pdf:
    for page in pdf.pages:
        table = page.extract_table()
        # Clean transaction rows & format currency fields
        """, language="python")

with col_b:
    st.subheader("Interactive Stock & Market Trend Analyzer")
    st.markdown("""
    * **Tools:** Python, Yahoo Finance API, Streamlit, Plotly
    * **Summary:** Developed a real-time web interface fetching historical stock prices, computing rolling averages, and displaying interactive candlestick charts.
    """)
    with st.expander("View Implementation Details"):
        st.write("Pulled financial data via API endpoints, computed 50-day and 200-day moving averages, and rendered interactive Plotly candlestick charts.")