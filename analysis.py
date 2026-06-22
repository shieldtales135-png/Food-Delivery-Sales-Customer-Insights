import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('data/food_delivery_sales.csv')

print("Total Orders:",len(df))
print("Total Net Sales:",df['Net_Sales'].sum())
print("Average Rating:",round(df['Rating'].mean(),2))

city=df.groupby('City')['Net_Sales'].sum()
print(city)

city.plot(kind='bar',title='Sales by City')
plt.tight_layout()
plt.savefig('images/sales_by_city.png')
plt.close()

df['Payment_Method'].value_counts().plot(kind='pie',autopct='%1.1f%%')
plt.ylabel('')
plt.tight_layout()
plt.savefig('images/payment_method.png')
