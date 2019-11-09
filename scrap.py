# importation

import requests
from bs4 import BeautifulSoup
import json

url='https://www.lespagesjaunesafrique.com/'

response= requests.get(url)
print(response.status_code)


if response.status_code == 200:
    
    #-------------RECUPERATION HTML--------------#
    html_soup = BeautifulSoup(response.text, 'html.parser')
    
    #-------------RECUPERATION TITRE--------------#
    div_title = html_soup.find_all('div', attrs = {'class':'col-sm-4 col-xs-6 col-md-4 col-lg-3'})
    
    compt = 1

    for item in div_title:
        
        ba = item.find('a')
        url = ba['href']
        
        pays = item.text 
        print(compt, "\n" + "Pays: " + pays + "\n" + "Lien: " + url + "\n")
        
        compt +=1
    
else:
    print("error", response.status_code)
