import matplotlib.pyplot as plt
import pandas as pd


def plot_conversion_by_variant(df: pd.DataFrame, savepath=None):
    conv = df.groupby('variant')['converted'].mean().reset_index()
    variants = conv['variant']
    rates = conv['converted']

    # ✅ Create figure and axes explicitly
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(variants, rates)
    ax.set_ylabel('Conversion rate')
    ax.set_title('Conversion rate by variant')
    ax.set_ylim(0, max(rates) * 1.5)

    # Add labels above bars
    for i, v in enumerate(rates):
        ax.text(i, v + 0.005, f"{v:.3f}", ha='center')

    # Optional: save chart
    if savepath:
        fig.savefig(savepath, bbox_inches='tight')

    return fig 


def plot_metric_distribution(df: pd.DataFrame, metric='metric_value'):
    if metric not in df.columns:
        return
    a = df[df['variant']=='A'][metric].dropna()
    b = df[df['variant']=='B'][metric].dropna()

    plt.figure(figsize=(8,4))
    plt.hist(a, bins=30, alpha=0.6, label='A')
    plt.hist(b, bins=30, alpha=0.6, label='B')
    plt.legend()
    plt.title(f'Distribution of {metric} by variant')
    plt.show()
