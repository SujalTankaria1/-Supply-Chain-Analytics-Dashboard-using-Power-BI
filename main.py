import pandas as pd

# === 1. Clean Orders Data ===
orders = pd.read_csv("orders.csv")
orders['OrderDate'] = pd.to_datetime(orders['OrderDate'])
orders['DeliveryDate'] = pd.to_datetime(orders['DeliveryDate'])
orders['DeliveryDelay'] = (orders['DeliveryDate'] - orders['OrderDate']).dt.days

# === 2. Clean Inventory Data ===
inventory = pd.read_csv("inventory.csv")
inventory['ProductID'] = inventory['ProductID'].str.strip()
inventory['WarehouseID'] = inventory['WarehouseID'].str.strip()
inventory['StockLevel'] = inventory['StockLevel'].fillna(inventory['StockLevel'].median())

# === 3. Clean Products Data ===
products = pd.read_csv("products.csv")
products['ProductID'] = products['ProductID'].str.strip()
products['ProductName'] = products['ProductName'].str.strip()
products['Category'] = products['Category'].str.title()
products.drop_duplicates(subset='ProductID', inplace=True)

# === 4. Clean Suppliers Data ===
suppliers = pd.read_csv("suppliers.csv")
suppliers['SupplierID'] = suppliers['SupplierID'].str.strip()
suppliers['SupplierName'] = suppliers['SupplierName'].str.strip()
suppliers['Location'] = suppliers['Location'].str.title()
suppliers['Rating'] = suppliers['Rating'].fillna(suppliers['Rating'].mean())

# === Save All to One Excel File ===
output_file = "SupplyChain_Cleaned_Combined.xlsx"
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    orders.to_excel(writer, sheet_name="Orders", index=False)
    inventory.to_excel(writer, sheet_name="Inventory", index=False)
    products.to_excel(writer, sheet_name="Products", index=False)
    suppliers.to_excel(writer, sheet_name="Suppliers", index=False)

print(f"✅ All sheets saved to: {output_file}")
