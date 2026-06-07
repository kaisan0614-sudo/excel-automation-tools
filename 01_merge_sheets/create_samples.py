import pandas as pd

df1 = pd.DataFrame({
    "Name": ["Alice Wang", "Bob Lee", "Carol Chang"],
    "Department": ["Sales", "Engineering", "Admin"],
    "Salary": [45000, 60000, 38000]
})

df2 = pd.DataFrame({
    "Name": ["David Chen", "Eva Lin", "Frank Huang"],
    "Department": ["Marketing", "Engineering", "Sales"],
    "Salary": [50000, 65000, 42000]
})

df1.to_excel("sample_input/employees_A.xlsx", index=False)
df2.to_excel("sample_input/employees_B.xlsx", index=False)
print("Sample files created!")
