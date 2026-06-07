import pandas as pd
import glob
import os

def merge_excel_files(input_folder, output_path):
    files = glob.glob(os.path.join(input_folder, "*.xlsx"))
    if not files:
        print("No .xlsx files found.")
        return

    frames = []
    for file in files:
        xl = pd.ExcelFile(file)
        for sheet in xl.sheet_names:
            df = xl.parse(sheet)
            df["Source File"] = os.path.basename(file)
            df["Source Sheet"] = sheet
            frames.append(df)

    result = pd.concat(frames, ignore_index=True)
    result.to_excel(output_path, index=False)
    print(f"Done! Merged {len(frames)} sheet(s) → {output_path}")

if __name__ == "__main__":
    input_folder = "sample_input"
    output_path = "merged_output.xlsx"
    merge_excel_files(input_folder, output_path)
