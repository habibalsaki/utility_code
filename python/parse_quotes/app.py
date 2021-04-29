from pages.quotes_page import QuotePage

import requests

page_content = requests.get('https://quotes.toscrape.com/').content
page = QuotePage(page_content)

for quote in page.quotes:
    print(quote)