import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("sharks-reference-23:24.csv")

# Filter the DataFrame to keep only the rows where 'Home' column is 'San Jose Sharks'
filtered_df = df[df['Home'] == 'San Jose Sharks']

# Save the filtered data to a new CSV file
filtered_df.to_csv("filtered_sharks23-24.csv", index=False)