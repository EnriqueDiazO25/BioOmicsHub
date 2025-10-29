
from __future__ import annotations
import pandas as pd
from bioomicshub.core.preprocessing import standardize_columns, zscore
from bioomicshub.core.visualization import bubble_plot

def main():
    df = pd.DataFrame({
        "Category": ["A","A","B","B","C"],
        "x": [1,2,3,4,5],
        "y": [5,4,3,2,1],
        "size": [10,30,50,40,20]
    })
    df = standardize_columns(df)
    fig = bubble_plot(df, "x", "y", "size")
    fig.savefig("bubble_example.png")
    print("OK -> bubble_example.png")

if __name__ == "__main__":
    main()
