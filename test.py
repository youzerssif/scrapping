import requests
from requests import get
from bs4 import BeautifulSoup

url = 'https://business.abidjan.net/PJ/'

response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')

if response.status_code == 200:

        # div_module = html_soup.find_all('div', attrs = {'id':'module'})[1]
        # div_mod = html_soup.find_all('div', attrs = {'id':'module'})[0]
        # div1 = div_module.find_all('table')[0]
        # nom_entreprise = div_module.find_all('p')[0]
        # trs = div1.find_all('tr')[1]
        # tr = div1.find_all('tr')[5]
        # email_entreprise = tr.find('a')
        # print('nom:{0}\n\n email:{1}'.format(nom_entreprise.text, email_entreprise.text))
        # div_module = html_soup.find('div', attrs = {'id':'content_left'})
        # module = div_module.find_all('div', attrs = {'class':'col-sm-6 col-p10'})
        
        # for item in module:
                
        #         div = item.find('div', attrs = {'class':'col-sm-8 col-8 col-per'})
        #         a = div.find('a')
        #         lien = a['href']
                
                
        #-----------------------NEXT PAGE--------------#
        # resp = get()
        # print(resp)
        # soup = BeautifulSoup(resp.text, 'html.parser')
        # div_modul = soup.find('div', attrs = {'id':'content_left'})
        # mod = div_modul.find_all('div', attrs = {'class':'col-sm-6 col-6'})
        # # print(mod)
        
        # for item in mod:
                
        # a = item.find('a')
        # liens = a['href']
        # # print(liens)
        
        # #-----------------------NEXT PAGE--------------#
        # respo = get(url+liens)
        # # print(respo)
        # soupe = BeautifulSoup(respo.text, 'html.parser')
        # # div_modu = soupe.find('div', attrs = {'id':'content_left'})
        # div_mod = soupe.find_all('div', attrs = {'id':'module'})[1]
        # mode = div_mod.find('table')
        # tr = mode.find_all('tr')
        # # print(tr)
        

        # for item in tr:
                                
        #         a = item.find('a')
        #         # print(a)
        #         if a is not None:
        #                 lie = a['href']
        #                 print(lie)
                #-----------------------DATA PAGE--------------#

        res = get("https://business.abidjan.net/PJ/societe.asp?id=14567")
        soup = BeautifulSoup(res.text, 'html.parser')
        div_module = soup.find_all('div', attrs = {'id':'module'})[1]
        div1 = div_module.find_all('table')[0]
        nom_entreprise = div_module.find_all('p')[0]

        trs = div1.find_all('tr')
        for tr in trs:
                tds = tr.find_all('td')
                print(len(tds))
                compt_td = 1
                for td in tds:
                        
                        print(compt_td)
                        if compt_td ==  1:
                                
                                rtext = td.text
                                rigth = rtext.strip()
                                if "géo" in rigth:
                                        print("Address geo")
                                
                        else:
                                rtext = td.text
                                print("Value : ",  rtext.strip()) 
                        compt_td += 1

                


        

else:
        print('erreur statut',status_code)


