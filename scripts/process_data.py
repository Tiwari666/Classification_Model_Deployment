import pandas as pd
from sklearn.model_selection import train_test_split

# Load your dataset
df = pd.read_csv('../data/Restaurant_Reviews.csv')

# Ensure the dataset is loaded correctly
print(df.head())

# Print the first few rows and column names to verify the structure
print("First few rows of the DataFrame:")
print(df.head())
print("\nColumn names in the DataFrame:")
print(df.columns)

# Continue with your data processing
X = df['Review']  # Correct column name
y = df['Liked']   # Correct column name

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save the processed data if necessary
X_train.to_csv('../data/X_train.csv', index=False)
y_train.to_csv('../data/y_train.csv', index=False)
X_test.to_csv('../data/X_test.csv', index=False)
y_test.to_csv('../data/y_test.csv', index=False)

# Print the shapes of the training and testing sets
print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"y_test shape: {y_test.shape}")
