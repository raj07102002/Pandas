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