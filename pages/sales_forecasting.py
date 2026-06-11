import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from sklearn.linear_model import LinearRegression

st.title("📈 Sales Forecasting")

if "data" in st.session_state:

    df = st.session_state["data"]

    df["Date"] = pd.to_datetime(df["Date"])

    df["Month"] = np.arange(len(df))

    X = df[["Month"]]
    y = df["Sales"]

    model = LinearRegression()

    model.fit(X,y)

    future_months = np.arange(
        len(df),
        len(df)+6
    ).reshape(-1,1)

    forecast = model.predict(future_months)

    future_dates = pd.date_range(
        start=df["Date"].max(),
        periods=7,
        freq="ME"
    )[1:]

    forecast_df = pd.DataFrame({
        "Date":future_dates,
        "Forecast Sales":forecast
    })

    st.subheader("Forecast Table")

    st.dataframe(
        forecast_df,
        width="stretch"
    )

    fig1 = px.line(
        forecast_df,
        x="Date",
        y="Forecast Sales",
        markers=True,
        title="Future Sales Forecast"
    )

    st.plotly_chart(fig1,width="stretch")

    pie = px.pie(
        forecast_df,
        values="Forecast Sales",
        names=forecast_df["Date"].dt.strftime("%b")
    )

    st.plotly_chart(pie,width="stretch")

else:
    st.warning("Upload Dataset First")