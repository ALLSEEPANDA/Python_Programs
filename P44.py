import pandas as pd

file_path = 'cars_sampled.csv'
data = pd.read_csv(file_path)

print("Data from cars_sampled.csv:")
print(data.head())