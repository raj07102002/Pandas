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

# Q.4 

# import pandas as pd
# df = pd.DataFrame({
#     'Name': ['Raj', 'Neha', 'Amit', 'Simran', 'John', 'Sara'],
#     'Marks': [80, 90, 85, 70, 75, 95]
# })
# df.head()

# Q.5 

# import pandas as pd

# df = pd.DataFrame({
#     'Marks': [70, 80, 90, 85, 75, 95],
#     'Attendance': [88, 92, 85, 90, 95, 87]
# })

# df.describe()

# Q.6

# import pandas as pd

# data = {'Name': ['Alice', 'Bob', 'Charlie'],
#         'Age': [25, 30, 22]}

# df = pd.DataFrame(data)

# # Sort by Age (ascending)
# sorted_df = df.sort_values(by='Age')
# print(sorted_df)

# Q.7

# import pandas as pd

# data = {
#     'Name': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'David']
# }

# df = pd.DataFrame(data)

# print(df['Name'].nunique())

# Q.8 

# import pandas as pd

# data = {
#     'deaths': [5, 8, 12, 6, 9]
# }

# df = pd.DataFrame(data)

# print(df['deaths'].iloc[2]) 

# Q.9 

# import pandas as pd

# b = pd.DataFrame({
#     'item': ['Apple', 'Banana', 'Cherry'],
#     'quantity': [5, 2, 8]
# })

# c = b.sort_values("quantity")
# print(c)

# Q.10 

# import pandas as pd

# df = pd.DataFrame({
#     'Marks': [80, 90, 75]
# })

# # Add 5 bonus marks using lambda
# df['Bonus'] = df['Marks'].apply(lambda x: x + 5)

# print(df) 

# Q.11 

# import pandas as pd
# df = pd.read_csv('customers.csv')
# print("Original Data:")
# print(df.head)