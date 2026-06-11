import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📄 Business Reports")

if "data" in st.session_state:

    df = st.session_state["data"]

    if st.button("📊 Generate Report"):

        st.success("Report Generated Successfully")

        # KPI Section
        st.subheader("📌 Business Summary")

        c1,c2,c3 = st.columns(3)

        c1.metric(
            "Total Sales",
            int(df["Sales"].sum())
        )

        c2.metric(
            "Total Revenue",
            f"${df['Revenue'].sum():,.0f}"
        )

        c3.metric(
            "Average Revenue",
            f"${df['Revenue'].mean():,.0f}"
        )

        st.divider()

        # Dataset Preview
        st.subheader("📋 Report Data")

        st.dataframe(
            df,
            width="stretch"
        )

        # Charts
        col1,col2 = st.columns(2)

        with col1:

            fig1 = px.line(
                df,
                x="Date",
                y="Sales",
                markers=True,
                title="Sales Trend Report"
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
                title="Revenue Report"
            )

            st.plotly_chart(
                fig2,
                width="stretch"
            )

        # Pie Chart
        st.subheader("🥧 Sales Distribution")

        pie = px.pie(
            df,
            values="Sales",
            names="Product",
            title="Product Wise Sales"
        )

        st.plotly_chart(
            pie,
            width="stretch"
        )

        # Statistics
        st.subheader("📈 Statistical Summary")

        st.dataframe(
            df.describe(),
            width="stretch"
        )

        # Download CSV
        csv = df.to_csv(index=False)

        st.download_button(
            label="⬇ Download CSV Report",
            data=csv,
            file_name="sales_report.csv",
            mime="text/csv"
        )

else:

    st.warning(
        "Please Upload Dataset First"
    )