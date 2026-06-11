import streamlit as st
import plotly.express as px

st.title("📊 EDA Analysis")

if "data" in st.session_state:

    df = st.session_state["data"]

    st.dataframe(df,width="stretch")

    col1,col2 = st.columns(2)

    with col1:

        fig1 = px.bar(
            df,
            x="Date",
            y="Revenue",
            title="Revenue Analysis"
        )

        st.plotly_chart(
            fig1,
            width="stretch"
        )

    with col2:

        fig2 = px.pie(
            df,
            values="Revenue",
            names="Date",
            title="Revenue Distribution"
        )

        st.plotly_chart(
            fig2,
            width="stretch"
        )

    fig3 = px.scatter(
        df,
        x="Sales",
        y="Revenue",
        size="Revenue",
        title="Sales vs Revenue"
    )

    st.plotly_chart(
        fig3,
        width="stretch"
    )

else:

    st.warning("Upload Dataset First")