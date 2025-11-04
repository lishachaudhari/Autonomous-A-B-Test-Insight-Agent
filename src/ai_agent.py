import os
from groq import Groq
from typing import Dict
client = Groq(api_key="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") 

PROMPT_TEMPLATE = '''
You are an expert data scientist. Given the experiment statistics below, produce:
1) A short executive summary (2-3 sentences).
2) A clear interpretation of significance and effect size.
3) 3 actionable recommendations (concise).
4) A short note on what further checks or sanity tests to run.

Experiment stats:
{stats}

Write the output as plain text with headers.
'''


def build_stats_text(stats: Dict) -> str:
    return "\n".join(f"{k}: {v}" for k, v in stats.items())

def generate_ai_insights(stats: Dict, model="llama-3.3-70b-versatile", temperature=0.2):
    prompt = PROMPT_TEMPLATE.format(stats=build_stats_text(stats))
    chat = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400
    )
    return chat.choices[0].message.content.strip()
