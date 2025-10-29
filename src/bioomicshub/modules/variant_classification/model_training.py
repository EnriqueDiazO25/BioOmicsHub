
from __future__ import annotations
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

def build_variant_pipeline(random_state: int = 42) -> Pipeline:
    pipe = Pipeline([
        ("scaler", StandardScaler(with_mean=False)),
        ("rf", RandomForestClassifier(n_estimators=400, random_state=random_state))
    ])
    return pipe

def train_and_eval(pipe: Pipeline, X: pd.DataFrame, y: pd.Series) -> dict:
    pipe.fit(X, y)
    proba = pipe.predict_proba(X)[:,1] if hasattr(pipe[-1], "predict_proba") else None
    auc = roc_auc_score(y, proba) if proba is not None else None
    return {"auc_on_train": auc}
