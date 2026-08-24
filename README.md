# Autonomous Data Analysis & Insights Platform

An end-to-end, multi-agent AI analytics system built with **Streamlit**, **Python**, and **Groq (Llama-3.3-70B)**. The platform automates data cleaning, dynamic parameter mapping, statistical hypothesis testing, conversion funnels, cohort analysis, user retention curves, and executive insights generation directly from raw CSV files.

---

## Architecture Overview



## Core Features
Intelligent LLM Query Routing: Utilizes zero-shot Llama-3.3-70B agents via Groq to parse plain-English analytical questions, identify intent (ab_test, funnel, cohort, retention), and map parameters to dataset schemas without manual user configuration.

Automated Data Processing Pipeline: Runs memory optimization, duplicate record removal, mixed type resolution, and automated numerical/categorical missing value imputation during ingestion.

## Statistical Engines:

- A/B Testing: Computes two-sample Z-tests/t-tests, confidence intervals, relative lift, and Cohen's d effect sizes to evaluate variant significance.

- Funnel Analysis: Tracks conversion rates, identifies friction points, and analyzes step-by-step drop-offs.

- Cohort Analysis: Generates flexible cohort matrices (Daily/Monthly) to track cohort behavior across user lifecycles.

- Retention Curves: Tracks Day 1, 7, and 30 retention metrics dynamically based on signup date attributes.

- Executive Summary Generation: Transforms raw numerical outputs and Plotly charts into plain-language business insights using an automated LLM interpretation agent.

## Tech Stack
Frontend: Streamlit

LLM Engine: Groq API (Llama-3.3-70b-versatile)

Data Processing: Python, Pandas, NumPy, SciPy

Data Visualization: Plotly Interactive Dashboards

## Getting Started
Prerequisites
Python 3.9+

A Groq API key

## Installation
Clone the repository:

Bash
git clone [https://github.com/your-username/autonomous-data-analysis-platform.git](https://github.com/your-username/autonomous-data-analysis-platform.git)
cd autonomous-data-analysis-platform
Create a virtual environment and install dependencies:

Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
Configure environment secrets:
Create a .env file or .streamlit/secrets.toml in the project root:

Ini, TOML
GROQ_API_KEY = "your_groq_api_key_here"
Run the Streamlit application:

Bash
streamlit run app.py
Usage Guide
Upload Dataset: Upload any structured CSV file via the sidebar interface.

Review Data Quality: View the automated audit report, missing value handling log, and optimized preview.

Ask Questions: Input analytical prompts (e.g., "Compare conversion rate between Variant A and Variant B" or "Show me user retention for the past 30 days").

Explore Results: Review the rendered Plotly charts alongside the AI-generated executive summary.
