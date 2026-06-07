import pandas as pd

df = pd.DataFrame({
    "Product": ["Keyboard", "Mouse", "Monitor", "Headset", "Webcam"],
    "Quantity Sold": [120, 340, 85, 210, 95],
    "Unit Price": [1200, 450, 8900, 1500, 2200],
    "Total Sales": [144000, 153000, 756500, 315000, 209000]
})

df.to_excel("sample_input/data.xlsx", index=False)
print("Sample file created!")
