import numpy as np
import pandas as pd
from typing import Dict
from scipy import stats


def cal_lift_stats(df: pd.DataFrame, control='A', treatment='B') -> Dict:
    #Calculate conversion lift, p-value (two-proportion z-test), and effect size.
    #Returns a result dict."""
    a = df[df['variant'] == control]
    b = df[df['variant'] == treatment]
    
    n_a = len(a)
    n_b = len(b)
    conv_a = a['converted'].sum()
    conv_b = b['converted'].sum()

    rate_a = conv_a / n_a
    rate_b = conv_b / n_b
    lift = (rate_b - rate_a) / rate_a if rate_a > 0 else None
    # Two-proportion z-test
    p_pool = (conv_a + conv_b) / (n_a + n_b)
    se = np.sqrt(p_pool * (1 - p_pool) * (1/n_a + 1/n_b))
    z = (rate_b - rate_a) / se
    p_value = 2 * (1 - stats.norm.cdf(abs(z)))

    # t-test on metric_value if present
    ttest_res = None
    if 'metric_value' in df.columns:
        ttest_res = stats.ttest_ind(a['metric_value'].dropna(), b['metric_value'].dropna(), equal_var=False)

    return {
        'control': control,
        'treatment': treatment,
        'n_control': n_a,
        'n_treatment': n_b,
        'conv_control': int(conv_a),
        'conv_treatment': int(conv_b),
        'rate_control': rate_a,
        'rate_treatment': rate_b,
        'lift': lift,
        'z': float(z),
        'p_value': float(p_value),
        'ttest': {
            'statistic': float(ttest_res.statistic),
            'pvalue': float(ttest_res.pvalue)
        } if ttest_res is not None else None
    }


