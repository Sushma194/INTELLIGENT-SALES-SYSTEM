import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📂 Data Upload")

file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if file:

    df = pd.read_csv(file)

    st.session_state["data"] = df

    st.success("Dataset Uploaded Successfully")

    c1,c2,c3 = st.columns(3)

    c1.metric("Rows",df.shape[0])
    c2.metric("Columns",df.shape[1])
    c3.metric("Sales",int(df["Sales"].sum()))

    st.subheader("Dataset")

    st.dataframe(df,width="stretch")

    col1,col2 = st.columns(2)

    with col1:

        fig = px.line(
            df,
            x="Date",
            y="Sales",
            markers=True,
            title="Sales Trend"
        )

        st.plotly_chart(fig,width="stretch")

    with col2:

        pie = px.pie(
            df,
            values="Sales",
            names="Date",
            title="Sales Distribution"
        )

        st.plotly_chart(pie,width="stretch")

else:

    st.info("Upload Dataset")