import pandas as pd

# Load the TSV file
df = pd.read_csv('../data/Restaurant_Reviews.tsv', delimiter='\t')

# Save the data as a CSV file
df.to_csv('../data/Restaurant_Reviews.csv', index=False)

print('TSV file converted to CSV file')


