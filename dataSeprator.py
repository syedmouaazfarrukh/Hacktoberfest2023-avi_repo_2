import pandas as pd

# Create a sample DataFrame
data = {'Category': ['A', 'B', 'A', 'C', 'B', 'C'],
        'Value': [10, 20, 15, 30, 25, 40]}

df = pd.DataFrame(data)

# Group the data by the 'Category' column
grouped = df.groupby('Category')

# Iterate through groups and perform actions
for group_name, group_data in grouped:
    print(f"Group: {group_name}")
    print(group_data)
