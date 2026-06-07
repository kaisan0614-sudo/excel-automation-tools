import pandas as pd

def filter_and_export(input_path, output_path, filters):
    df = pd.read_excel(input_path)
    result = df.copy()

    for col, condition in filters.items():
        if col not in result.columns:
            print(f"Column '{col}' not found, skipping.")
            continue

        if isinstance(condition, dict):
            op = condition.get("op")
            val = condition.get("value")
            if op == ">=":
                result = result[result[col] >= val]
            elif op == "<=":
                result = result[result[col] <= val]
            elif op == ">":
                result = result[result[col] > val]
            elif op == "<":
                result = result[result[col] < val]
            elif op == "==":
                result = result[result[col] == val]
        elif isinstance(condition, list):
            result = result[result[col].isin(condition)]
        else:
            result = result[result[col] == condition]

    result.to_excel(output_path, index=False)
    print(f"Done! {len(result)} row(s) matched → {output_path}")

if __name__ == "__main__":
    filters = {
        "Department": ["Engineering", "Sales"],
        "Salary": {"op": ">=", "value": 45000}
    }
    filter_and_export("sample_input/employee_data.xlsx", "filtered_output.xlsx", filters)
