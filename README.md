🍔 Food Delivery Sales & Customer Insights
<p align="center">
  <img src="https://raw.githubusercontent.com/hariruthranhub/food-delivery-sales-analysis/main/06_business_dashboard.png" alt="Food Delivery Business Insights Dashboard" width="820">
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-11557C" alt="Matplotlib">
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen" alt="Status">
</p>
An exploratory data analysis (EDA) project on food delivery order data, built using Python (Pandas, NumPy, Matplotlib) as part of the Naan Mudhalvan Arts Internship Program 2026 — Python for Data Analytics.
📌 Overview
A food delivery business wants to better understand how, when, and what its customers order — so it can plan staffing, promote the right dishes, and allocate delivery partners more efficiently across zones.
This project analyzes a sample order log of 650+ orders across a 90-day window and 8 delivery zones to answer five practical business questions:
#	Business Question
1	When do customers order the most? (peak hours)
2	What are the most popular dishes?
3	Which delivery areas generate the most orders?
4	Which food categories drive the most revenue?
5	How do customers prefer to pay?
🛠️ Tools & Libraries
Library	Used For
Pandas	Loading, cleaning, and aggregating order data
NumPy	Numerical operations & synthetic dataset generation
Matplotlib	Bar charts, pie chart, and the combined dashboard
📂 Repository Structure
```
├── Food_Delivery_Sales_Analysis.ipynb   # Main analysis notebook (cleaning + EDA + visuals)
├── food_delivery_orders.csv             # Raw order data (missing values & duplicates)
├── food_delivery_orders_cleaned.csv     # Cleaned dataset used for analysis
├── generate_dataset.py                  # Script used to generate the sample dataset
├── 01_peak_order_hours.png              # Chart: orders by hour
├── 02_top_10_dishes.png                 # Chart: best-selling dishes
├── 03_orders_by_area.png                # Chart: orders by delivery zone
├── 04_revenue_by_category.png           # Chart: revenue by food category
├── 05_payment_methods.png               # Chart: payment method split
├── 06_business_dashboard.png            # Combined 4-in-1 dashboard
└── requirements.txt                     # Python dependencies
```
📊 Key Insights
🕐 Orders peak at lunch (12–1 PM) and dinner (7–9 PM) — a classic bimodal food-delivery demand curve.
🍗 Chicken Biryani is the best-selling dish, and Biryani as a category drives the single largest share of revenue.
📍 Order volume is fairly even across zones, with Anna Nagar and Adyar slightly ahead of the rest.
💳 UPI is the most-used payment method (43%), ahead of Cash on Delivery, Card, and Wallet.
⏱️ Average delivery time is ~36 minutes, with an average customer rating of ~4.4 / 5.
<p align="center">
  <img src="https://raw.githubusercontent.com/hariruthranhub/food-delivery-sales-analysis/main/05_payment_methods.png" alt="Orders by Payment Method" width="420">
</p>
▶️ How to Run
Clone or download this repository.
Install dependencies:
```bash
   pip install -r requirements.txt
   ```
Open `Food_Delivery_Sales_Analysis.ipynb` in Jupyter Notebook or Google Colab.
Run all cells from top to bottom.
🚀 Future Scope
Forecast daily/weekly order volume using time-series methods.
Build an interactive dashboard (Streamlit or Power BI) on top of the cleaned dataset.
Segment customers by order frequency and spend (RFM analysis) for targeted offers.
👤 Author
Hariharan Ruthran V
Naan Mudhalvan Arts Internship Program 2026 — Python for Data Analytics
