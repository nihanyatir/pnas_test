import requests
from bs4 import BeautifulSoup

#https://www.pnas.org/content/by/section/Psychological%20and%20Cognitive%20Sciences?page=1
#sayfa sayisi 133

pdf_urls = []

for i in (range(1,2)):
    url = "https://www.pnas.org/content/by/section/Psychological%20and%20Cognitive%20Sciences?page=" + str(i)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')

    for link in soup.find_all(class_='highwire-cite-metadata-pages'):
        nihan = str(link)
        pdf_urls.append(nihan[nihan.find('">')+2:nihan.find(";")])

    print(*pdf_urls, sep='\n')
    #yorumekledim

    #print(ext_ids)

    #print(find_ids)
    #pdf_urls.append(soup.find_all(class_='highwire-cite-metadata-pages'))
    #print(pdf_urls)