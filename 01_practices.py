# Q1

# import pandas as pd
# data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
# df = pd.DataFrame(data)
# (df)

# Q.2 

# import pandas as pd

# s = pd.Series([10, 20, None, 30])
# print(s.count())
# df = pd.DataFrame({
#     'A': [1, 2, None],
#     'B': [4, None, 6]
# })
# print(df.count())

# Q.3
# import pandas as pd

# data = pd.DataFrame({
#     'Student': ['Raj', 'Simran', 'Amit', 'Neha', 'Ali'],
#     'Class': [10, 10, 9, 9, 10],
#     'Marks': [80, 70, 90, 85, 60]
# })

# result = data.groupby('Class')['Marks'].sum()
# print(result)