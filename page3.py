import requests
from requests import get
from bs4 import BeautifulSoup

url = 'https://business.abidjan.net/PJ/scat.asp?CatID=1&ScatID=804'

response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')

if response.status_code == 200:

    # div_modu = html_soup.find('div', attrs = {'id':'content_left'})
    div_mod = html_soup.find_all('div', attrs = {'id':'module'})[1]
    mode = div_mod.find('table')
   
    tr = mode.find_all('table')
    
    
    # print(tr)
            
    
    for item in tr:
        # trs = item.find('tr')                           
        a = item.find('a')
        # print(a)
        if a is not None:
            liens = a['href']
            entreprise = a.get_text()
            # print(liens)
            data ={
                'entreprise':entreprise,
                'lien':liens,
            }
            print(data)
                    
else:
    print('erreur statut',status_code)