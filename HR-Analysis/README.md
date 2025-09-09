# 📊 Employee Attrition Analysis (Analytics Phase)

## 📌 Project Overview
This project analyzes employee attrition patterns using the IBM HR Analytics dataset.  
The goal is to uncover key factors driving attrition and provide actionable insights for HR teams.  

Attrition (employee turnover) refers to employees leaving the company.  
In this dataset, **~16% of employees left**, while **84% stayed**.

---

## ⚙️ Tools & Libraries
- **Python** → Pandas, Seaborn, Matplotlib
- **Jupyter Notebook** for analysis
- **Dataset** → IBM HR Attrition Dataset (Kaggle)

---

## 📊 Business Insights

1. **Overall Attrition**
   - ~16% employees left, 84% stayed.  
   - Attrition is significant but not extreme.

2. **Department-Wise Attrition**
   - Sales has the **highest attrition (~20%)**.  
   - HR is moderate (~14%), R&D slightly lower (~13%).

3. **Job Role-Wise Attrition**
   - Sales Representatives and Lab Technicians show the highest turnover.  
   - Managers/Directors are much more stable.

4. **Demographics**
   - Younger employees (<35 years) leave more often.  
   - Gender is not a strong driver.  
   - Married employees are slightly more stable.

5. **Compensation**
   - Employees with lower monthly income have higher attrition.  
   - Higher pay improves retention.

6. **Workload**
   - Employees working overtime are **3x more likely** to leave.  
   - Poor work-life balance is a strong attrition factor.

7. **Numeric Correlations**
   - Monthly Income ↔ Job Level (expected).  
   - Age ↔ Total Working Years (expected).  
   - No single numeric variable fully explains attrition.

---

## 📈 Key Visualizations
- Attrition Distribution (Yes/No)
- Attrition by Department
- Attrition by Job Role
- Attrition by Gender
- Attrition by Age
- Attrition vs Monthly Income (Boxplot)
- Attrition by Overtime
- Correlation Heatmap (numeric features)

📌 *Screenshots of these charts are included in the `Screenshots/` folder.*

---

## 📝 Business Recommendations
Based on the analytics:
- **Target retention programs** at Sales and entry-level employees.  
- **Improve compensation** for lower income groups.  
- **Reduce overtime** and promote better work-life balance.  
- **Focus on young employees** (<35 years) to improve early-career retention.

---

## ✅ Next Steps
This completes the **Analytics Phase** of the project.  
The next step will be to extend this analysis into **Machine Learning models** to predict attrition.

