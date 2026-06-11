import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

st.title("🤖 Model Training & Evaluation")

# ---------------- CSS ----------------
st.markdown("""
<style>

.metric-box{
    background:white;
    padding:15px;
    border-radius:15px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.15);
}

.block{
    background: linear-gradient(135deg,#e0f2fe,#f5f3ff);
    padding:15px;
    border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- DATA CHECK ----------------
if "data" in st.session_state:

    df = st.session_state["data"]

    # Date fix
    df["Date"] = pd.to_datetime(df["Date"])

    # Feature engineering
    df["Month"] = np.arange(len(df))

    X = df[["Month"]]
    y = df["Sales"]

    # Model
    model = LinearRegression()
    model.fit(X, y)

    pred = model.predict(X)

    # Metrics
    mae = mean_absolute_error(y, pred)
    r2 = r2_score(y, pred) * 100

    st.success("✅ Model Trained Successfully")

    # KPI Cards
    c1, c2 = st.columns(2)

    c1.metric("📊 Accuracy", f"{r2:.2f}%")
    c2.metric("📉 MAE", round(mae, 2))

    st.divider()

    # ---------------- RESULTS TABLE ----------------
    result = pd.DataFrame({
        "Actual": y,
        "Predicted": pred
    })

    st.subheader("📋 Prediction Results")

    st.dataframe(result, width="stretch")

    # ---------------- GRAPHS ----------------
    col1, col2 = st.columns(2)

    with col1:

        fig1 = px.line(
            result,
            y=["Actual", "Predicted"],
            title="📈 Actual vs Predicted Sales"
        )

        st.plotly_chart(fig1, use_container_width=True)

    with col2:

        pie = px.pie(
            values=[r2, max(0, 100 - r2)],
            names=["Accuracy", "Error"],
            title="🥧 Model Performance"
        )

        st.plotly_chart(pie, use_container_width=True)

    # ---------------- FLOW CHART ----------------
    st.subheader("🔄 Model Training Workflow")

    st.graphviz_chart("""
    digraph G {
        rankdir=LR;

        node [
            shape=box,
            style=filled,
            fillcolor=lightblue,
            fontsize=12
        ];

        Upload [label="📂 Upload Data"];
        Clean [label="🧹 Preprocessing"];
        Train [label="🤖 Train Model"];
        Predict [label="📈 Prediction"];
        Eval [label="📊 Evaluation"];

        Upload -> Clean -> Train -> Predict -> Eval;
    }
    """)

else:
    st.warning("⚠️ Upload Dataset First")