import requests
from bs4 import BeautifulSoup
import csv

british_airways_data = []

for x in range(1, 41): 
    website = f"https://www.airlinequality.com/airline-reviews/british-airways/page/{x}/?sortby=post_date%3ADesc&pagesize=100"
    r = requests.get(website)
    soup = BeautifulSoup(r.content, "lxml")

    review_blocks = soup.find_all("article", class_="comp_media-review-rated")

    for review in review_blocks:
        review_data = {}

        # Name, Location, Date
        header = review.find("h3", class_="text_sub_header userStatusWrapper")
        if header:
            name_tag = header.find("span", itemprop="name")
            review_data["Name"] = name_tag.get_text(strip=True) if name_tag else "NaN"

            date_tag = header.find("time", itemprop="datePublished")
            review_data["Date"] = date_tag.get_text(strip=True) if date_tag else "NaN"

            header_text = header.get_text(" ", strip=True)
            if "(" in header_text and ")" in header_text:
                review_data["Location"] = header_text.split("(")[-1].split(")")[0].strip()
            else:
                review_data["Location"] = "NaN"
        else:
            review_data["Name"] = review_data["Date"] = review_data["Location"] = "NaN"

        # Short Summary
        summary_tag = review.find("h2", class_="text_header")
        review_data["Short Summary"] = summary_tag.get_text(strip=True) if summary_tag else "NaN"

        # Verification and Full Review
        body = review.find("div", class_="text_content")
        if body:
            strong = body.find("strong")
            em_tag = strong.find("em") if strong else None

            if em_tag and "Trip Verified" in em_tag.get_text(strip=True):
                review_data["Verification"] = "✅ Trip Verified"
            else:
                review_data["Verification"] = "Not Verified"

            if strong:
                strong.decompose()

            full_text = body.get_text(strip=True).replace("✅", "").replace("|", "").strip()
            review_data["Full Review"] = full_text
        else:
            review_data["Verification"] = "Not Verified"
            review_data["Full Review"] = "NaN"

        # Rating
        rating_tag = review.find("div", itemprop="reviewRating")
        if rating_tag:
            rating_value = rating_tag.find("span", itemprop="ratingValue")
            review_data["Rating"] = rating_value.get_text(strip=True) if rating_value else "NaN"
        else:
            review_data["Rating"] = "NaN"

        # Review Table
        table = review.find("table", class_="review-ratings")
        desired_fields = [
            "Aircraft", "Type Of Traveller", "Seat Type",
            "Route", "Date Flown", "Seat Comfort", "Cabin Staff Service",
            "Food & Beverages", "Inflight Entertainment", "Ground Service",
            "Wifi & Connectivity", "Value For Money"
        ]

        # Initialize all to NaN
        for field in desired_fields:
            review_data[field] = "NaN"

        if table:
            rows = table.find_all("tr")
            for row in rows:
                header_cell = row.find("td", class_="review-rating-header")
                value_cell = row.find("td", class_="review-value") or row.find("td", class_="review-rating-stars")
                if header_cell and value_cell:
                    key = header_cell.get_text(strip=True)
                    if key in desired_fields:
                        # Handle stars as numbers
                        if "review-rating-stars" in value_cell.get("class", []):
                            stars = value_cell.find_all("span", class_="star fill")
                            review_data[key] = str(len(stars))
                        else:
                            review_data[key] = value_cell.get_text(strip=True)

        # Recommended
        recommended_td = table.find("td", class_="review-value rating-yes") if table else None
        review_data["Recommended"] = "yes" if recommended_td else "no"

        british_airways_data.append(review_data)

# Save CSV
columns = []
for review in british_airways_data:
    for key in review:
        if key not in columns:
            columns.append(key)

with open("British_Airways_Data.csv", mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()
    for review in british_airways_data:
        for key in columns:
            if key not in review:
                review[key] = "NaN"
        writer.writerow(review)

print("CSV file saved successfully.")
