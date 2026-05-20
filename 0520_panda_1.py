import pandas as pd
import numpy as np

# 建立 stock1
stock1 = pd.Series([120, 80, None, 60, 95, None, 110])

# 建立 stock2（加入索引）
fruits = ["Apple", "Banana", "Orange", "Mango", "Grape", "Peach", "Melon"]
stock2 = pd.Series(stock1.values, index=fruits)

# 將 stock2 轉為字典 stock3
stock3 = stock2.to_dict()

# 輸出結果
print("stock1")
print(stock1)

print("\nstock2")
print(stock2)

print("\nstock3")
print(stock3)

# Banana 的庫存值
print("\nBanana 庫存：", stock2["Banana"])

# 缺失值檢查
print("\n缺失值檢查：")
print(stock2.isnull())

# 缺失值數量
print("\n缺失值數量：", stock2.isnull().sum())

# 存成 CSV 檔
stock2.to_csv("0520_stock.csv")
print("\n已存成 0520_stock.csv")