
from __future__ import annotations
import pandas as pd
import numpy as np
from typing import Iterable, Optional

def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    return df

def zscore(df: pd.DataFrame, cols: Optional[Iterable[str]] = None) -> pd.DataFrame:
    """Aplica z-score a columnas numéricas."""
    df = df.copy()
    cols = cols or df.select_dtypes(include=np.number).columns
    df[cols] = (df[cols] - df[cols].mean()) / df[cols].std(ddof=0).replace(0, np.nan)
    return df

def filter_low_expression(df: pd.DataFrame, min_mean: float = 1.0) -> pd.DataFrame:
    num_cols = df.select_dtypes(include=np.number).columns
    keep = df[num_cols].mean(axis=1) >= min_mean
    return df.loc[keep].copy()
