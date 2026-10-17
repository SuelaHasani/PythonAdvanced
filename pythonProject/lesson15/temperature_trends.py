import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("temperature.csv")
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Temperature"] = pd.to_numeric(
    df["Temperature"], errors="coerce"
)
df = df.dropna(subset=["Date", "Temperature"])
df = df.sort_values("Date")

plt.figure(figsize=(12, 6))
plt.plot(df["Date"], df["Temperature"], color="blue")

plt.title("Temperature Changes Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()