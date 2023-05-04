import requests
from tqdm import tqdm 
from bs4 import BeautifulSoup
import argparse

def main(urls):
    confs = []
    for url in tqdm(urls, desc="Crawling Conferences"):
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        soup = soup.find_all('div', class_='media-body')
        soup = [i.find('h5', class_='media-heading') for i in soup]
        soup = [str(i).split('''<h5 class="media-heading">''', 1)[1] for i in soup]
        soup = [str(i).split('''<span''', 1)[0] for i in soup]
        confs.append(soup)
    conf_intersect = set.intersection(*map(set, confs))
    print('Writing to members.txt ...')
    with open('members.txt', 'w') as f:
        for url, conf in zip(urls, confs):
            f.write(f'{url}\n')
            f.write('\n'.join(conf))
            f.write('\n\n\n')
        f.write('Overlapping Members:\n')
        f.write('\n'.join(conf_intersect))
    print('Done')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', nargs='+', type=str, required=True, help='FSE or ASE URL which lists all PC members')
    args = parser.parse_args()
    main(args.c)