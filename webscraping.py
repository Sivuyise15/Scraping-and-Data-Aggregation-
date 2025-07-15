import requests
from bs4 import BeautifulSoup
import csv

# Step 1: URL
url = "https://sivuyise15.github.io/my-website/"

try:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    reviews = soup.find_all('div', class_='review') # The reviews in the html file
    with open('Reviews.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Header in the csv file
        writer.writerow(['review_id', 'author', 'date', 'rating', 'text'])

        for review in reviews:
            review_id = review.get('id', 'N/A')
            author = review.find('span', class_='author').get_text(strip=True)
            date = review.find('span', class_='date').get_text(strip=True)
            rating = review.find('span', class_='rating').get_text(strip=True)
            text = review.find('p', class_='text').get_text(strip=True)

            print(f"{review_id}  {author}  {date}  {rating}  {text}")
            writer.writerow([review_id, author, date, rating, text])
    print("Reviews written to a csv file")

except Exception as e:
    
    print("Exception occurred, the website might not be allowing scraping")