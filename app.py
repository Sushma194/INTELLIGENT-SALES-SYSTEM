import streamlit as st

st.set_page_config(
    page_title="AI Intelligent Sales System",
    page_icon="📈",
    layout="wide"
)

st.markdown("""
<style>

.main{
background:#f4f7fc;
}

[data-testid="stSidebar"]{
background:#1e293b;
}

[data-testid="stSidebar"] *{
color:white;
}

div[data-testid="metric-container"]{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0 4px 15px rgba(0,0,0,0.15);
border-left:6px solid #2563eb;
}

h1,h2,h3{
color:#0f172a;
}

.stDataFrame{
background:white;
border-radius:15px;
}

</style>
""",unsafe_allow_html=True)

st.title("📈 Intelligent Sales Forecasting & Inventory Optimization")

st.success("AI Powered Business Intelligence Dashboard")

st.markdown("""
### Features

✅ Data Upload

✅ Data Preprocessing

✅ EDA Analysis

✅ Model Training

✅ Sales Forecasting

✅ Inventory Optimization

✅ Reports

✅ Dashboard
""")
st.markdown("""
<style>

.main{
background: linear-gradient(
135deg,
#dbeafe,
#f3e8ff,
#fef9c3
);
}

[data-testid="stSidebar"]{
background: linear-gradient(
180deg,
#2563eb,
#7c3aed
);
}

[data-testid="stSidebar"] *{
color:white;
}

div[data-testid="metric-container"]{
background:white;
padding:20px;
border-radius:20px;
box-shadow:0 8px 20px rgba(0,0,0,0.15);
transition:0.3s;
}

div[data-testid="metric-container"]:hover{
transform:scale(1.05);
}

.stDataFrame{
background:white;
border-radius:15px;
}

</style>
""",unsafe_allow_html=True)