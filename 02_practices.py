# Q.1 

# import pandas as pd

# # Load the datasets (if not already loaded)
# cars1 = pd.read_csv('cars1.csv')
# cars2 = pd.read_csv('cars2.csv')

# # Combine both datasets into one
# cars = pd.concat([cars1, cars2], ignore_index=True)

# print(cars.shape)    # Shows total rows and columns
# print(cars.head())   # See the first 5 rows
# print(cars.tail())   # See the last 5 rows

# Q.2 
# import pandas as pd

# df = pd.DataFrame({
#     'name': ['Raj', 'Neha', 'Amit', 'Ravi', 'Simran'],
#     'occupation': ['Doctor', 'Engineer', 'Doctor', 'Doctor', 'Engineer']
# })

# print(df['occupation'].value_counts().head(1)) 

# Q.3 

# import pandas as pd

# data = {
#     'Customer': ['Raj', 'Neha', 'Amit', 'Raj', 'Neha'],
#     'City': ['Delhi', 'Mumbai', 'Delhi', 'Delhi', 'Pune']
# }

# df = pd.DataFrame(data)
# print(df) 

# Q.4 
# # From a dictionary of lists (most common)
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [25, 30, 35, 28],
#     'City': ['New York', 'London', 'Paris', 'Tokyo']
# }
# df1 = pd.DataFrame(data)
# print("DataFrame from a dictionary of lists:\n", df1)
# print("-" * 30)

# # From a list of dictionaries
# data_list_of_dict = [
#     {'Name': 'Eve', 'Age': 22, 'City': 'Rome'},
#     {'Name': 'Frank', 'Age': 40, 'City': 'Berlin'},
#     {'Name': 'Grace', 'Age': 29, 'City': 'Sydney'}
# ]
# df2 = pd.DataFrame(data_list_of_dict)
# print("DataFrame from a list of dictionaries:\n", df2)
# print("-" * 30)

# # From a NumPy array (with custom columns and index)
# data_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# df3 = pd.DataFrame(data_array, columns=['ColA', 'ColB', 'ColC'], index=['Row1', 'Row2', 'Row3'])
# print("DataFrame from a NumPy array:\n", df3)
# print("-" * 30) 

# Q.5 

# import pandas as pd

# euro12 = pd.DataFrame({
#     'Team': ['Germany', 'Spain', 'Greece', 'Italy'],
#     'Goals': [10, 12, 5, 8]
# })

# result = euro12[euro12.Team.str.startswith('G')]
# print(result)