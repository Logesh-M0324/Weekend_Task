import pandas as pd

# pd.set_option("display.max_rows", None)
# pd.set_option("display.max_column", None)

# data = pd.read_csv("dataset/raw/olist_orders_dataset.csv")

# print("===========================Head==================================")

# print(data.head())

# print("===========================Sample================================")

# print(data.sample(5))

# print("===========================Tail==================================")

# print(data.tail())

# print("===========================Info=================================")

# print(data.info())

# print("===========================Describe=================================")

# print(data.describe())

# print("===========================Type=================================")

# print(type(data))

# print("===========================size================================")

# print(f"the total rows in the dataset is {data.shape[0]} \n the total column in the dataset is {data.shape[1]}")

# print(data.isnull().sum())

# print("===================================unique Values===============================")

# print(data["order_status"].value_counts())

# print("========================================checking=========================================")

# numerical = data.select_dtypes(include=["number"]).columns.tolist()
# categorical = data.select_dtypes(include=["object"]).columns.tolist()
# datetime = data.select_dtypes(include=["datetime"]).columns.tolist()

# print("======================Numerical=================================")
# print(numerical)
# print("======================categorical=================================")
# print(categorical)
# print("======================DateTime=================================")
# print(datetime)

# print("==================print missing values========================================")
# missing = data.isnull().sum()
# print(missing)

# missing = missing[missing > 0]
# print(missing)

# print("======================================Learning=========================================")

# print(data.columns)

# print("+++++++++++++++++++++++++++++++++++")

# missing_1 = data.isnull().sum().sum()
# print(missing_1)

data = pd.read_csv("./exports/master_dataset.csv")
print(data.head())

data_1 = pd.read_csv("./exports/final_clean_dataset.csv")
print(data.head())