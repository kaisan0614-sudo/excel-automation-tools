import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice Wang", "Bob Lee", "Carol Chang", "David Chen", "Eva Lin", "Frank Huang", "Grace Wu", "Henry Liu"],
    "Department": ["Sales", "Engineering", "Admin", "Marketing", "Engineering", "Sales", "Admin", "Engineering"],
    "Level": ["Associate", "Engineer", "Associate", "Associate", "Senior Engineer", "Senior Associate", "Associate", "Engineer"],
    "Salary": [45000, 60000, 38000, 50000, 75000, 52000, 36000, 62000]
})

df.to_excel("sample_input/employee_data.xlsx", index=False)
print("Sample file created!")
