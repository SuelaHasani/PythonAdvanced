import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Temperature"] = pd.to_numeric(
    df["Temperature"], errors="coerce"
)

df = df.dropna(subset=["Date", "Temperature"])
df = df.sort_values("Date")

print(df.head())
print(f"Average temperature: {df['Temperature'].mean():.2f}")