import urllib.request
import sys
import argparse
from googlesearch import search
from bs4 import BeautifulSoup
from collections import Counter

def get_options():
    parser = argparse.ArgumentParser(sys.argv[1:])
    parser.add_argument("-q", "--query", type=str, help="")
    parser.add_argument("-d", "--tld", type=str, help="Top Level Domain. Where to search.", default='com')
    parser.add_argument("-l", "--lang", type=str, help="Languaje to use in the search.")
    parser.add_argument("-n", "--num", type=int, help="How many results per page to show.")
    parser.add_argument("-s", "--start", type=int, help="First result to scrap.")
    parser.add_argument("-e", "--stop", type=int, help="Last result to scrap.")
    parser.add_argument("-p", "--pause", type=float, help="How many seconds to wait between scrapings.")
    parser.add_argument("-t", "--top", type=int, help="Top most common results.")
    options = parser.parse_args()
    return options

def get_urls(options):
    results = []
    for i in search(options.query, tld=options.tld, lang=options.lang, num=options.num, start=options.start, stop=options.stop, pause=options.pause):
        page = urllib.request.urlopen(i)
        soup = BeautifulSoup(page,"html.parser")
        a = soup.get_text().lower().split()
        for j in a:
            results.append(j)

    print(Counter(results).most_common(options.top))

def main():
    options = get_options()
    get_urls(options)

if __name__ == '__main__':
    main()