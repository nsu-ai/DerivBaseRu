import argparse
import csv
import unicodedata
from collections import defaultdict

import requests
from bs4 import BeautifulSoup


def query_pages():
    params = defaultdict(set, {
        'format': 'json',
        'action': 'query',
        'list': 'categorymembers',
        'cmtitle': 'Категория:Русские_глаголы',
    })

    while True:
        resp = requests.get(
            'https://ru.wiktionary.org/w/api.php',
            params=params
        ).json()

        if 'error' in resp:
            raise ValueError(resp['error'])
        if 'warnings' in resp:
            print(resp['warnings'])
        if 'query' in resp:
            yield resp['query']
        if 'continue' not in resp:
            break
        params.update(resp['continue'])
        print(f'Getting next page with {params}')


def get_page(page_id):
    url = 'https://ru.m.wiktionary.org/wiki/'
    return requests.get(
        url=url,
        params={
            'curid': page_id
        }
    ).content


def get_verb(doc):
    soup = BeautifulSoup(doc, 'html.parser')
    inf = soup.findAll('title', {})[0]
    """
    columns = soup.findAll('td', {
        'align': 'left'
    })
    
    forms = []
    for item in columns:
        forms += map(
            lambda x: sanitize(x).strip(),
            filter(lambda x: isinstance(x, str), item.contents)
        )
    """
    return str(inf)[7:-22]
    try:
        return {
            'infinitive': str(inf)[7:-22],
            'present_i': forms[0],
            'present_thou': forms[4],
            'present_it': forms[8],

            'present_we': forms[13],
            'present_you': forms[16],
            'present_they': forms[19],

            'past_male': forms[9],
            'past_female': forms[10],
            'past_neutral': forms[11],
            'past_many': forms[14],
            'imperative': forms[7]
        }
    except IndexError as ex:
        print(ex)
        return None


def sanitize(word):
    return ''.join(filter(
        lambda x: unicodedata.category(x) != 'Mn' and x not in ['△', '*'],
        unicodedata.normalize('NFD', word)
    ))


def get_progress(current, total):
    return f'{round(current / total * 100)}%'


#def main(*args, **kwargs):
def main():
    #total_pages = 1
    with open('verbs.txt', 'w', newline='\n', buffering=1) as fw:
        counter = 0
        writer = None

        for response in query_pages():
            for elem in response['categorymembers']:
                fw.writelines([elem['title']])
                """
                page_id = elem['pageid']
                page = get_page(page_id)
                verb = get_verb(page)

                if verb is None:
                    print(f'An error occured on page {page_id} processing')
                    continue

                if counter == 0:
                    writer = csv.DictWriter(fw, verb.keys())
                    writer.writeheader()

                writer.writerow(verb)
                """
                counter += 1
                #print(f'{get_progress(counter, total_pages)} {elem}')
            print('*' * 30)
            if counter > 10:
                break

def argparser():
    parser = argparse.ArgumentParser(
        description='Scrape Russian verb forms from Wiktionary.',
        add_help=True
    )
    parser.add_argument(
        '--filename',
        type=str,
        default='verbs.csv',
        help='file to save verb forms to (default: verbs.csv)'
    )
    return parser


if __name__ == '__main__':
    main()
    #main(**vars(argparser().parse_args()))
