# 🗽 NYC Airbnb Data Integration & Analysis

This project focuses on cleaning, merging, and analyzing Airbnb listing data from New York City using Python and pandas. The dataset combines information from multiple sources and formats — CSV, Excel, and TSV — to generate a consolidated, analysis-ready dataset for exploring trends in room types, pricing, and review activity.

---

## 📌 Project Objective

To integrate and analyze multi-format Airbnb data in order to:
- Identify the earliest and most recent review activity
- Clean and standardize room type and price data
- Calculate the number of private rooms and average listing price
- Produce a structured summary DataFrame for downstream reporting or visualization

---

## 📁 Data Sources

1. **`airbnb_price.csv`**  
   - Contains listing IDs, prices (in text), and full neighborhood names  
2. **`airbnb_room_type.xlsx`**  
   - Includes listing IDs, room types, and descriptions  
3. **`airbnb_last_review.tsv`**  
   - Provides host names and last review dates  

---

## 🔧 Key Features

### 🔗 Multi-Source Data Merging
Merged three files using `listing_id` as the common key to build a unified dataset.

### 🧹 Data Cleaning & Transformation
- Cleaned `price` column (removed `"dollars"` and converted to `float`)
- Standardized `room_type` to lowercase for consistent filtering
- Converted `last_review` to datetime using custom format (`%B %d %Y`)

### 📊 Key Metric Extraction
- Counted the number of **private room** listings
- Computed **average price** of listings
- Extracted **first** and **last** review dates across all listings

### 📄 Summary Output
Created a final `review_dates` DataFrame with:
- `first_reviewed`: Earliest review date
- `last_reviewed`: Most recent review date
- `nb_private_rooms`: Count of private room listings
- `avg_price`: Rounded average price across all listings

---

## 💻 Tech Stack

- **Python** (pandas, NumPy) – Data manipulation and analysis  
- **Jupyter Notebook** – Interactive development and documentation  
- **File Formats** – CSV, XLSX (Excel), TSV (tab-separated values)  
- **Datetime Parsing** – Custom handling of review date strings  
- **Text Normalization** – For room type filtering and currency cleanup  

---

## 📈 Why This Project?

Real-world data is rarely clean or unified. This project simulates a practical data wrangling task where multiple file formats and inconsistent data types must be cleaned and integrated. The final result is an analysis-ready dataset that could power dashboards, inform business strategy, or be extended for machine learning use.

---

## 📎 Sample Output

```python
  first_reviewed last_reviewed  nb_private_rooms  avg_price
0   2019-04-01     2019-05-31               2248      141.78
