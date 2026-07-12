import pandas as pd

df = pd.read_csv("data/raw/trials.csv")

df["days_to_convert"] = (
    pd.to_numeric(
        df["days_to_convert"],
        errors="coerce"
    )
)

df["days_to_convert"] = (
    df["days_to_convert"]
    .astype("Int64")
)

df.to_csv(
    "data/raw/trials.csv",
    index=False
)

print("trials.csv fixed successfully")