import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Vehicle Type': ['Car', 'Truck', 'Car', 'Bike', 'Truck', 'Car', 'Bike'],
    'Kilometre': [15000, 30000, 25000, 10000, 40000, 5000, 2000],
    'Type': ['Sedan', 'Pickup', 'Hatchback', 'Sport', 'Pickup', 'SUV', 'Sport'],
    'Price': [20000, 25000, 15000, 10000, 30000, 22000, 12000],
    'Year of Reg': [2020, 2019, 2021, 2020, 2018, 2021, 2019]
}

df = pd.DataFrame(data)

kilometre_data = df.groupby('Vehicle Type')['Kilometre'].sum()

plt.figure(figsize=(10, 5))
kilometre_data.plot(kind='bar', color='skyblue')
plt.title('Total Kilometres by Vehicle Type')
plt.xlabel('Vehicle Type')
plt.ylabel('Total Kilometre')
plt.xticks(rotation=45)
plt.tight_layout() 
plt.show()

price_data = df.groupby('Type')['Price'].mean()

plt.figure(figsize=(10, 5))
price_data.plot(kind='bar', color='lightgreen')
plt.title('Average Price by Vehicle Type')
plt.xlabel('Type')
plt.ylabel('Average Price')
plt.xticks(rotation=45)
plt.tight_layout()  
plt.show()

year_price_data = df.groupby('Year of Reg')['Price'].mean()

plt.figure(figsize=(8, 8))
plt.pie(year_price_data, labels=year_price_data.index, autopct='%1.1f%%', startangle=140)
plt.title('Average Price Distribution by Year of Registration')
plt.axis('equal') 
plt.show()