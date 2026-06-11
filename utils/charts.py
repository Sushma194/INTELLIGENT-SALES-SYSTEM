import plotly.express as px

def sales_chart(df):

    fig=px.line(
        df,
        x='Date',
        y='Sales'
    )

    return fig