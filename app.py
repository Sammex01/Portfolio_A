import streamlit as st
import pandas as pd
import plotly.express as px
import duckdb

# ---------------------------------------------------------
# 1. PAGE CONFIGURATION & STYLING
# ---------------------------------------------------------
st.set_page_config(
    page_title="Data Analyst Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# 2. SIDEBAR NAVIGATION & PROFILE
# ---------------------------------------------------------
with st.sidebar:
    st.image("https://via.placeholder.com/150", width=120)  # Replace with your photo URL
    st.title("Your Name")
    st.caption("Data Analyst | SQL, Python, Tableau")
    st.markdown("---")
    
    st.subheader("📬 Get in Touch")
    st.markdown("[LinkedIn](#)")
    st.markdown("[GitHub](#)")
    st.markdown("✉️ your.email@example.com")
    st.markdown("---")
    
    st.caption("Built purely with Python & Streamlit")

# ---------------------------------------------------------
# 3. HERO SECTION & KEY METRICS
# ---------------------------------------------------------
st.title("Hi, I'm a Data Analyst 👋")
st.subheader("Transforming raw data into actionable business decisions.")
st.write(
    "Welcome to my interactive portfolio! Explore my featured projects below "
    "by running real-time queries and filtering live datasets."
)

# KPI Highlight Bar
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Datasets Processed", value="2.5M+", delta="Rows")
col2.metric(label="SQL Queries Executed", value="1,200+", delta="Production")
col3.metric(label="Machine Learning Models", value="12", delta="Trained")
col4.metric(label="Dashboards Built", value="25+", delta="Active")

st.markdown("---")

# ---------------------------------------------------------
# 4. FEATURED INTERACTIVE PROJECT: SQL & EXPLORATORY DATA ANALYSIS
# ---------------------------------------------------------
st.header("📌 Project 1: E-Commerce Revenue & Customer Analysis")
st.markdown("""
**Objective:** Analyze revenue trends and customer purchasing habits across product categories.  
*Interact with the controls below to filter data and run live SQL queries.*
""")

# Data Generation & Initial Assignment
@st.cache_data
def load_sample_data():
    data = {
        'Order_Date': pd.date_range(start='2026-01-01', periods=100, freq='D'),
        'Category': ['Electronics', 'Clothing', 'Home', 'Books'] * 25,
        'Revenue': [120, 45, 200, 15] * 25,
        'Units_Sold': [2, 1, 4, 1] * 25,
        'Region': ['North', 'South', 'East', 'West'] * 25
    }
    return pd.DataFrame(data)

# Load data FIRST before calling interactive filter widgets
df = load_sample_data()

# Interactive Filters
filter_col1, filter_col2 = st.columns(2)
with filter_col1:
    selected_categories = st.multiselect(
        "Select Product Categories:",
        options=df['Category'].unique(),
        default=df['Category'].unique()
    )
with filter_col2:
    selected_regions = st.multiselect(
        "Select Regions:",
        options=df['Region'].unique(),
        default=df['Region'].unique()
    )

# Filter Dataframe
filtered_df = df[
    (df['Category'].isin(selected_categories)) & 
    (df['Region'].isin(selected_regions))
]

# Tabs for Visualizations vs SQL Runner vs Data Table
tab1, tab2, tab3 = st.tabs(["📊 Interactive Charts", "💻 Live SQL Query Runner", "📁 Raw Dataset"])

with tab1:
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        # Plotly Time Series
        fig_line = px.line(
            filtered_df, 
            x='Order_Date', 
            y='Revenue', 
            color='Category',
            title='Revenue Trend Over Time'
        )
        st.plotly_chart(fig_line, use_container_width=True)
        
    with col_chart2:
        # Plotly Bar Chart
        fig_bar = px.bar(
            filtered_df, 
            x='Category', 
            y='Revenue', 
            color='Region', 
            barmode='group',
            title='Total Revenue by Category & Region'
        )
        st.plotly_chart(fig_bar, use_container_width=True)

with tab2:
    st.subheader("Run DuckDB SQL directly on the DataFrame")
    default_query = "SELECT Category, SUM(Revenue) AS Total_Revenue, SUM(Units_Sold) AS Total_Units FROM filtered_df GROUP BY Category ORDER BY Total_Revenue DESC"
    
    user_query = st.text_area("Write SQL Query (Reference the table as `filtered_df`):", value=default_query, height=100)
    
    if st.button("Run SQL Query"):
        try:
            query_result = duckdb.query(user_query).df()
            st.success("Query executed successfully!")
            st.dataframe(query_result, use_container_width=True)
        except Exception as e:
            st.error(f"SQL Error: {e}")

with tab3:
    st.dataframe(filtered_df, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------------
# 5. PROJECT ARCHIVE / CASE STUDY CARDS
# ---------------------------------------------------------
st.header("📂 Additional Case Studies")

proj_col1, proj_col2 = st.columns(2)

with proj_col1:
    st.subheader("Customer Churn Prediction Model")
    st.markdown("""
    * **Tools:** Python, Scikit-learn, XGBoost
    * **Impact:** Reduced churn rate by 14% via targeted retention offers.
    """)
    with st.expander("Read Case Study Summary"):
        st.write("Identified top 5 churn indicators using logistic regression and Random Forest models...")

with proj_col2:
    st.subheader("Automated Financial PDF Extraction Pipeline")
    st.markdown("""
    * **Tools:** Python, Pandas, pdfplumber
    * **Impact:** Reduced manual data extraction time from 8 hours to 2 minutes.
    """)
    with st.expander("Read Case Study Summary"):
        st.write("Extracted structured transaction ledgers from multi-page credit PDFs...")