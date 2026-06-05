import pandas as pd
import glob
import os

def merge_excel_files(input_folder, output_path):
    files = glob.glob(os.path.join(input_folder, "*.xlsx"))
    if not files:
        print("找不到任何 .xlsx 檔案")
        return

    frames = []
    for file in files:
        xl = pd.ExcelFile(file)
        for sheet in xl.sheet_names:
            df = xl.parse(sheet)
            df["來源檔案"] = os.path.basename(file)
            df["來源工作表"] = sheet
            frames.append(df)

    result = pd.concat(frames, ignore_index=True)
    result.to_excel(output_path, index=False)
    print(f"完成！合併 {len(frames)} 張工作表 → {output_path}")

if __name__ == "__main__":
    input_folder = "sample_input"
    output_path = "merged_output.xlsx"
    merge_excel_files(input_folder, output_path)
