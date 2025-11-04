import pandas as pd
from typing import Tuple, Union, IO

def load_data(path: Union[str, IO]) -> pd.DataFrame:
    """Load CSV and basic cleaning.
    Works with both file paths and Streamlit uploads (file-like objects).
    """
    # Reset file pointer if path is a file-like object
    if hasattr(path, "seek"):
        path.seek(0)

    # Read only header to check for 'timestamp'
    preview_df = pd.read_csv(path, nrows=0)
    parse_dates = ['timestamp'] if 'timestamp' in preview_df.columns else None

    # Reset again before full read
    if hasattr(path, "seek"):
        path.seek(0)

    # Read entire file
    df = pd.read_csv(path, parse_dates=parse_dates)

    # Normalize variant column
    if 'variant' in df.columns:
        df['variant'] = df['variant'].astype(str).str.upper()

    # Quick sanity checks
    assert 'variant' in df.columns and 'converted' in df.columns, \
        "CSV must contain 'variant' and 'converted' columns"

    return df


def prepare_aggregates(df: pd.DataFrame) -> Tuple[pd.DataFrame, dict]:
    """Return aggregated metrics by variant and a summary dict."""
    # Ensure required columns exist
    required_cols = {'user_id', 'variant', 'converted'}
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")

    # Handle optional metric_value column safely
    if 'metric_value' not in df.columns:
        df['metric_value'] = None  # placeholder

    agg = df.groupby('variant').agg(
        users=('user_id', 'nunique'),
        conversions=('converted', 'sum'),
        conversion_rate=('converted', 'mean'),
        metric_mean=('metric_value', 'mean')
    ).reset_index()

    summary = {
        row.variant: {
            'N': int(row.users),
            'conversions': int(row.conversions),
            'conversion_rate': float(row.conversion_rate),
            'metric_mean': None if pd.isna(row.metric_mean) else float(row.metric_mean)
        }
        for row in agg.itertuples()
    }

    return agg, summary
