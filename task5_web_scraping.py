import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import time
from urllib.parse import urljoin

# TASK 5: WEB SCRAPING AND ANALYSIS

BASE_URL = "https://books.toscrape.com/"

# Create output folder
os.makedirs("output", exist_ok=True)

books = []

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

print("=" * 60)
print("TASK 5: WEB SCRAPING")
print("=" * 60)

# 1. Scrape 5 Pages

for page in range(1, 6):

    if page == 1:
        url = BASE_URL
    else:
        url = urljoin(
            BASE_URL,
            f"catalogue/page-{page}.html"
        )

    print(f"Scraping page {page}...")

    try:
        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()

    except requests.RequestException as error:
        print(f"Error loading page {page}: {error}")
        continue

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    book_items = soup.select(
        "article.product_pod"
    )

    for book in book_items:

        # Book title
        title = book.h3.a.get("title", "").strip()

        # Price
        price_text = book.select_one(
            ".price_color"
        ).get_text(strip=True)

        price = price_text.replace("£", "")

        try:
            price = float(price)
        except ValueError:
            price = None

        # Rating
        rating_element = book.select_one(
            "p.star-rating"
        )

        rating = None

        if rating_element:
            rating_classes = rating_element.get("class", [])

            if len(rating_classes) > 1:
                rating_word = rating_classes[1]
                rating = rating_map.get(
                    rating_word
                )

        # Availability
        availability_element = book.select_one(
            ".availability"
        )

        if availability_element:
            availability = availability_element.get_text(
                " ",
                strip=True
            )
        else:
            availability = "Unknown"

        # Product URL
        relative_url = book.h3.a.get(
            "href",
            ""
        )

        product_url = urljoin(
            url,
            relative_url
        )

        # Add data
        books.append({
            "Title": title,
            "Price_GBP": price,
            "Rating": rating,
            "Availability": availability,
            "URL": product_url
        })

    # Wait before next request
    time.sleep(1)

# 2. Create DataFrame

df = pd.DataFrame(books)

print("\nNumber of books collected:", len(df))

print("\nFirst 5 records:")
print(df.head())


# ==========================================
# 3. Clean Data
# ==========================================

print("\nCleaning data...")

# Remove duplicate titles
df = df.drop_duplicates(
    subset=["Title"]
)

# Remove extra spaces
df["Title"] = df["Title"].str.strip()

df["Availability"] = (
    df["Availability"]
    .str.replace(
        r"\s+",
        " ",
        regex=True
    )
    .str.strip()
)

# Convert numeric columns
df["Price_GBP"] = pd.to_numeric(
    df["Price_GBP"],
    errors="coerce"
)

df["Rating"] = pd.to_numeric(
    df["Rating"],
    errors="coerce"
)

# Remove missing important values
df = df.dropna(
    subset=[
        "Title",
        "Price_GBP",
        "Rating"
    ]
)

# 4. Check Cleaned Data

print("\n========== CLEANED DATA ==========")

print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate records:")
print(df.duplicated().sum())

# 5. Exploratory Analysis

print("\n========== EXPLORATORY ANALYSIS ==========")

print("\nPrice Statistics:")
print(df["Price_GBP"].describe())

print("\nRating Statistics:")
print(df["Rating"].describe())


# Average price by rating
average_price = (
    df.groupby("Rating")["Price_GBP"]
    .mean()
)

print("\nAverage Price by Rating:")
print(average_price)


# Rating distribution
rating_distribution = (
    df["Rating"]
    .value_counts()
    .sort_index()
)

print("\nRating Distribution:")
print(rating_distribution)

# 6. Most Expensive Books

print("\nTop 10 Most Expensive Books:")

top_expensive = (
    df.sort_values(
        "Price_GBP",
        ascending=False
    )
    .head(10)
)

print(
    top_expensive[
        ["Title", "Price_GBP", "Rating"]
    ]
)

# 7. Visualization
sns.set_theme(
    style="whitegrid"
)


# Rating distribution
plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="Rating"
)

plt.title(
    "Distribution of Book Ratings"
)

plt.xlabel("Rating")
plt.ylabel("Number of Books")

plt.tight_layout()

plt.savefig(
    "output/book_rating_distribution.png"
)

plt.show()


# Price distribution
plt.figure(figsize=(8, 5))

plt.hist(
    df["Price_GBP"],
    bins=10,
    edgecolor="black"
)

plt.title(
    "Distribution of Book Prices"
)

plt.xlabel("Price (£)")
plt.ylabel("Number of Books")

plt.tight_layout()

plt.savefig(
    "output/book_price_distribution.png"
)

plt.show()


# Price vs Rating
plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Rating",
    y="Price_GBP",
    s=80
)

plt.title(
    "Book Price vs Rating"
)

plt.xlabel("Rating")
plt.ylabel("Price (£)")

plt.tight_layout()

plt.savefig(
    "output/price_vs_rating.png"
)

plt.show()

# 8. Save CSV

csv_file = "output/scraped_books.csv"

df.to_csv(
    csv_file,
    index=False
)

# 9. Save Excel
excel_file = "output/scraped_books.xlsx"

df.to_excel(
    excel_file,
    index=False
)

# 10. Final Report
print("\n" + "=" * 60)
print("SCRAPING COMPLETED SUCCESSFULLY")
print("=" * 60)

print(
    f"\nTotal books collected: {len(df)}"
)

print(
    f"Average price: £{df['Price_GBP'].mean():.2f}"
)

print(
    f"Average rating: {df['Rating'].mean():.2f}"
)

print(
    f"\nCSV file: {csv_file}"
)

print(
    f"Excel file: {excel_file}"
)

print("\nTask 5 completed!")