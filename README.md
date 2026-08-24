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
