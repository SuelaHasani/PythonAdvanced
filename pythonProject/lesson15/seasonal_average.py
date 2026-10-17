import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("temperature.csv")
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Temperature"] = pd.to_numeric(
    df["Temperature"], errors="coerce"
)
df = df.dropna(subset=["Date", "Temperature"])

seasons = {
    12: "Winter", 1: "Winter", 2: "Winter",
    3: "Spring", 4: "Spring", 5: "Spring",
    6: "Summer", 7: "Summer", 8: "Summer",
    9: "Autumn", 10: "Autumn", 11: "Autumn"
}

df["Season"] = df["Date"].dt.month.map(seasons)

seasonal_avg = df.groupby("Season")["Temperature"].mean()
seasonal_avg = seasonal_avg.reindex(
    ["Winter", "Spring", "Summer", "Autumn"]
)

print(seasonal_avg.round(2))

seasonal_avg.plot(kind="bar", color="orange")
plt.title("Seasonal Average Temperature")
plt.xlabel("Season")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()