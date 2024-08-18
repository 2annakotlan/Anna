import streamlit as st
import plotly.express as px
import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    'x': [1, 2, 3, 4],
    'y': [10, 11, 12, 13]
})

# Create a bar chart using plotly.express
fig = px.bar(df, x='x', y='y', title='Plotly Bar Chart')
st.plotly_chart(fig)
