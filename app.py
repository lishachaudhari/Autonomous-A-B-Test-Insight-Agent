import streamlit as st
import pandas as pd
from src.data_loader import load_data, prepare_aggregates
from src.statistical_tests import cal_lift_stats
from src.ai_agent import generate_ai_insights
from src.visualize import plot_conversion_by_variant, plot_metric_distribution

st.set_page_config(page_title='A/B Test Insight Agent')
st.title('Autonomous A/B Test Insight Agent')

uploaded = st.file_uploader('Upload CSV', type=['csv'])
if uploaded is not None:
    df = load_data(uploaded)
    agg, summary = prepare_aggregates(df)
    st.write('Aggregated metrics:')
    st.dataframe(agg)

    if st.button('Run Analysis'):
        st.info('Running statistical tests...')
        results = cal_lift_stats(df)
        st.write('Statistics:')
        st.json(results)

        st.info('Generating AI summary...')
        ai_text = generate_ai_insights(results)
        st.subheader('AI Insights')
        st.write(ai_text)

        st.subheader('Conversion chart')
        fig = plot_conversion_by_variant(df)
        st.pyplot(fig)


else:
    st.info('Upload a CSV with `variant` and `converted` columns to get started.')
