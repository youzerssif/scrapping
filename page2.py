import requests
from requests import get
from bs4 import BeautifulSoup

url = 'https://business.abidjan.net/PJ/cat.asp?catid=1'

response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')

if response.status_code == 200:

    div_modul = html_soup.find('div', attrs = {'id':'content_left'})
    mod = div_modul.find_all('div', attrs = {'class':'col-sm-6 col-6'})
    # print(mod)
            
    for item in mod:
                    
        a = item.find('a')
        sous = a.get_text()
        liens = a['href']
        data ={
            'sous-categorie':sous,
            'lien':liens,
        }
        print(data)
        
else:
    print('erreur statut',status_code)