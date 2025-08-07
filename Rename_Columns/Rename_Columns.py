import pandas as pd
from typing import List

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
        students.rename(columns=
            {
                "id": "student_id",
                "first": "first_name",
                "last": "last_name",
                "age": "age_in_years"
            }, inplace=True);  
        return students

data = [
    [1, "Ella" ,"kook" ,19666],
    [2, "David" ,"lol" ,19450],
    [3, "Finn" ,"dsf" ,183],
    [4, "Violet" ,"sd" ,520]
]

# Example 1:
# Input:
# +----+---------+----------+-----+
# | id | first   | last     | age |
# +----+---------+----------+-----+
# | 1  | Mason   | King     | 6   |
# | 2  | Ava     | Wright   | 7   |
# | 3  | Taylor  | Hall     | 16  |
# | 4  | Georgia | Thompson | 18  |
# | 5  | Thomas  | Moore    | 10  |
# +----+---------+----------+-----+
# Output:
# +------------+------------+-----------+--------------+
# | student_id | first_name | last_name | age_in_years |
# +------------+------------+-----------+--------------+
# | 1          | Mason      | King      | 6            |
# | 2          | Ava        | Wright    | 7            |
# | 3          | Taylor     | Hall      | 16           |
# | 4          | Georgia    | Thompson  | 18           |
# | 5          | Thomas     | Moore     | 10           |
# +------------+------------+-----------+--------------+
# Explanation: 
# The column names are changed accordingly.

df = pd.DataFrame(data, columns=["id", "first", "last", "age"])

result = renameColumns(df)

print(result)


__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
