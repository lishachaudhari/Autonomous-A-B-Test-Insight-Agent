#  Autonomous A/B Test Insight Agent



###  AI-powered A/B testing dashboard — analyze experiments, visualize insights, and get instant data-driven recommendations.

---

##  Overview

**Autonomous A/B Test Insight Agent** is an interactive **Streamlit dashboard** that automates your A/B testing workflow.  
It combines **classical statistical analysis** with **Groq-based AI insights**, so you can instantly interpret test results and make confident business decisions.

---

##  Features

- **Upload Data:** Accepts CSVs with columns like `variant`, `converted`, and optional `metric_value`.  
- **Statistical Analysis:** Performs two-proportion z-tests, calculates lift & effect size.  
- **AI Insights (Groq):** Generates executive summaries, significance interpretation, and actionable recommendations.  
- **Visualization:** Conversion rate and metric distribution charts.  
- **Interactive Dashboard:** No code required — runs locally with Streamlit.

---

##  Tech Stack

| Component | Purpose |
|------------|----------|
| **Python 3.9+** | Core programming language |
| **Streamlit** | Front-end dashboard |
| **Pandas / NumPy / SciPy** | Statistical analysis |
| **Matplotlib** | Visualizations |
| **Groq API (LLM)** | AI-generated insights |

---

##  Installation

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

##  Sample AI Output (Groq)

Executive Summary: Variant B shows a statistically significant improvement in conversion (+3.1%) with a p-value of 0.02.
Interpretation: The lift is moderate but reliable at 95% confidence.
Recommendations:

Roll out Variant B gradually.

Re-validate with a longer timeframe.

Segment results by geography or traffic source.

---

##   Dashboard Preview

Example Streamlit interface — Upload CSV → Run Analysis → Get Instant AI Insights

<img width="439" height="588" alt="image" src="https://github.com/user-attachments/assets/7a69d3a5-bd0c-4be3-b86b-4f834939034f" />
<img width="444" height="567" alt="image" src="https://github.com/user-attachments/assets/e50cfa9b-eda7-4e5a-a0b8-ada528ea79c0" />
<img width="450" height="245" alt="image" src="https://github.com/user-attachments/assets/ddda7d84-96e4-4400-bfe6-56288d4fa2e4" />

---

##   Project Structure
<img width="395" height="219" alt="image" src="https://github.com/user-attachments/assets/e1fef218-f061-49c1-89be-5491b6db8543" />

---

##   Future Enhancements

- Add Bayesian A/B testing
- Support multi-variant (A/B/n) experiments
- Integrate experiment tracking (e.g., MLflow)
- Add automated report generation (PDF/Markdown)

