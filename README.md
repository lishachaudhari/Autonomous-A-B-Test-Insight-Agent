# 🚀 Autonomous A/B Test Insight Agent

[![Built with Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![Powered by Groq](https://img.shields.io/badge/Powered%20by-Groq%20LLM-FF6B00?logo=groq)](https://groq.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

### 🧠 AI-powered A/B testing dashboard — analyze experiments, visualize insights, and get instant data-driven recommendations.

---

## ✨ Overview

**Autonomous A/B Test Insight Agent** is an interactive **Streamlit dashboard** that automates your A/B testing workflow.  
It combines **classical statistical analysis** with **Groq-based AI insights**, so you can instantly interpret test results and make confident business decisions.

---

## 🔍 Features

✅ **📂 Upload Data:** Accepts CSVs with columns like `variant`, `converted`, and optional `metric_value`.  
✅ **📊 Statistical Analysis:** Performs two-proportion z-tests, calculates lift & effect size.  
✅ **🧠 AI Insights (Groq):** Generates executive summaries, significance interpretation, and actionable recommendations.  
✅ **📈 Visualization:** Conversion rate and metric distribution charts.  
✅ **💻 Interactive Dashboard:** No code required — runs locally with Streamlit.

---

## 🧩 Tech Stack

| Component | Purpose |
|------------|----------|
| **Python 3.9+** | Core programming language |
| **Streamlit** | Front-end dashboard |
| **Pandas / NumPy / SciPy** | Statistical analysis |
| **Matplotlib** | Visualizations |
| **Groq API (LLM)** | AI-generated insights |

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/ab-test-insight-agent.git
   cd ab-test-insight-agent
2. **Create and activate a virtual environment**
   ```bash
   Copy code
   python -m venv venv
   source venv/bin/activate       # (Mac/Linux)
   venv\Scripts\activate          # (Windows)
3. **Install dependencies**
   ```bash
   Copy code
   pip install -r requirements.txt
4. **Set your Groq API key**
   ```bash
   Copy code
   export GROQ_API_KEY="your_api_key_here"     # Mac/Linux
   setx GROQ_API_KEY "your_api_key_here"       # Windows
5. **Run the App**
   ```bash
   streamlit run app.py

---
##   📊 Example Input Data
user_id	variant	converted	metric_value
1	A	0	12.5
2	B	1	14.2
3	A	0	10.8
4	B	1	15.1
## 🧠 Sample AI Output (Groq)

Executive Summary: Variant B shows a statistically significant improvement in conversion (+3.1%) with a p-value of 0.02.
Interpretation: The lift is moderate but reliable at 95% confidence.
Recommendations:

Roll out Variant B gradually.

Re-validate with a longer timeframe.

Segment results by geography or traffic source.

##  📈 Dashboard Preview

Example Streamlit interface — Upload CSV → Run Analysis → Get Instant AI Insights

(Add a screenshot here if available)

![Dashboard Preview](assets/dashboard_preview.png)

##  🗂️ Project Structure
ab-test-insight-agent/
│
├── app.py                   # Streamlit main dashboard
├── src/
│   ├── data_loader.py       # Load and preprocess data
│   ├── statistical_tests.py # Run A/B test calculations
│   ├── ai_agent.py          # Groq API integration
│   └── visualize.py         # Plot charts
│
├── requirements.txt
└── README.md

##  🌟 Future Enhancements

Add Bayesian A/B testing

Support multi-variant (A/B/n) experiments

Integrate experiment tracking (e.g., MLflow)

Add automated report generation (PDF/Markdown)

## 👩‍💻 Author

Lisha Chaudhari
📊 Data Scientist | AI & Experimentation Enthusiast
