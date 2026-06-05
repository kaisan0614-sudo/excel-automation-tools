import pandas as pd

def filter_and_export(input_path, output_path, filters):
    df = pd.read_excel(input_path)
    result = df.copy()

    for col, condition in filters.items():
        if col not in result.columns:
            print(f"欄位「{col}」不存在，略過")
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
    print(f"完成！篩選出 {len(result)} 筆資料 → {output_path}")

if __name__ == "__main__":
    filters = {
        "部門": ["工程", "業務"],
        "薪資": {"op": ">=", "value": 45000}
    }
    filter_and_export("sample_input/員工資料.xlsx", "filtered_output.xlsx", filters)
