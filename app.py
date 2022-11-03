import requests
from bs4 import BeautifulSoup

WEBSITE_URL = "https://en.wikipedia.org/wiki/Julia_(programming_language)"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

def main():
    page = requests.get(WEBSITE_URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find element with class 'infobox vevent'
    infobox = soup.find('table', class_='infobox vevent')

    # Find all 'img' tags in the infobox
    images = infobox.find('td', class_='infobox-image').find_all('img')

    # Find tr where th has Text 'paradigm'
    paradigm = infobox.find('th', text='Paradigm').parent
    # Find td in the above tr
    paradigm = paradigm.find('td')
    # Find all 'a' tags in the td
    paradigm = paradigm.find_all('a')

    # Find tr where th has Text 'First appeared'
    first_appeared = infobox.find('th', text='First\&nbsp;appeared').parent
    # Find td in the above tr
    first_appeared = first_appeared.find('td')
    # Find all 'a' tags in the td
    first_appeared = first_appeared.find_all('a')

    #Find tr where th has Text 'Typing discipline'
    typing_discipline = infobox.find('th', text='Typing discipline').parent
    # Find td in the above tr
    typing_discipline = typing_discipline.find('td')
    # Find all 'a' tags in the td
    typing_discipline = typing_discipline.find_all('a')


    language = {
        'name': 'Julia',
        'paradigm': [p.text for p in paradigm],
        'typing_discipline': [t.text for t in typing_discipline],
        'release_date': first_appeared,
        'images': [i['src'] for i in images]
    }

    # get sixth element from info box
    # forma alternativa de pegar o release date
    # infobox.find_all('tr')[5].text



    print(language)


if __name__ == '__main__':
    main()