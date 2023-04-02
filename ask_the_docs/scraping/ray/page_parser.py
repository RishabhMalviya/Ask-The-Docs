import re
import requests

from bs4 import BeautifulSoup

from ask_the_docs.cleaning import RayDocsTextCleaner


def get_cleaned_text(URL: str) -> str:
    soup = BeautifulSoup(requests.get(URL).content, 'html.parser')
    main_text = soup.find('main').get_text()

    return RayDocsTextCleaner().clean(main_text)
