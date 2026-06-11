import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🧹 Data Preprocessing")

# Colorful CSS
st.markdown("""
<style>

.main{
background: linear-gradient(
135deg,
#dbeafe,
#f0f9ff,
#e0f2fe
);
}

.box{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,0.15);
}

</style>
""",unsafe_allow_html=True)

if "data" in st.session_state:

    df = st.session_state["data"]

    st.subheader("📋 Original Dataset")

    st.dataframe(df,width="stretch")

    col1,col2 = st.columns(2)

    with col1:
        st.metric(
            "Rows",
            df.shape[0]
        )

    with col2:
        st.metric(
            "Columns",
            df.shape[1]
        )

    st.subheader("Missing Values")

    missing = pd.DataFrame({
        "Column":df.columns,
        "Missing":df.isnull().sum().values
    })

    st.dataframe(missing,width="stretch")

    fig1 = px.bar(
        missing,
        x="Column",
        y="Missing",
        title="Missing Values Analysis"
    )

    st.plotly_chart(
        fig1,
        width="stretch"
    )

    if st.button("🧹 Clean Data"):

        clean_df = df.copy()

        clean_df.drop_duplicates(
            inplace=True
        )

        clean_df.fillna(
            0,
            inplace=True
        )

        st.success(
            "Data Cleaned Successfully"
        )

        st.subheader(
            "✅ Cleaned Dataset"
        )

        st.dataframe(
            clean_df,
            width="stretch"
        )

        st.session_state[
            "data"
        ] = clean_df

        # Comparison KPIs

        c1,c2,c3 = st.columns(3)

        c1.metric(
            "Original Rows",
            df.shape[0]
        )

        c2.metric(
            "Clean Rows",
            clean_df.shape[0]
        )

        c3.metric(
            "Duplicates Removed",
            df.shape[0]-
            clean_df.shape[0]
        )

        # Sales Chart

        st.subheader(
            "📈 Sales Analysis"
        )

        fig2 = px.line(
            clean_df,
            x="Date",
            y="Sales",
            markers=True,
            title="Sales Trend"
        )

        st.plotly_chart(
            fig2,
            width="stretch"
        )

        # Revenue Chart

        fig3 = px.bar(
            clean_df,
            x="Date",
            y="Revenue",
            title="Revenue Analysis"
        )

        st.plotly_chart(
            fig3,
            width="stretch"
        )

        # Pie Chart

        fig4 = px.pie(
            clean_df,
            values="Sales",
            names="Date",
            title="Sales Distribution"
        )

        st.plotly_chart(
            fig4,
            width="stretch"
        )

        # Flow Chart

        st.subheader(
            "🔄 Data Cleaning Flow"
        )

        st.markdown("""
        ```text
        Raw Dataset
              │
              ▼
        Remove Duplicates
              │
              ▼
        Handle Missing Values
              │
              ▼
        Feature Validation
              │
              ▼
        Clean Dataset
              │
              ▼
        Ready For Model Training
        ```
        """)

else:

    st.warning(
        "Upload Dataset First"
    )