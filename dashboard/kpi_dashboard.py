import streamlit as st

def show_kpis(df):

    c1,c2,c3=st.columns(3)

    c1.metric(
        "💰 Total Revenue",
        f"${df['Revenue'].sum():,.0f}"
    )

    c2.metric(
        "📦 Total Sales",
        int(df['Sales'].sum())
    )

    c3.metric(
        "📈 Avg Revenue",
        f"${df['Revenue'].mean():,.0f}"
    )