import streamlit as st
import pandas as pd
from data_loader import get_crop_data, get_rainfall_data
from analysis_engine import compare_states, best_worst_district, crop_trend, policy_compare
from visuals import show_bar

from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
RESOURCE_ID = os.getenv("RESOURCE_ID")


crop_url = f"https://api.data.gov.in/resource/{RESOURCE_ID}?api-key={API_KEY}&format=csv&limit=50000"
rain_path = "data/rainfall_data.xls"

crop_df = get_crop_data(crop_url)
rain_df = get_rainfall_data(rain_path)

df = pd.merge(crop_df, rain_df, on=["state", "district"], how="left")

st.set_page_config(page_title="KrishiPulse", layout="wide")

st.title("KrishiPulse – Agriculture × Climate Insights")

st.markdown("A small prototype to explore how crop patterns and rainfall data relate across India.")

menu = st.sidebar.radio(
    "Choose a section",
    [
        "Overview",
        "Rainfall vs Crop",
        "Best & Worst Districts",
        "10-Year Trend",
        "Policy Support",
    ],
)

states = sorted(df["state"].dropna().unique())
crops = sorted(df["crop"].dropna().unique())
years = sorted(df["year"].dropna().unique())

if menu == "Overview":
    st.subheader("All India Crop Production Stats")
    c1, c2 = st.columns(2)

    with c1:
        top_states = df.groupby("state")["production"].sum().sort_values(ascending=False).head(10)
        st.write("Top States by Production")
        st.bar_chart(top_states)

    with c2:
        rain_stats = rain_df.groupby("state")["ANNUAL"].mean().sort_values(ascending=False).head(10)
        st.write("States with Highest Average Rainfall")
        st.bar_chart(rain_stats)

    st.markdown("Source: data.gov.in")

elif menu == "Rainfall vs Crop":
    st.subheader("Crop × Rainfall Comparison")

    crop = st.selectbox("Select Crop", crops)
    s1 = st.selectbox("State 1", states)
    s2 = st.selectbox("State 2", states)
    yrs = st.multiselect("Select Years", years)

    if st.button("Run Comparison"):
        p1, p2, r1, r2 = compare_states(df, crop, s1, s2, yrs)
        st.write(f"{s1.title()} – Production: {p1}, Rainfall: {r1}")
        st.write(f"{s2.title()} – Production: {p2}, Rainfall: {r2}")
        st.markdown("Source: data.gov.in")

elif menu == "Best & Worst Districts":
    st.subheader("Best vs Worst Performing Districts")

    st.markdown(
        "This section automatically finds:\n"
        "- The district with **highest production** for the selected crop in State A\n"
        "- The district with **lowest production** for the selected crop in State B\n"
        "- For the same year\n"
    )

    crop = st.selectbox("Select Crop", crops)
    state_best = st.selectbox("State (Best Performer)", states)
    state_worst = st.selectbox("State (Worst Performer)", states, index=1)
    yr = st.selectbox("Select Year", years)

    if st.button("Find Districts"):
        best, worst = best_worst_district(df, crop, state_best, state_worst, yr)

        if best.empty or worst.empty:
            st.error("No data found for this combination. Try changing crop, states, or year.")
        else:
            st.success("Districts identified successfully!")

            col1, col2 = st.columns(2)
            with col1:
                st.write("### Best District")
                st.dataframe(best)

            with col2:
                st.write("### Worst District")
                st.dataframe(worst)

            # Safe bar chart
            try:
                show_bar(best, worst)
            except:
                st.warning("Chart could not be generated for this data.")


elif menu == "10-Year Trend":
    st.subheader("Crop Trend Over Years")

    crop = st.selectbox("Select Crop", crops)
    state = st.selectbox("Select State", states)
    yrs = st.multiselect("Select Years", years)

    if st.button("Show Trend"):
        trend = crop_trend(df, crop, state, yrs)
        st.dataframe(trend)
        st.markdown("Source: data.gov.in")

elif menu == "Policy Support":
    st.subheader("Data Support for Policy Choice")

    a = st.selectbox("Crop A (drought-resistant)", crops)
    b = st.selectbox("Crop B (water-intensive)", crops)
    s = st.selectbox("State", states)
    yrs = st.multiselect("Years", years)

    if st.button("Compare"):
        pa, pb, ra = policy_compare(df, a, b, s, yrs)
        st.write(f"Avg Production of {a}: {pa}")
        st.write(f"Avg Production of {b}: {pb}")
        st.write(f"Avg Rainfall: {ra}")
        st.markdown("Source: data.gov.in")
