import pandas as pd
import numpy as np

# Generate 10 random numbers
numbers = np.random.randint(1, 101, 10)

# Create a Pandas Series
series = pd.Series(numbers)

# Display the Series
print("Pandas Series:")
print(series)

# Display basic information
print("First number:", series.iloc[0])
print("Last number:", series.iloc[-1])
print("Number of values:", len(series))

# Simple operations
print("Sum:", series.sum())
print("Mean:", series.mean())