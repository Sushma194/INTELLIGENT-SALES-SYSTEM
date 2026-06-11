import streamlit as st
import plotly.express as px

st.title("📊 Executive Dashboard")

if "data" in st.session_state:

    df = st.session_state["data"]

    c1,c2,c3 = st.columns(3)

    c1.metric(
        "💰 Revenue",
        f"${df['Revenue'].sum():,.0f}"
    )

    c2.metric(
        "📦 Sales",
        int(df["Sales"].sum())
    )

    c3.metric(
        "📈 Avg Revenue",
        f"${df['Revenue'].mean():,.0f}"
    )

    st.divider()

    col1,col2 = st.columns(2)

    with col1:

        fig1 = px.line(
            df,
            x="Date",
            y="Sales",
            markers=True,
            title="Sales Trend"
        )

        st.plotly_chart(
            fig1,
            width="stretch"
        )

    with col2:

        fig2 = px.bar(
            df,
            x="Date",
            y="Revenue",
            title="Revenue Analysis"
        )

        st.plotly_chart(
            fig2,
            width="stretch"
        )

    pie = px.pie(
        df,
        values="Sales",
        names="Date",
        title="Sales Distribution"
    )

    st.plotly_chart(
        pie,
        width="stretch"
    )

    st.subheader("📋 Dataset")

    st.dataframe(
        df,
        width="stretch"
    )

else:

    st.warning(
        "Upload Dataset First"
    )