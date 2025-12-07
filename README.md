# Manufacturing Performance Analysis – Equipment Efficiency (2024)

**Author:** 23f1002718@ds.study.iitm.ac.in  

This repository contains an LLM-assisted analysis of equipment efficiency for a manufacturing company, using quarterly performance data from 2024 and comparing it to the industry benchmark.

---

## 1. Business Context

The company has observed rising downtime and maintenance costs, and the current **average equipment efficiency rate is 74.88**, which is significantly below the **industry target of 90**.  
The executive team needs a clear, data-driven story to decide whether to invest in a **predictive maintenance program** and how to prioritize resources for the next fiscal year.

---

## 2. Dataset

For this analysis, we use quarterly equipment efficiency data:

| Quarter | Efficiency |
|--------:|-----------:|
| Q1      | 71.86      |
| Q2      | 72.50      |
| Q3      | 76.00      |
| Q4      | 79.14      |

- **Average (2024):** 74.88  
- **Industry Target:** 90

---

## 3. Analysis Approach

The analysis was implemented in **Python** (`analysis.py`) with:

- Pandas for basic data handling  
- Matplotlib for visualization  
- Simple summaries:
  - Average efficiency
  - Gap between current performance and the benchmark target

Visualizations (created by the code):

1. Line chart: efficiency per quarter vs industry target  
2. Bar chart: each quarter’s efficiency vs industry target  

---

## 4. Key Findings

1. **Always below target**  
   - Every quarter is below the **benchmark of 90**.  
   - Best quarter: **Q4 (79.14)**, still ~11 points below target.

2. **Improvement, but too slow**  
   - Q1 = 71.86 → Q4 = 79.14  
   - Trend is going up, but not enough to reach 90 soon.

3. **Big gap on average**  
   - **Average efficiency:** 74.88  
   - **Gap to target:** 90 − 74.88 ≈ **15.12 points**  

4. **Likely cause: downtime & maintenance issues**  
   - Low efficiency usually means:
     - More unplanned downtime  
     - Higher reactive maintenance  
     - Higher repair cost and disruption  

---

## 5. Business Implications

- **Higher cost per unit** – Machines are not working at their best, so production is less efficient.  
- **Capacity risk** – Harder to meet demand without overtime or extra shifts.  
- **Strategic risk** – Long-term, running below the industry target can make the company less competitive.

---

## 6. Recommendations – How to reach 90

To close the gap between **74.88** and **90**, the company should not rely only on reactive or fixed-schedule maintenance.

**Main recommendation:**  
👉 **Implement predictive maintenance program.**

### What predictive maintenance means

- Use sensors and data to track machine health (vibration, temperature, etc.).
- Predict failures **before** they happen.
- Plan maintenance when it causes the least disturbance.

### Steps

1. **Start with critical machines**
   - Pick the top machines that cause the most downtime.
2. **Collect data**
   - Install sensors, log failures, and repair history.
3. **Build alerts**
   - Simple rules or models that say:  
     “This machine is behaving abnormally → check it soon.”
4. **Measure impact**
   - Target:
     - Increase efficiency by **3–5 points** in the next 2–3 quarters.
     - Reduce unplanned downtime by **10–15%**.

Over 1–2 years, with continuous improvement, the company can move from **74.88 → 80+ → 90**.

---

## 7. LLM Assistance

This project used an LLM coding assistant (e.g., Jules / ChatGPT Codex) to:

- Generate the Python code (`analysis.py`)
- Suggest visualization logic
- Help write this data story for executives
