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

# Show column names
print("\nShape:")
print(df.shape)

print(df.describe())
print("Max:\n", df.max())