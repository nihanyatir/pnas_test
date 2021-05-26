import requests
from bs4 import BeautifulSoup

#133 pages

link_list = []
vol_list = []
issue_list = []

#volume: <span class="highwire-cite-metadata-volume highwire-cite-metadata">118 </span>
#issue: <span class="highwire-cite-metadata-issue highwire-cite-metadata">(22) </span>

for i in (range(1,2)):
    url = "https://www.pnas.org/content/by/section/Psychological%20and%20Cognitive%20Sciences?page=" + str(i)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')

    for volume in soup.find_all(class_='highwire-cite-metadata-volume'):
        vol_to_str = str(volume)
        #print(vol_to_str)
        vol_list.append(vol_to_str[vol_to_str.find('>')+1:vol_to_str.find('</')-1])
    
    for issue in soup.find_all(class_='highwire-cite-metadata-issue'):
        iss_to_str = str(issue)
        issue_list.append(iss_to_str[iss_to_str.find('>(')+2:iss_to_str.find(")")])

    for link in soup.find_all(class_='highwire-cite-metadata-pages'):
        elem_to_str = str(link)
        link_list.append(elem_to_str[elem_to_str.find('">')+2:elem_to_str.find(';')])

# pdf_urls = []
# elem = []

# for i in range(len(link_list)):
#     elem = "https://www.pnas.org/content/pnas/" + str(link_list[i][-3:]) + "/" + str(link_list[i][1:3]) + "/" + str(link_list[i]) + ".full.pdf"
#     pdf_urls.append(elem)
#     i += 1

# print(*pdf_urls, sep='\n')