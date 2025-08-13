import pandas as pd
import numpy as np

# ========================
# 1. Load the CSV files
# ========================
begin_inventory = pd.read_csv("BegInvFINAL12312016_cleaned.csv")
purchase_prices = pd.read_csv("2017PurchasePricesDec_cleaned.csv")

# ========================
# 2. Keep only needed columns & drop duplicates
# ========================
begin_inventory = begin_inventory[["Brand", "Description", "Size", "onHand", "Store"]].drop_duplicates()
purchase_prices = purchase_prices[["Brand", "Description", "Size", "PurchasePrice"]].drop_duplicates()

# ========================
# 3. Merge on common keys
# ========================
df = pd.merge(
    begin_inventory,
    purchase_prices,
    on=["Brand", "Description", "Size"],
    how="inner"
)
print(f"✅ Merged rows: {len(df)}")

# ========================
# 4. Calculate Total Value
# ========================
df["TotalValue"] = df["onHand"] * df["PurchasePrice"]

# ========================
# 5. Demand Forecasting (Simple moving average using onHand)
# ========================
df["Forecast_Demand"] = df["onHand"].rolling(window=3, min_periods=1).mean()

# ========================
# 6. ABC Analysis
# ========================
df["Annual_Consumption_Value"] = df["onHand"] * df["PurchasePrice"]
df = df.sort_values("Annual_Consumption_Value", ascending=False)
df["Cumulative_Value"] = df["Annual_Consumption_Value"].cumsum()
total_value = df["Annual_Consumption_Value"].sum()
df["Cumulative_Percentage"] = 100 * df["Cumulative_Value"] / total_value

def classify_abc(x):
    if x <= 80:
        return "A"
    elif x <= 95:
        return "B"
    else:
        return "C"

df["ABC_Category"] = df["Cumulative_Percentage"].apply(classify_abc)

# ========================
# 7. EOQ Calculation
# ========================
ordering_cost = 50        # Example cost per order
carrying_cost_rate = 0.2  # 20% annual carrying cost rate
df["Annual_Demand"] = df["onHand"] * 12
df["Holding_Cost"] = df["PurchasePrice"] * carrying_cost_rate
df["EOQ"] = np.sqrt((2 * df["Annual_Demand"] * ordering_cost) / df["Holding_Cost"])

# ========================
# 8. Reorder Point (ROP)
# ========================
# Simulate lead time & safety stock if missing
df["LeadTimeDays"] = np.random.randint(5, 15, size=len(df))
df["SafetyStock"] = np.random.randint(5, 20, size=len(df))
df["Avg_Daily_Demand"] = df["onHand"] / 30
df["ROP"] = (df["Avg_Daily_Demand"] * df["LeadTimeDays"]) + df["SafetyStock"]

# ========================
# 9. Carrying Cost
# ========================
df["Carrying_Cost"] = df["Holding_Cost"] * df["onHand"]

# ========================
# 10. Inventory Turnover
# ========================
df["QuantitySold"] = np.random.randint(10, 100, size=len(df))  # Simulated
df["Inventory_Turnover"] = df["QuantitySold"] / df["onHand"]

# ========================
# 11. Save Results
# ========================
df.to_csv("Inventory_Analysis_Full.csv", index=False)

# Summary files
summary_by_brand = df.groupby("Brand", as_index=False)["TotalValue"].sum()
summary_by_brand.to_csv("Summary_By_Brand.csv", index=False)

summary_by_store = df.groupby("Store", as_index=False)["TotalValue"].sum()
summary_by_store.to_csv("Summary_By_Store.csv", index=False)

print("\n✅ Inventory Analysis Completed!")
print("📁 Saved: Inventory_Analysis_Full.csv, Summary_By_Brand.csv, Summary_By_Store.csv")
print("\nSample Output:")
print(df.head())
