import numpy as np
import pandas as pd

# my_data = np.array([[0, 3], [10, 7], [20, 9], [30, 14], [40, 15]])

# my_column_names = ["temperature", "activity"]
# my_dataframe = pd.DataFrame(data=my_data, columns=my_column_names)

# my_dataframe["adjusted"] = my_dataframe["activity"] + 2

# print(my_dataframe)

# print("Rows #0, #1 and #2:")
# print(my_dataframe.head(3), "\n")

# print("Row #2:")
# print(my_dataframe.iloc[[2]], "\n")

# print("Row 1-3:")
# print(my_dataframe[1:4], "\n")

# print("Column 'temperature':")
# print(my_dataframe['temperature'])

data = np.random.randint(size=(3,4), low=0, high=101)
columns = ["Eleanor", "Chidi", "Tahani", "Jason"]

df = pd.DataFrame(data, columns=columns)

df["Janet"] = df["Tahani"] + df["Jason"]

print(df)

print("First Eleanor")
print(df["Eleanor"][0])
