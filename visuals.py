import streamlit as st
import pandas as pd

def show_bar(best, worst):
    if best.empty or worst.empty:
        return

    data = pd.DataFrame({
        "District": [best['district'].iloc[0], worst['district'].iloc[0]],
        "Production": [best['production'].iloc[0], worst['production'].iloc[0]],
    })

    st.bar_chart(data.set_index("District"))