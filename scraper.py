import json
import os

import grequests
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


def get_data_from_api():
    '''
    Retrieve data from quotes API. For the first time the API is called and the data is cached inside quotes.json file.
    For subsequent requests, data is served from cached file (quotes.json)
    This is to reduce unnecessary server load and time required to get quotes data
    '''
    if os.path.exists('quotes.json'):
        print('[x] Quotes API call not required as data available in quotes.json')
        with open('quotes.json') as f:
            data = json.loads(f.read())
        return data
    else:
        print('[!] Quotes API call required as quotes.json does not exist')
        url = 'https://type.fit/api/quotes'
        response_json = requests.get(url).json()
        with open('quotes.json', 'w') as f:
            f.write(json.dumps(response_json))
        print('[x] Stored data in quotes.json')
        return response_json


def create_author_quote_mapping(api_response):
    '''
    Create a list of quotes for each author, where author name is available
    '''
    author_quote_mapping = {}
    for item in api_response:
        author = item['author']
        quote = item['text']
        if author:
            if author not in author_quote_mapping:
                author_quote_mapping[author] = []
            author_quote_mapping[author].append(quote)
    return author_quote_mapping


def get_author_image(authors):
    '''
    Get author image from Wikipedia, if exists
    Create author to author image mapping and store as images.json
    '''
    if os.path.exists('images.json'):
        print('[x] Web scraping Wikipedia for author images not required as data available in images.json')
        with open('images.json') as f:
            images = json.loads(f.read())
    else:
        print('[!] images.json file does not exist')
        print('[x] Fetching author data from Wikipedia')
        urls = (
            f'https://en.wikipedia.org/wiki/{author}' for author in authors)
        rs = (grequests.get(u) for u in urls)
        responses = grequests.map(rs)
        image_not_found_count = 0
        images = {}
        print('[x] Parsing author image links from Wikipedia data')
        for response in tqdm(responses):
            try:
                soup = BeautifulSoup(response.text, 'lxml')
                author = response.url.split('/')[-1].replace('_', ' ')
                td = soup.find('td', class_='infobox-image')
                image = td.find('img')
                images[author] = f'https:{image["src"]}'
            except AttributeError:
                image_not_found_count += 1
        print(
            f'[!] Could not find images for {image_not_found_count} out of {len(authors)} authors')
        with open('images.json', 'w') as f:
            f.write(json.dumps(images))
    return images

# from: https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def get_quotes_with_author_images():
    api_data = get_data_from_api()
    author_quote_mapping = create_author_quote_mapping(api_data)
    # sort dict alphabetically based on key (author name): https://stackoverflow.com/questions/24728933/sort-dictionary-alphabetically-when-the-key-is-a-string-name/24728952
    author_quote_mapping = dict(
        sorted(author_quote_mapping.items(), key=lambda x: x[0].lower()))
    images = get_author_image(list(author_quote_mapping.keys()))
    # consider quotes from only those authors whose image is available
    quotes_with_author_images = [
        {'name': author, 'image': images[author], 'quotes': quotes}
        for author, quotes in author_quote_mapping.items()
        if author in images
    ]

    return chunks(quotes_with_author_images, 3)


if __name__ == "__main__":
    get_quotes_with_author_images()
