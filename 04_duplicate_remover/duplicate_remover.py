import pandas as pd

def remove_duplicates(input_path, output_path, subset=None, keep="first"):
    df = pd.read_excel(input_path)
    original_count = len(df)

    duplicates = df[df.duplicated(subset=subset, keep=False)]
    if len(duplicates) > 0:
        print("Duplicate rows found:")
        print(duplicates.to_string(index=False))
        print()

    df_clean = df.drop_duplicates(subset=subset, keep=keep)
    removed = original_count - len(df_clean)

    df_clean.to_excel(output_path, index=False)
    print(f"Done! {original_count} rows → removed {removed} duplicate(s) → {len(df_clean)} rows remaining")
    print(f"Output → {output_path}")

if __name__ == "__main__":
    remove_duplicates(
        input_path="sample_input/data.xlsx",
        output_path="cleaned_output.xlsx",
        subset=None,   # None = all columns must match; or specify e.g. ["Name", "Department"]
        keep="first"   # "first" keeps first occurrence, "last" keeps last
    )
