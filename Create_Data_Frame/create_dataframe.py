import pandas as pd
from typing import List

df = pd.DataFrame(
    {
        "Name" : [
            'hih1',
            'hih2',
            'hih3',
        ],
        "Age": [22, 33, 45],
        'Sex': ["mo", "mio", "kds"],
    }
)

# print the full dataForm
print("Full dataFrame:")
print(df)

# show column names
print("\nColumns:")
print(df.columns.tolist())

# Show shape (rows,  coluns)
print("\nShape:")
print(df.shape)

# Show first 2 rows
print("\nFirst 2 Rows:")
print(df.head(2))

# Show info about the DataFrame
print("\nInfo:")
print(df.info())

# Filter row where Age > 30
print("\nFiltered (age > 30):")
print(df[df["Age"] > 30])