# 📊 Customer Churn Analysis Dashboard (Power BI + Python + SQL)

## 🎯 Objective: 
To analyze customer churn behavior, identify key factors influencing attrition, and deliver actionable insights to reduce churn and improve customer retention.

---
## 🧠 Overview

This project presents an end-to-end **Customer Churn Analysis** for a telecom company.<br>
Starting from **data cleaning** and **exploratory data analysis** in **Python**, moving through **SQL** segmentation, culminating in an interactive **Power BI dashboard**, and extending into a **machine learning classification model** that predicts individual customer churn risk — the goal was to uncover behavioral patterns behind customer churn and derive data-driven recommendations for retention strategies.

---

## 🧾 Dataset Information

**Source:** [`Telco Customer Churn Dataset (Kaggle)`↗️](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

**File Used:** WA_Fn-UseC_-Telco-Customer-Churn.csv

### 📚 Data Dictionary

| Column | Description | Data Type |
|------|-----|---------|
| `customerID` | Unique identifier for each customer | String|
| `gender` | Customer gender (Male/Female) | String |
| `SeniorCitizen` | Indicates if the customer is a senior citizen (1/0) | Integer |
| `Partner` | Whether the customer has a partner | String |
| `Dependents` | Whether the customer has dependents |	String |
| `tenure` |	Number of months the customer has stayed |	Integer |
|  `Contract` |	Type of contract (Month-to-month, One year, Two year) |	String |
|  `InternetService` |	Internet type (DSL, Fiber optic, No) |	String |
|  `PaymentMethod` |	Billing method (Electronic check, Credit card, etc.) 	| String |
|  `MonthlyCharges` |	Amount charged to the customer monthly |	Float |
|  `TotalCharges`  |	Total amount charged  |	Float  |
|  `Churn` |	Whether the customer left the company |	String |

---

## ⚙️ Installation & Setup

You can run this project in two ways: **directly on Google Colab** or **locally on your system**.

---

### ▶️ Option 1: Run on Google Colab (Recommended)
No installation needed — just open the notebook and start running.

**Data Exploration:**
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Harsh1574/data-analytics-portfolio/blob/main/Customer-Churn-Analysis/Notebooks/01_data_overview.ipynb)

**Exploratory Data Analysis:**
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Harsh1574/data-analytics-portfolio/blob/main/Customer-Churn-Analysis/Notebooks/02_data_eda.ipynb)

**Churn Prediction Model:**
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Harsh1574/data-analytics-portfolio/blob/main/Customer-Churn-Analysis/Notebooks/03_churn_model.ipynb)

---

### 💻 Option 2: Run Locally
1. #### 📥 Clone this repository:
   ```bash
   git clone https://github.com/Harsh1574/data-analytics-portfolio.git
   cd data-analytics-portfolio/Customer_Churn_Analysis
   ```

_This project requires Python 3.9+ and packages listed in [`requirements.txt`](./requirements.txt). To install dependencies run the command in Step 2👇_

2. #### ⚙️ Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. #### 🚀 Launch Jupyter Notebook:
   ```bash
   # Launch notebooks for data exploration
   jupyter notebook Notebooks/01_data_overview.ipynb

   # Launch notebooks for exploratory data analysis
   jupyter notebook Notebooks/02_data_eda.ipynb

   # Launch notebook for churn prediction model
   jupyter notebook Notebooks/03_churn_model.ipynb
   ```
---

## 🧹 Data Preparation (Python)

- Performed data cleaning and transformation using Pandas:

- Handled missing and inconsistent values (TotalCharges nulls converted, data types fixed).

- Removed duplicates and whitespace inconsistencies.

- Standardized categorical columns (title case, unified naming).

- Created tenure_band and mc_quint (Monthly Charge Quintiles) for segmentation.

- Exported clean dataset → [`telco_dataset_cleaned.csv`](.Datasets/telco_dataset_cleaned.csv).

📁 File Location: `./Datasets/telco_dataset_cleaned.csv`

---

## 🧮 Exploratory Data Analysis (Python)

**Libraries Used:**
`pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`

- Performed detailed EDA to identify churn drivers:

- Churn distribution & overall rate

- Tenure vs Churn % trend

- Contract Type vs Churn Rate

- Monthly Charges & Payment Method influence

### 🖼️ Preview Charts:

