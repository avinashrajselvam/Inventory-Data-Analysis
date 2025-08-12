# 📦 Inventory Data Analysis


## 📜 Overview
This project analyzes **beginning inventory** and **purchase price** data to calculate:
- Annual consumption value per product
- ABC classification of products
- Summary statistics for inventory management decisions

It merges two datasets:
1. **Beginning Inventory Data** (`BegInvFINAL12312016_cleaned.csv`)
2. **Purchase Prices Data** (`2017PurchasePricesDec_cleaned.csv`)

The analysis produces a **ranked list of items** by their annual consumption value and assigns **ABC categories** to help prioritize inventory control.

---

## 📂 Dataset Description

| File Name | Description | Key Columns |
|-----------|-------------|-------------|
| `BegInvFINAL12312016_cleaned.csv` | Beginning inventory data | `Item_Number`, `Item_Description`, `Annual_Usage` |
| `2017PurchasePricesDec_cleaned.csv` | Purchase prices data | `Item_Number`, `Unit_Price` |

> **Note:** Ensure both datasets have a **common key column** (e.g., `Item_Number`) for merging.

---

## 🛠 Requirements

Before running the code, install the required Python libraries:

```bash
pip install pandas numpy
```

---

## ▶️ How to Run

1. Place both CSV files in the same folder as the script.
2. Update the script with the correct column names if they differ in your dataset.
3. Run the Python script:

```bash
python inventory_analysis.py
```

4. The output will be saved as:
```
inventory_analysis_results.csv
```

---

## 📊 Output Columns

| Column | Description |
|--------|-------------|
| `Item_Number` | Unique identifier for the product |
| `Item_Description` | Name or description of the product |
| `Annual_Usage` | Total quantity used annually |
| `Unit_Price` | Purchase price per unit |
| `Annual_Consumption_Value` | Annual usage × unit price |
| `ABC_Category` | Classification based on Pareto principle |

---

## 📈 ABC Classification Criteria

- **A**: Top 70% of total annual consumption value (high-priority items)
- **B**: Next 20% of total value
- **C**: Remaining 10% of total value (low-priority items)

---

## 📜 License

This project is licensed under the **MIT License** — you are free to use and modify it.
