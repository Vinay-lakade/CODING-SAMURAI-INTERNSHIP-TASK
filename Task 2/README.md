# 📊 TV Advertisement Spend vs Sales Prediction - Linear Regression Project

This project demonstrates a simple **Linear Regression** model using **Python** and **scikit-learn** to predict product sales based on TV advertisement spending.

## 🎯 Objective

To understand how TV advertisement budgets affect product sales, and build a simple linear regression model to predict future sales using past data.

## 📁 Dataset

A small sample dataset was manually created with two columns:
- **TV**: TV advertisement spending (in $1000s)
- **Sales**: Product sales (in $1000s)

```python
data = {
    'TV': [230.1, 44.5, 17.2, 151.5, 180.8, 8.7, 57.5, 120.2],
    'Sales': [22.1, 10.4, 9.3, 18.5, 12.9, 7.2, 11.8, 13.2]
}

⚙️ Technologies Used
Python 🐍
Pandas
Matplotlib
Scikit-learn (LinearRegression, train_test_split, metrics)

📌 Steps Performed
Imported required libraries.
Created and loaded the dataset.
Split the data into training and testing sets.
Trained a Linear Regression model.
Evaluated the model using Mean Squared Error (MSE) and R² Score.
Visualized the regression line over actual data.

📈 Model Evaluation
bash
Copy
Edit
Mean Squared Error: X.XX
R² Score: X.XX(Replace with your actual output)

📉 Visualization
The graph below shows the actual data points (blue) and the regression line (red):

📌 Graph will be shown when the script is executed using matplotlib.

🚀 How to Run
bash
Copy
Edit
pip install pandas scikit-learn matplotlib
python linear_regression_tv_sales.py

✅ Output
Predicted sales based on test data
Graph showing TV ad spend vs Sales with a regression line
Evaluation metrics (MSE and R²)
