import pandas as pd

file_path = 'cars_sampled.csv'
df = pd.read_csv(file_path)
num_attributes = df.shape[1]
attribute_names = df.columns.tolist()

print(f"Number of attributes: {num_attributes}")
print("Attribute names:")
for attribute in attribute_names:
    print(attribute)