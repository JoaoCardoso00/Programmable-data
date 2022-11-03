import requests
import os
import shutil
from bs4 import BeautifulSoup


WEBSITE_URL = "https://en.wikipedia.org/wiki/Java_(programming_language)"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
CURRENT_DIRECTORY = os.getcwd()
SUBDIR = "anexos"
PATH_ANEXOS = os.path.join(CURRENT_DIRECTORY, SUBDIR)

def main():
    page = requests.get(WEBSITE_URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')







if __name__ == '__main__':
    main()