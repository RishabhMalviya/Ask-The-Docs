import os
import re
import yaml
import requests

from pathlib import Path
from bs4 import BeautifulSoup

from ask_the_docs.scrapers.ray.page_parser import get_cleaned_text


HOME_URL = "https://docs.ray.io/en/latest/ray-overview/index.html"
homepage_soup = BeautifulSoup(requests.get(HOME_URL).content, 'html.parser')
toc_top_level_tags = homepage_soup.find_all("li", class_=re.compile(r"toctree-l1 has-children"))


def save_sub_library_urls(sub_library: str = "Ray RLlib") -> None:
    """
    Finds all HTML files in the Ray Docs for the given sub-library
    Saves the list HTML files URLs in the `data` directory
    """
    sub_library_name_simplified = re.sub(r"( )+", lambda x: "_", sub_library).lower()
    sub_library_tags = list(filter(lambda tag: tag.findNext("a").string.strip() == sub_library, toc_top_level_tags))[0]

    sub_library_urls = {
        "urls" : ['https://docs.ray.io/en/latest/' + link_tag.get('href')[2:] for link_tag in sub_library_tags.find_all("a")]
    }
    
    with open(f"./data/urls/{sub_library_name_simplified}.yaml", "w+") as f:
        yaml.dump(sub_library_urls, f)


def extract_text(sub_library: str = "Ray RLlib"):
    """
    Parses all the HTML URLs for the given sub library and
    dumps the text contents into a specified folder
    """
    sub_library_name_simplified = re.sub(r"( )+", lambda x: "_", sub_library).lower()
    
    urls = yaml.safe_load(Path(f"./data/urls/{sub_library_name_simplified}.yaml").read_text())["urls"]

    for idx, url in enumerate(urls):
        print(f'Parsing URL {idx+1}/{len(urls)}: {url}')

        page_name = url.split('/')[-1][:-5]
        output_filepath = f"./data/text/{sub_library_name_simplified}/{page_name}.txt"
        os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
        with open(output_filepath, "w+") as f:
            yaml.dump(get_cleaned_text(url), f)
