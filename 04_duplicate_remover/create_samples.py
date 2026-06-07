import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice Wang", "Bob Lee", "Carol Chang", "Alice Wang", "David Chen", "Bob Lee", "Frank Huang", "Carol Chang"],
    "Department": ["Sales", "Engineering", "Admin", "Sales", "Marketing", "Engineering", "Sales", "Admin"],
    "Salary": [45000, 60000, 38000, 45000, 50000, 60000, 42000, 38000]
})

df.to_excel("sample_input/data.xlsx", index=False)
print("Sample file created!")
