import pandas as pd

df1 = pd.DataFrame({
    "姓名": ["王小明", "李小華", "張美玲"],
    "部門": ["業務", "工程", "行政"],
    "薪資": [45000, 60000, 38000]
})

df2 = pd.DataFrame({
    "姓名": ["陳大偉", "林小燕", "黃志豪"],
    "部門": ["行銷", "工程", "業務"],
    "薪資": [50000, 65000, 42000]
})

df1.to_excel("sample_input/員工資料A.xlsx", index=False)
df2.to_excel("sample_input/員工資料B.xlsx", index=False)
print("測試檔案建立完成！")
