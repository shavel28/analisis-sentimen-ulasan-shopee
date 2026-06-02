from google_play_scraper import reviews
import pandas as pd

result, _ = reviews(
    'com.shopee.id',
    lang='id',
    country='id',
    count=10000
)

df = pd.DataFrame(result)
df = df[['content', 'score']]

df.to_csv('dataset.csv', index=False)

print("Scraping selesai")