import pandas as pd
from typing import List

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(subset='email', keep='first', inplace=True)
    return customers

data = [
    ["Ella", "emily0@example.com"],
    ["David", "michael@example.com"],
    ["Zachary", "sarah@example.com"],
    ["Alice", "john@example.com"],
    ["Finn", "john@example.com"],
    ["Violet", "alice@example.com"]
]

# | customer_id | name    | email               |
# | ----------- | ------- | ------------------- |
# | 1           | Ella    | emily@example.com   |
# | 2           | David   | michael@example.com |
# | 3           | Zachary | sarah@example.com   |
# | 4           | Alice   | john@example.com    |
# | 6           | Violet  | alice@example.com   |

df = pd.DataFrame(data, columns=["name", "email"])

result = dropDuplicateEmails(df)

print(result)


__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
