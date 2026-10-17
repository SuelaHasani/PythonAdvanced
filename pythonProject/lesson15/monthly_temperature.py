import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("temperature.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Temperature"] = pd.to_numeric(
    df["Temperature"], errors="coerce"
)
df = df.dropna(subset=["Date", "Temperature"])

df["Month"] = df["Date"].dt.month

monthly_avg = df.groupby("Month")["Temperature"].mean()

print(monthly_avg.round(2))

monthly_avg.plot(kind="bar", color="skyblue")
plt.title("Monthly Average Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()