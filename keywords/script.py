from googlesearch import search
import urllib.request
from bs4 import BeautifulSoup
from collections import Counter

def get_urls():
    query = "arteterapia es wikipedia"
    results = []
    for i in search(query,tld='com.ar',lang='es',num=10,start=0,stop=10,pause=2.0):
        if 'es.wikipedia' in i:
            print(i)
            page = urllib.request.urlopen(i)
            soup = BeautifulSoup(page,"html.parser")
            a = soup.get_text().lower().split()
            for j in a:
                results.append(j)

    print(Counter(results).most_common(30))


def main():
    get_urls()
if __name__ == '__main__':
    main()