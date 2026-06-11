import streamlit as st
import plotly.express as px

def inventory_analysis(df):

    st.subheader("📦 Inventory Analysis")

    fig=px.bar(
        df,
        x="Product",
        y="Inventory"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )