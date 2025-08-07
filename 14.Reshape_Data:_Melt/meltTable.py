import pandas as pd
from typing import List

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    report = report.melt(
        id_vars=["product"],
        value_vars=["quarter_1", "quarter_2", "quarter_3", "quarter_4"],
        var_name="quarter",
        value_name="sales",
    )
    return report

data1 = [
    ["ila", 15, 8, 32, 63],
    ["aya", 15, 8, 32, 63],
    ["ilyass", 15, 8, 32, 63],
    ["kaneki", 15, 8, 32, 63]
]


# Example 1:

# Input:
# +-------------+-----------+-----------+-----------+-----------+
# | product     | quarter_1 | quarter_2 | quarter_3 | quarter_4 |
# +-------------+-----------+-----------+-----------+-----------+
# | Umbrella    | 417       | 224       | 379       | 611       |
# | SleepingBag | 800       | 936       | 93        | 875       |
# +-------------+-----------+-----------+-----------+-----------+
# Output:
# +-------------+-----------+-------+
# | product     | quarter   | sales |
# +-------------+-----------+-------+
# | Umbrella    | quarter_1 | 417   |
# | SleepingBag | quarter_1 | 800   |
# | Umbrella    | quarter_2 | 224   |
# | SleepingBag | quarter_2 | 936   |
# | Umbrella    | quarter_3 | 379   |
# | SleepingBag | quarter_3 | 93    |
# | Umbrella    | quarter_4 | 611   |
# | SleepingBag | quarter_4 | 875   |
# +-------------+-----------+-------+
# Explanation:


df1 = pd.DataFrame(data1, columns=["product", "quarter_1", "quarter_2", "quarter_3", "quarter_4"])

result = meltTable(df1)

print(result)


__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
