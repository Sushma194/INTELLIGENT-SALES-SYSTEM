import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📦 Inventory Optimization")

avg_demand = st.slider(
    "Average Demand",
    50,500,100
)

lead_time = st.slider(
    "Lead Time",
    1,20,5
)

safety_stock = st.slider(
    "Safety Stock",
    10,200,20
)

rop = (
    avg_demand *
    lead_time +
    safety_stock
)

c1,c2 = st.columns(2)

c1.metric(
    "Safety Stock",
    safety_stock
)

c2.metric(
    "Reorder Point",
    rop
)

inventory_df = pd.DataFrame({
    "Category":[
        "Demand",
        "Lead Time",
        "Safety Stock",
        "ROP"
    ],
    "Value":[
        avg_demand,
        lead_time,
        safety_stock,
        rop
    ]
})

fig = px.bar(
    inventory_df,
    x="Category",
    y="Value",
    title="Inventory Analysis"
)

st.plotly_chart(
    fig,
    width="stretch"
)

pie = px.pie(
    inventory_df,
    values="Value",
    names="Category"
)

st.plotly_chart(
    pie,
    width="stretch"
)