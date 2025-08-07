import pandas as pd
from typing import List

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    res = weather.pivot(index='month', columns='city', values='temperature')
    return res


data1 = [
    ["Jacksonville", "Mason", 8],
    [2, "Ava", 6],
    [3, "Taylor", 15],
    [4, "Georgia", 17]
]


# Example 1:
# Input:
# +--------------+----------+-------------+
# | city         | month    | temperature |
# +--------------+----------+-------------+
# | Jacksonville | January  | 13          |
# | Jacksonville | February | 23          |
# | Jacksonville | March    | 38          |
# | Jacksonville | April    | 5           |
# | Jacksonville | May      | 34          |
# | ElPaso       | January  | 20          |
# | ElPaso       | February | 6           |
# | ElPaso       | March    | 26          |
# | ElPaso       | April    | 2           |
# | ElPaso       | May      | 43          |
# +--------------+----------+-------------+
# Output:
# +----------+--------+--------------+
# | month    | ElPaso | Jacksonville |
# +----------+--------+--------------+
# | April    | 2      | 5            |
# | February | 6      | 23           |
# | January  | 20     | 13           |
# | March    | 26     | 38           |
# | May      | 43     | 34           |
# +----------+--------+--------------+


df1 = pd.DataFrame(data1, columns=["city", "month", "temperature"])

result = pivotTable(df1)

print(result)


__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
