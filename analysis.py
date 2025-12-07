"""
Manufacturing Equipment Efficiency Analysis - 2024

Author: 23f1002718@ds.study.iitm.ac.in
"""

import matplotlib.pyplot as plt
import pandas as pd

# Quarterly equipment efficiency data (2024)
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "Efficiency": [71.86, 72.50, 76.00, 79.14],
}

industry_target = 90  # Benchmark target

df = pd.DataFrame(data)

# Calculate average efficiency
average_efficiency = df["Efficiency"].mean()
print("Average efficiency:", round(average_efficiency, 2))

# ---- Visualization 1: Line chart of efficiency over quarters ----
plt.figure()
plt.plot(df["Quarter"], df["Efficiency"], marker="o", label="Equipment Efficiency")
plt.axhline(industry_target, linestyle="--", label="Industry Target (90)")
plt.title("Quarterly Equipment Efficiency - 2024")
plt.xlabel("Quarter")
plt.ylabel("Efficiency Rate")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("efficiency_trend_vs_target.png")
plt.close()

# ---- Visualization 2: Bar chart comparison by quarter ----
plt.figure()
plt.bar(df["Quarter"], df["Efficiency"])
plt.axhline(industry_target, linestyle="--", label="Industry Target (90)")
plt.title("Quarterly Equipment Efficiency vs Industry Target")
plt.xlabel("Quarter")
plt.ylabel("Efficiency Rate")
plt.legend()
plt.tight_layout()
plt.savefig("efficiency_bar_vs_target.png")
plt.close()

# Optional: Simple text-based insight
gap_to_target = industry_target - average_efficiency
print(f"Average gap to target: {gap_to_target:.2f} points")
