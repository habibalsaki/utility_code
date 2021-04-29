from bs4 import BeautifulSoup
from locators.quotes_page_locators import QuotePageLocators
from parser.quotes import Quotes

class QuotePage:
    def __init__(self,page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        locator = QuotePageLocators.QUOTE
        quote_tags = self.soup.select(locator)
        return [Quotes(e) for e in quote_tags]

