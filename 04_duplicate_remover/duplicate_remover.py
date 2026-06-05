import pandas as pd

def remove_duplicates(input_path, output_path, subset=None, keep="first"):
    df = pd.read_excel(input_path)
    original_count = len(df)

    duplicates = df[df.duplicated(subset=subset, keep=False)]
    if len(duplicates) > 0:
        print(f"發現重複資料：")
        print(duplicates.to_string(index=False))
        print()

    df_clean = df.drop_duplicates(subset=subset, keep=keep)
    removed = original_count - len(df_clean)

    df_clean.to_excel(output_path, index=False)
    print(f"完成！原始 {original_count} 筆 → 移除 {removed} 筆重複 → 剩餘 {len(df_clean)} 筆")
    print(f"輸出檔案 → {output_path}")

if __name__ == "__main__":
    remove_duplicates(
        input_path="sample_input/資料.xlsx",
        output_path="cleaned_output.xlsx",
        subset=None,   # None = 所有欄位都相同才算重複，指定欄位名稱如 ["姓名", "部門"]
        keep="first"   # 保留第一筆，"last" 保留最後一筆
    )
