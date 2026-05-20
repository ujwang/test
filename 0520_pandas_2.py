import pandas as pd

# -------------------------
# 使用字典建立 DataFrame
# -------------------------
data_dict = {
    "Product": ["Apple", "Banana", "Orange", "Mango", "Grape", "Guava"],
    "Price": [30, 20, 25, 60, 45, 35],
    "Sales": [100, 150, 80, 60, 90, 54]
}

df1 = pd.DataFrame(data_dict)

# -------------------------
# 使用列表（子列表）建立 DataFrame
# -------------------------
data_list = [
    ["Apple", 30, 100],
    ["Banana", 20, 150],
    ["Orange", 25, 80],
    ["Mango", 60, 60],
    ["Grape", 45, 90],
    ["Guava", 35, 54]
]

df2 = pd.DataFrame(data_list, columns=["Product", "Price", "Sales"])

# 顯示前5筆資料
print(df1.head())

# 顯示後5筆資料
print(df1.tail())

# 顯示列數與欄數
print(df1.shape)

# 顯示欄位名稱
print(df1.columns)

# 顯示資料型態
print(df1.dtypes)

# 顯示非空值數量
print(df1.count())

# 計算統計資訊（取到小數後2位）
stats = df1.describe().round(2)

print(stats)

# 存成 CSV 檔
stats.to_csv("0520_stock2.csv")

print("\n已存成 0520_stock2.csv")