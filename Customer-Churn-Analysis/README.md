# 📊 Customer Churn Analysis Dashboard (Power BI)
---
## 🧠 Overview

This project analyzes customer churn behavior for a telecom company using **Power BI**.
<br>
It focuses on how **contract types, payment methods, internet services**, and customer tenure influence churn, with **DAX-driven** interactive insights and tooltips.

---

## 📌 Key Highlights

**💡 Overall Churn Rate: 26.6%**

**📉 Highest churn: Month-to-month customers (42.7%)**

**📈 Lowest churn: Two-year contracts (2.8%)**

**🔍 High-risk segments:**

  - **Fiber Optic** internet users (41.9% churn)

  - **Electronic Check** payments (45.3% churn)

**🧩 Custom DAX Tooltips:** Provide contract-wise, internet, and payment breakdown insights

**🎯 Interactive Slicers:** Contract, Internet Service, Payment Method, Gender, Senior Citizen

**🧮 DAX Measures:**

  - Churn Rate %

  - Churned Customers

  - Avg Monthly Charges

  - Custom insight measures for tooltip pages
---

## 🗂️ Power BI Dashboard Overview

| Page | Purpose |
|------|----------|
| 1️⃣ **Main Dashboard** | Main churn dashboard with KPIs and segment analysis |
| 2️⃣ **TT Contract** | Contract-wise deep-dive with tooltip insights |
| 3️⃣ **TT Payment** | Churn distribution by payment methods |
| 4️⃣ **TT Internet** | Churn analysis by internet service type |
| 5️⃣ **TT Tenure** | Tenure-based customer retention trend |
| 6️⃣ **TT Monthly** | Quintile-based monthly charge analysis |
| 7️⃣ **TT Contract Donut** | Distribution of internet and payment types within each contract |

---

## 🧩 DAX Logic Example

DAX
```
Churn Rate % = 
DIVIDE(
    [Churned Customers],
    [Customers],
    0
)
```

DAX
```
Contract Donut Insight =
VAR ContractType = SELECTEDVALUE(telco_dataset_cleaned[contract])
RETURN
SWITCH(
    TRUE(),
    ContractType = "Month-to-month",
        "Majority of short-term customers use Fiber Optic Internet and" & UNICHAR(10) &
        "Electronic Check payments, which strongly link to higher churn risk.",
    ContractType = "One year",
        "Balanced distribution across internet and payment types indicates moderate loyalty;" & UNICHAR(10) &
        "opportunities exist to convert to longer-term plans.",
    ContractType = "Two year",
        "Stable and diversified base with higher share of Credit Card and Bank Transfer users" & UNICHAR(10) &
        "representing the most loyal customer group.",
    "Select a contract type."
)
```
---

## 📈 Key Business Insights

  - 📊 Customers with short-term contracts show higher churn due to lack of retention offers.

  - 💳 Electronic check payments are a strong churn indicator—customers prefer more secure options.

  - 🌐 Fiber optic service customers churn more, likely due to performance or pricing dissatisfaction.

  - 💰 High monthly charge quintiles experience medium churn—highlighting upsell but risk potential.

  - 🕒 Loyalty improves with tenure—customers over 4 years have <10% churn.

---

## 🧰 Tools & Technologies

|Tool|Purpose|
|----|-------|
|🧠 **Power BI**|Dashboard visualization|
|🧮 **DAX**|Calculations and insights|
|🧹 **Excel/CSV**|Data preprocessing|
|📊 **Power Query**|Cleaning & transformation|

---

## 📸 Dashboard Preview
![Main Dashboard Preview](./Dashboard_Screenshots/Main_Dashboard.png)

---


