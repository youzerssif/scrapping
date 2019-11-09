import requests
from requests import get
from bs4 import BeautifulSoup

url = 'https://business.abidjan.net/PJ/'

response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')

if response.status_code == 200:
    
    div_module = html_soup.find('div', attrs = {'id':'content_left'})
    module = div_module.find_all('div', attrs = {'class':'col-sm-6 col-p10'})
            
    for item in module:
            #------------RECUPERATION---------------#        
            div = item.find('div', attrs = {'class':'col-sm-8 col-8 col-per'})
            img = item.find('div', attrs = {'class':'col-sm-4 col-4'})
            #------------AFFECTATION---------------# 
            a = div.find('a')
            serv = div.find('span').get_text()
            imag = img.find('img')
            image = imag['src']
            lien = a['href']
            #------------AFFICHAGE---------------#
            print(lien)
            print(image)
            print(serv)
else:
    print('erreur statut',status_code)