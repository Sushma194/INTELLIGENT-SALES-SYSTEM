import streamlit as st
import plotly.express as px

def sales_analysis(df):

    st.subheader("📈 Monthly Sales Trend")

    fig = px.line(
        df,
        x="Date",
        y="Sales",
        markers=True,
        title="Sales Growth Over Time"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    st.subheader("💰 Revenue Trend")

    fig2 = px.bar(
        df,
        x="Date",
        y="Revenue",
        title="Monthly Revenue"
    )

    st.plotly_chart(
        fig2,
        width="stretch"
    )

    st.subheader("🥧 Sales Distribution")

    pie = px.pie(
        df,
        values="Sales",
        names="Date",
        title="Sales Share by Month"
    )

    st.plotly_chart(
        pie,
        width="stretch"
    )