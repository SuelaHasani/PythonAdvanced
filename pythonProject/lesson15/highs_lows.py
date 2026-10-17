import pandas as pd

df = pd.read_csv("temperature.csv")
df["Temperature"] = pd.to_numeric(
    df["Temperature"], errors="coerce"
)
df = df.dropna(subset=["Temperature"])

print("Hottest day: ")
print(df.loc[df["Temperature"].idxmax()])

print("\nColdest day:")
print(df.loc[df["Temperature"].idxmin()])