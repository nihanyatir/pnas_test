import requests
from bs4 import BeautifulSoup

#133 pages

link_list = []

for 1 in (range(1,2)):
    url = "https://www.pnas.org/content/by/section/Psychological%20and%20Cognitive%20Sciences?page=" + str(1)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')

    for link in soup.find_all(class_='highwire-cite-metadata-pages'):
        elem_to_str = str(link)
        link_list.append(elem_to_str[elem_to_str.find('">')+2:elem_to_str.find(";")])

print(len(link_list))

pdf_urls = []
elem = []

for i in range(len(link_list)):
    elem = ["https://www.pnas.org/content/pnas/" + str(link_list[i][-3:]) + "/" + str(link_list[i][1:3]) + "/" + str(link_list[i]) + ".full.pdf"]
    pdf_urls.append(elem)
    i += 1

print(*pdf_urls, sep='\n')