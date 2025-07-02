# 📦 Supply Chain Analytics Dashboard (Power BI)

A data-driven dashboard built with Power BI to analyze the performance of supply chain operations, including delivery efficiency, supplier reliability, and inventory management.

---

## 📊 Project Overview

This project showcases how data can be cleaned, structured, and visualized to extract actionable insights in a supply chain setting. The dataset simulates order, product, inventory, and supplier details.

### Key Objectives:
- Analyze average delivery delays across products and suppliers
- Identify delayed vs on-time orders
- Visualize stock levels by warehouse
- Rate and compare supplier performance

---

## 🛠 Tools & Technologies

| Tool         | Purpose                             |
|--------------|-------------------------------------|
| **Power BI** | Dashboard creation and data modeling |
| **Python (Pandas)** | Data cleaning & transformation      |
| **Excel**    | Initial data review and formatting   |
| **DAX**      | Custom measures & calculated columns |

---

## 📁 Folder Structure
📦 SupplyChain-Analytics-Dashboard
├── SupplyChain_Cleaned_Combined.xlsx # Cleaned dataset with all tables
├── SupplyChain_Dashboard.pbix # Power BI dashboard file
├── main.py # Python script used to clean and export the data
├── images/
│ ├── dashboard-overview.png # Screenshot of dashboard
└── README.md # Project documentation


---

## 📸 Dashboard Preview

![Dashboard Screenshot](images/Dashboard-overview.png)

> The dashboard includes visuals like:
> - Avg Delivery Delay (Card)
> - Delay by Product (Bar Chart)
> - Delay Over Time (Line Chart)
> - Supplier Ratings (Bar)
> - Inventory Levels by Product (Table/Map)

---

## ⚙ Data Model & Relationships

- `Orders[ProductID]` → `Products[ProductID]`
- `Orders[SupplierID]` → `Suppliers[SupplierID]`
- `Inventory[ProductID]` → `Products[ProductID]`

---

## 🔎 DAX Measures Used

```DAX
AvgDelay = AVERAGE(Orders[DeliveryDelay])

DelayedOrders = COUNTROWS(
    FILTER(Orders, Orders[DeliveryDelay] > 3)
)


