import pandas as pd
import numpy as np
# Generate random data
np.random.seed(42)
data = {
    'value1': np.random.normal(100, 15, 100),
    'value2': np.random.normal(50, 10, 100),
    'value3': np.random.normal(200, 30, 100)
}
# Add some outliers
data['value1'][5] = 500
data['value2'][15] = -100
data['value3'][25] = 1000
df = pd.DataFrame(data)
# Save original dataset to CSV
df.to_csv('original_data.csv', index=False)
# Calculate Z-scores
mean = df.mean()
std_dev = df.std()
z_scores = (df - mean) / std_dev
# Filter rows where all Z-scores are below threshold (3)
threshold = 3
df_cleaned = df[(np.abs(z_scores) < threshold).all(axis=1)]
# Save cleaned dataset to CSV
df_cleaned.to_csv('cleaned_data.csv', index=False)
print(f"Original rows: {len(df)}")
print(f"Cleaned rows: {len(df_cleaned)}")
print(f"Outliers removed: {len(df) - len(df_cleaned)}")
print("\nOriginal data saved to 'original_data.csv'")
print("Cleaned data saved to 'cleaned_data.csv'")