![](./Screenshots/scatter_tenure_vs_monthly_charges.png)

![](./Screenshots/churn_by_contract.png)

![](./Screenshots/tenure_dist_by_churn.png)

![](./Screenshots/churn_vs_tenure_trend.png)

_All the visualizations are available in the [`Screenshots`](./Screenshots/) folder._

---

## 🧩 SQL Analysis
A few SQL queries were written to validate churn trends and segment data before Power BI visualization:

sql
```
SELECT Contract, 
       ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS ChurnRate
FROM telco_churn
GROUP BY Contract;
```
**📁 File Location:** [`./Notebooks/02_data_eda.ipynb`]

_To view the exploratory data analysis (EDA) file, [`click here`](./Notebooks/02_data_eda.ipynb)._

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

## 📊 Power BI Dashboard

The Power BI dashboard provides a clear, interactive view of churn patterns with:

- KPI Cards (Customers, Churned, Churn Rate %)

- Churn by Tenure Bands

- Churn by Contract Type

- Churn by Internet Service

- Churn by Payment Method

- Churn by Monthly Charges Quintiles

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
## 📸 Dashboard Preview
[Main Dashboard Preview](./Dashboard_Screenshots/Main_Dashboard.png)

_[**`Power BI Dashboard`**](./PBIX_File/Customer_Churn_Dashboard.pbix)↗️ - Explore the dashboard._

**📁 File Location:** `./PBIX_File/Customer_Churn_Dashboard.pbix`


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
## 💡 Key Insights

|Segment	|Observation|	Recommendation|
|--|--|--|
|📊 Contract Type	|Month-to-month users have the highest churn (42.7%)|	Promote annual plans with bundled discounts|
|🌐 Internet Service	|Fiber optic customers show 41.9% churn|	Improve service quality and connection reliability|
|💳 Payment Method	|Electronic check users show 45% churn	|Encourage auto-pay via credit card or bank transfer|
|🕒 Tenure	|0–6 month customers churn 54.7%	|Improve onboarding and early engagement|
|💰 Monthly Charges	|Higher-paying customers have moderate churn	|Offer loyalty benefits and premium support|

---

## 🤖 Churn Prediction Model — Project Report

**Goal:** Build a machine learning classification model to predict individual customer churn probability and assign each customer a risk segment, enabling the business to prioritise proactive retention efforts.

**Dataset:** Cleaned Telco Churn Dataset — 7,032 rows × 20 features  
**Target Variable:** `Churn` (binary: Yes / No)  
**Tools & Libraries:** Python, Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Seaborn

**📁 Notebook Location:** [`./Notebooks/03_churn_model.ipynb`](./Notebooks/03_churn_model.ipynb)

**📁 Output File:** [`./Datasets/churn_model_scores.csv`](./Datasets/churn_model_scores.csv)

---

### 📋 Table of Contents

