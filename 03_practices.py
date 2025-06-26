# Q.1
# import pandas as pd
# df = pd.DataFrame({
#     'OrderID': [101, 102, 103],
#     'Product': ['Keyboard', 'Mouse', 'Laptop'],
#     'Quantity': [2, 1, 1]
# })

# # Get the Quantity column
# print(df['Quantity']) 

# Q.2 

# import pandas as pd

# df = pd.DataFrame({
#     'Name': ['Raj', 'Ali', 'Sara', 'Maya', 'Tom'],
#     'Occupation': ['Doctor', 'Engineer', 'Doctor', 'Teacher', 'Engineer']
# })

# print(df['Occupation'].nunique())       
# print(df['Occupation'].unique()) 

# Q.3 

# import pandas as pd

# df = pd.DataFrame({
#     'Score': [10, 20, 10, 30, 20, 40]
# })

# unique_ints = df['Score'].dropna().unique()
# print("Unique integer values:", unique_ints)
# print("Count:", len(unique_ints)) 

# Q.4 

# import pandas as pd

# df = pd.DataFrame({
#     'Name': ['Raj', 'Ali', 'Sara', 'Maya', 'Tom'],
#     'Occupation': ['Doctor', 'Engineer', 'Doctor', 'Teacher', 'Engineer']
# })

# print(df['Occupation'].nunique())       # Output: 3
# print(df['Occupation'].unique()) 

# Q.5 

# import pandas as pd

# # Create columns with data
# df = pd.DataFrame({
#     'Name': ['Raj', 'Ali', 'Sara'],
#     'Age': [22, 24, 23],
#     'City': ['Delhi', 'Mumbai', 'Chennai'] 

# })
# df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
# print(df)

