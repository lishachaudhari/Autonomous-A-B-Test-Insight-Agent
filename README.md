# Autonomous Data Analysis & Insights Platform

An end-to-end, multi-agent AI analytics system built with **Streamlit**, **Python**, and **Groq (Llama-3.3-70B)**. The platform automates data cleaning, dynamic parameter mapping, statistical hypothesis testing, conversion funnels, cohort analysis, user retention curves, and executive insights generation directly from raw CSV files.

---

## Architecture Overview
```mermaid
flowchart TD
    %% Input Layer
    A[User Query & CSV File] --> B[Streamlit UI Interface]
    
    %% Ingestion & Cleaning Engine
    subgraph Data_Pipeline [Data Processing Engine]
        B --> C[Load CSV Dataset]
        C --> D[Data Quality Audit]
        D --> E[Data Cleaning & Imputation]
    end

    %% Intelligence Layer (LLM Routing)
    subgraph LLM_Agents [LLM Intelligence Layer - Llama 3.3 70B via Groq]
        E --> F[Query Classification Agent]
        F -->|Identifies Analysis Types| G[Column & Parameter Selection Agent]
        G -->|Extracts Variant/Metric Parameters| H[Analysis Routing Control]
    end

    %% Statistical & Analytics Modules
    subgraph Analytics_Engine [Statistical Calculation Modules]
        H -->|ab_test| I[A/B Testing Engine]
        H -->|funnel| J[Funnel Analysis Engine]
        H -->|cohort| K[Cohort Matrix Engine]
        H -->|retention| L[Retention Curve Engine]
    end

    %% Visualization & Executive Interpretation
    subgraph Insights_Layer [Visualization & AI Summary]
        I & J & K & L --> M[Interactive Dashboards]
        I & J & K & L --> N[Result Interpretation LLM Agent]
        N --> O[Executive Summary Generation]
    end

    %% Output
    M --> P[Render Interactive Streamlit Analytics Hub]
    O --> P

# Autonomous Data Analysis & Insights Platform

An end-to-end, multi-agent AI analytics system built with **Streamlit**, **Python**, and **Groq (Llama-3.3-70B)**. The platform automates data cleaning, dynamic parameter mapping, statistical hypothesis testing, conversion funnels, cohort analysis, user retention curves, and executive insights generation directly from raw CSV files.

---

## Core Features

* **Intelligent LLM Query Routing:** Utilizes zero-shot Llama-3.3-70B agents via Groq to parse plain-English analytical questions, identify intent (`ab_test`, `funnel`, `cohort`, `retention`), and map parameters to dataset schemas without manual user configuration.
* **Automated Data Processing Pipeline:** Runs memory optimization, duplicate record removal, mixed type resolution, and automated numerical/categorical missing value imputation during ingestion.
* **Statistical Engines:**
  * **A/B Testing:** Computes two-sample Z-tests/t-tests, confidence intervals, relative lift, and Cohen's d effect sizes to evaluate variant significance.
  * **Funnel Analysis:** Tracks conversion rates, identifies friction points, and analyzes step-by-step drop-offs.
  * **Cohort Analysis:** Generates flexible cohort matrices (Daily/Monthly) to track cohort behavior across user lifecycles.
  * **Retention Curves:** Tracks Day 1, 7, and 30 retention metrics dynamically based on signup date attributes.
* **Executive Summary Generation:** Transforms raw numerical outputs and Plotly charts into plain-language business insights using an automated LLM interpretation agent.

---

## Tech Stack

* **Frontend:** Streamlit
* **LLM Engine:** Groq API (Llama-3.3-70b-versatile)
* **Data Processing:** Python, Pandas, NumPy, SciPy
* **Data Visualization:** Plotly Interactive Dashboards

---

## Getting Started

### Prerequisites

* Python 3.9+
* A Groq API key

### Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/autonomous-data-analysis-platform.git](https://github.com/your-username/autonomous-data-analysis-platform.git)
   cd autonomous-data-analysis-platform