1. [Feature Engineering](#feature-engineering)
2. [Model Training — Baseline Comparison](#model-training--baseline-comparison)
3. [Hyperparameter Tuning](#hyperparameter-tuning)
4. [Final Results](#final-results)
5. [Churn Risk Segmentation](#churn-risk-segmentation)
6. [Key Learnings](#key-learnings)

---

### 🔧 Feature Engineering

#### Dataset Overview

The cleaned dataset contained 7,032 customer records (11 rows dropped during cleaning) with the following feature types used for modelling:

| Type | Features |
|---|---|
| Numerical | `tenure`, `MonthlyCharges`, `TotalCharges` |
| Binary categorical | `gender`, `Partner`, `Dependents`, `PhoneService`, `PaperlessBilling`, `SeniorCitizen` |
| Multi-class categorical | `MultipleLines`, `InternetService`, `OnlineSecurity`, `OnlineBackup`, `DeviceProtection`, `TechSupport`, `StreamingTV`, `StreamingMovies`, `Contract`, `PaymentMethod` |

**Target:** `Churn` — encoded as `1` (churned) and `0` (retained)

---

#### Step 1 — Handling Class Imbalance

The dataset had a significant class imbalance — approximately **73.5% retained** and **26.5% churned** customers. Training a model directly on imbalanced data would bias predictions toward the majority (non-churn) class, leading to poor recall for churned customers who are the most actionable group.

To address this, the `class_weight='balanced'` parameter was applied during model training, which automatically adjusts the loss function to penalise misclassification of the minority (churn) class more heavily — without requiring synthetic data generation.

---

#### Step 2 — Encoding Categorical Features

All categorical columns were encoded before modelling:

| Type | Features | Transformation |
|---|---|---|
| Binary Yes/No columns | `Partner`, `Dependents`, `PhoneService`, `PaperlessBilling`, `Churn` | Label Encoding (0 / 1) |
| Multi-category columns | `InternetService`, `Contract`, `PaymentMethod`, `MultipleLines`, service add-ons | OneHotEncoder (drop='first') |
| `SeniorCitizen` | Already binary integer | No transformation needed |
| `gender` | Male / Female | Label Encoding |

The `customerID` column was set aside as an identifier and excluded from training features.

---

#### Step 3 — Feature Scaling

Numerical features (`tenure`, `MonthlyCharges`, `TotalCharges`) were standardised using **StandardScaler** to ensure distance-based and gradient-based models are not dominated by features with wide value ranges.

| Feature | Approx. Range |
|---|---|
| `tenure` | 1 – 72 months |
| `MonthlyCharges` | ~18 – 118 |
| `TotalCharges` | ~18 – 8,684 |

---

#### Step 4 — Preprocessing Pipeline

All transformations were chained into a single `ColumnTransformer` for clean, reproducible preprocessing:

```
ColumnTransformer
├── StandardScaler      →  tenure, MonthlyCharges, TotalCharges
├── OneHotEncoder       →  InternetService, Contract, PaymentMethod, MultipleLines, add-ons
└── Label Encoding      →  gender, Partner, Dependents, PhoneService, PaperlessBilling, Churn
```

The final preprocessed feature matrix was ready for model training with all features on a consistent scale.

---

### 🤖 Model Training — Baseline Comparison

The data was split **80% training / 20% testing** (random_state=42), yielding:
- Training set: ~5,625 samples
- Test set: ~1,407 samples

Six classification algorithms were trained on default (untuned) settings and evaluated using four metrics:

| Metric | What it measures |
|---|---|
| **Accuracy** | Proportion of correct predictions overall |
| **Precision** | Of predicted churners, how many actually churned (lower false alarm rate) |
| **Recall** | Of actual churners, how many were correctly identified (critical for retention) |
| **ROC-AUC** | Overall discriminative ability across all thresholds (higher = better, max 1.0) |

> **Note:** For churn prediction, **Recall** is the most operationally important metric — failing to flag a churner is costlier than a false alarm.

### Baseline Results

| Model | Accuracy | Precision | Recall | ROC-AUC | Notes |
|---|---|---|---|---|---|
| Logistic Regression | 0.803 | 0.648 | 0.574 | 0.845 | Solid baseline, linear boundary |
| Decision Tree | 0.728 | 0.494 | 0.511 | 0.673 | Overfits — poor generalisation |
| **Random Forest** | 0.796 | 0.643 | 0.497 | 0.832 | Good accuracy, low recall |
| **Gradient Boosting** | 0.809 | 0.660 | 0.581 | 0.853 | Best baseline overall |
| XGBoost | 0.803 | 0.645 | 0.565 | 0.847 | Strong candidate |
| K-Nearest Neighbors | 0.762 | 0.547 | 0.490 | 0.762 | Competitive but limited |

### Key Observations

- **Gradient Boosting** achieved the best ROC-AUC (0.853) and recall (0.581) at baseline — a clear frontrunner.
- **Logistic Regression** performed surprisingly well for a linear model, confirming that some churn signals are linearly separable (e.g. contract type, tenure).
- **Decision Tree** overfits with unstable splits on this noisy dataset, producing the lowest AUC (0.673).
- **KNN** suffers from high dimensionality after one-hot encoding, which dilutes distance-based discrimination.
- **Top 3 candidates** for tuning based on ROC-AUC and Recall: **Gradient Boosting (0.853)**, **XGBoost (0.847)**, and **Logistic Regression (0.845)**.

---

### ⚙️ Hyperparameter Tuning

The top models were tuned using **RandomizedSearchCV** (5-fold cross-validation, 50 iterations) to find the best balance between recall and generalisation.

**Search Spaces:**

| Model | Parameters Searched |
|---|---|
| Gradient Boosting | `n_estimators`, `learning_rate`, `max_depth`, `min_samples_split`, `min_samples_leaf`, `subsample` |
| XGBoost | `n_estimators`, `learning_rate`, `max_depth`, `min_child_weight`, `gamma`, `subsample`, `colsample_bytree` |
| Logistic Regression | `C`, `penalty`, `solver` |

**Best Parameters Found:**

| Model | Best Parameters |
|---|---|
| Gradient Boosting | n_estimators=300, lr=0.05, max_depth=4, min_samples_split=10, min_samples_leaf=4, subsample=0.8 |
| XGBoost | n_estimators=200, lr=0.1, max_depth=4, min_child_weight=3, gamma=0.1, subsample=0.8, colsample_bytree=0.8 |
| Logistic Regression | C=0.1, penalty='l2', solver='lbfgs' |

**Results After Tuning:**

| Model | Accuracy | Precision | Recall | ROC-AUC | Δ AUC vs Baseline |
|---|---|---|---|---|---|
| Logistic Regression | 0.806 | 0.656 | 0.579 | 0.848 | +0.003 |
| XGBoost | 0.812 | 0.668 | 0.592 | 0.857 | +0.010 ✅ |
| **Gradient Boosting** | **0.817** | **0.675** | **0.611** | **0.864** | **+0.011** ✅ |

---

### 🏆 Final Results

#### Top 3 Models — Head to Head

| Model | ROC-AUC | Recall | Accuracy | Precision |
|---|---|---|---|---|
| **Gradient Boosting** | **0.864** | **0.611** | **0.817** | **0.675** |
| XGBoost | 0.857 | 0.592 | 0.812 | 0.668 |
| Logistic Regression | 0.848 | 0.579 | 0.806 | 0.656 |

#### Winner: Gradient Boosting Classifier 🥇

**Final Configuration:**
```
GradientBoostingClassifier(
    n_estimators     = 300,
    learning_rate    = 0.05,
    max_depth        = 4,
    min_samples_split = 10,
    min_samples_leaf  = 4,
    subsample        = 0.8
)
```

**Final Test Performance:**
- **ROC-AUC: 0.864** — strong discriminative ability across all decision thresholds
- **Recall: 0.611** — correctly identifies ~61% of all churners
- **Accuracy: 81.7%** — correct predictions on 4 out of 5 customers
- **Precision: 0.675** — when predicting churn, correct ~68% of the time

**Why Gradient Boosting?**
- Achieves the highest ROC-AUC and recall across all evaluated models — the two metrics that matter most for a churn retention use case
- Builds trees sequentially, each correcting the residual errors of the previous — well-suited to the mixed feature types and non-linear interactions in this dataset
- `subsample` and `min_samples_leaf` parameters naturally control overfitting without requiring external regularisation
- Outputs calibrated probability scores (`churn_proba`) that are directly used for risk segmentation — making it the most operationally deployable model

---

### 🎯 Churn Risk Segmentation

Using the final Gradient Boosting model's predicted churn probabilities, each customer was assigned to one of five risk tiers:

| Risk Segment | Probability Range | Business Action |
|---|---|---|
| 🔴 **Very High** | ≥ 0.70 | Immediate intervention — priority retention offers |
| 🟠 **High** | 0.50 – 0.69 | Proactive outreach — contract upgrade incentives |
| 🟡 **Moderate** | 0.35 – 0.49 | Monitoring — soft engagement campaigns |
| 🟢 **Low** | 0.20 – 0.34 | Routine engagement — loyalty rewards |
| ⚪ **Very Low** | < 0.20 | Low priority — standard communications |

The full scored dataset (7,032 customers with `churn_proba` and `churn_risk_segment`) was exported to:

**📁 File Location:** [`./Datasets/churn_model_scores.csv`](./Datasets/churn_model_scores.csv)

This file can be loaded directly into Power BI to overlay model-predicted churn risk on top of the existing analytical dashboard, enabling the business to move from retrospective analysis to proactive, data-driven customer retention.

---

### 💡 Key Learnings

**1. Class imbalance must be addressed early.**  
With only 26.5% churners in the dataset, ignoring imbalance would produce a model that predicts "No Churn" for most customers and still achieves 73% accuracy — while missing almost all actual churners. Using `class_weight='balanced'` directly addresses this without distorting the data.

**2. Recall beats accuracy for churn prediction.**  
A model that flags 61% of churners with 82% accuracy is far more valuable than a model with 85% accuracy that only catches 40% of churners. The cost of a missed churner (lost revenue, lost relationship) far outweighs the cost of a false alarm (a retention offer sent unnecessarily).

**3. Gradient Boosting handles mixed feature types naturally.**  
Unlike linear models, Gradient Boosting doesn't require manual interaction terms to capture relationships like "Month-to-month contract AND Fiber Optic AND Electronic Check = very high churn risk." It learns these compound patterns directly from data.

**4. Probability scores are more useful than binary predictions.**  
Rather than just predicting "Will Churn / Won't Churn," outputting `churn_proba` enables tiered risk segmentation — so the business can prioritise its most at-risk customers rather than treating all predicted churners equally.

**5. The model complements the dashboard, not replaces it.**  
EDA and Power BI identified *what kinds of customers* churn. The model identifies *which specific customers* are at risk. Together, they form a complete picture: segment-level strategy informed by analytics, individual-level targeting enabled by machine learning.

---

## 🧰 Tools & Technologies

|Tool|Purpose|
|----|-------|
|**🐍 Python (Pandas, Seaborn, Matplotlib)**|Data cleaning and exploratory analysis|
|**🤖 Python (Scikit-learn, XGBoost)**|Machine learning model training and evaluation|
|**🧮 SQL (MySQL / DuckDB)**|Querying and validation|
|🧠 **Power BI**|Dashboard visualization|
|🧮 **DAX**|Calculations and insights|
|🧹 **Excel/CSV**|Data preprocessing|
|📊 **Power Query**|Cleaning & transformation|
|**💻 GitHub**|Version control and portfolio hosting|

---
## 📁 Repository Structure
|Folder|	Description|
|--|--|
|`/Datasets/`|	Raw, cleaned datasets, and model churn scores|
|`/SQL/`|	SQL queries for data segmentation|
|`/Notebooks/`|	Python notebooks for EDA and model training|
|`/PBIX_File/`|	Power BI file (Customer_Churn.pbix)|
|`/Dashboard_Screenshots/`|	Power BI dashboard visuals|
|`/Screenshots/`|	EDA plots and data preview images|
|`/Docs/`|	Supporting documentation|
|`requirements.txt`|	Python dependencies|

---

## 🚀 Results & Impact

- ✅ Identified high-risk churn segments (Month-to-Month, Fiber Optic, Electronic Check users).
- ✅ Developed targeted retention strategies for each customer group.
- ✅ Created interactive tooltip-based Power BI dashboard to drill down into specific behaviors.
- ✅ Presented data storytelling insights for business decision-making.
- ✅ Built a Gradient Boosting classification model achieving **ROC-AUC of 0.864** and **61% churn recall**.
- ✅ Generated individual-level churn probability scores and risk segments for all 7,032 customers.
- ✅ Exported scored dataset ready for Power BI integration to enable proactive, targeted retention campaigns.

---

## 📎 Quick Links

[`EDA Notebook`↗️](./Notebooks/02_data_eda.ipynb)

[`Churn Model Notebook`↗️](./Notebooks/03_churn_model.ipynb)

[`Power BI Dashboard`↗️](./PBIX_File/Customer_Churn_Dashboard.pbix)

[`Project Documentation`↗️](./Docs/Customer_Churn_Analysis_Documentation.pdf)

[`Dashboard Screenshots`↗️](./Dashboard_Screenshots/)

[`Raw Dataset (CSV File)`↗️](./Datasets/telco_dataset_raw.csv)

[`Python Dependencies File`↗️](./requirements.txt)

[`Cleaned Dataset (CSV File)`↗️](./Datasets/telco_dataset_cleaned.csv)

[`Churn Model Scores (CSV File)`↗️](./Datasets/churn_model_scores.csv)

[`Python Visualizations Screenshots`↗️](./Screenshots/)

[`Data cleaning and exploration file`↗️](./Notebooks/01_data_overview.ipynb)

[`Business Insights & Recommendations`↗️](./Docs/insights.md)

[`Telco Customer Churn Dataset – Kaggle (Download dataset)`↗️](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

---

## 👤 Connect with me

**Harshvardhan Rajgarhia**<br>

[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:harsvardhanrajgarhia@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/harshvardhan-rajgarhia-ba62982a4)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Harsh1574/data-analytics-portfolio)



---
