from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parent
RAW_DATA = ROOT / "data" / "raw" / "raw_data"
PROCESSED_DATA = ROOT / "data" / "processed"


def main() -> None:
    """Read the raw Excel files, plot the data, and export combined results."""
    source = RAW_DATA / "fsi-2020.xlsx"
    if not source.exists():
        raise FileNotFoundError(f"Input file not found: {source}")

    data = pd.read_excel(source, index_col=0)
    if len(data.columns) >= 3:
        data.iloc[:, 2].plot(figsize=(15, 2.5), title="Selected 2020 Series")
        plt.tight_layout()
        plt.show()

    files = sorted(RAW_DATA.glob("*.xlsx"))
    if not files:
        raise FileNotFoundError(f"No Excel files found in {RAW_DATA}")

    combined = pd.concat(
        [pd.read_excel(file, index_col=0) for file in files],
        ignore_index=True,
    )

    if "Total" in combined.columns:
        combined["Total"].plot(title="Total")
        plt.tight_layout()
        plt.show()

    PROCESSED_DATA.mkdir(parents=True, exist_ok=True)
    combined.to_excel(PROCESSED_DATA / "visualized_data.xlsx", index=True)
    combined.to_csv(PROCESSED_DATA / "visualized_data.csv", index=True)
    print(f"Processed {len(files)} Excel files into {PROCESSED_DATA}")


if __name__ == "__main__":
    main()
