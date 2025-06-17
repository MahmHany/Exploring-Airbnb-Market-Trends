# Import necessary packages
import pandas as pd
import numpy as np

# Load Airbnb listing price data from CSV
airbnb_price = pd.read_csv('data/airbnb_price.csv')

# Load Airbnb room type and description data from Excel
airbnb_room = pd.read_excel('data/airbnb_room_type.xlsx')

# Load Airbnb last review and host data from TSV (tab-separated file)
airbnb_last_review = pd.read_csv('data/airbnb_last_review.tsv', sep='\t')

# Merge price and room type data on 'listing_id'
data_2merged = pd.merge(airbnb_price, airbnb_room, on="listing_id")

# Merge the result with review data to create a unified dataset
data = pd.merge(data_2merged, airbnb_last_review, on="listing_id")

# Display the first 10 rows to verify the merged dataset
data.head(10)

# Convert 'last_review' column to datetime format (e.g., 'May 21 2019')
data["last_review"] = pd.to_datetime(data["last_review"], format='%B %d %Y')

# Get the earliest and most recent review dates
first_reviewed = data['last_review'].min()
last_reviewed = data['last_review'].max()

# Check the unique room types before filtering
data['room_type'].unique()

# Convert all values in 'room_type' to lowercase for consistency
data['room_type'] = data['room_type'].str.lower()

# Count the number of listings with room_type = 'private room'
nb_private_rooms = data['room_type'].value_counts()['private room']

# Remove the word 'dollars' from price column and convert to float
data['price'] = data['price'].str.replace("dollars", "")
data['price'] = data['price'].astype(float)

# Calculate the average price of listings
avg_price = data['price'].mean()

# Create a summary DataFrame with key statistics
review_dates = pd.DataFrame({
    "first_reviewed": [first_reviewed],
    "last_reviewed": [last_reviewed],
    "nb_private_rooms": [nb_private_rooms],
    "avg_price": [round(avg_price, 2)]   
})

# Print the summary table
print(review_dates)
