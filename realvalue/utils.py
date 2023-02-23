import pandas as pd
import requests
from bs4 import BeautifulSoup

def autobox(user_input='7732УАА', user_input_type='1'):
    url = 'https://www.autobox.mn/'
    req_url = 'https://www.autobox.mn/vhistory.php'
    if user_input_type =='1':
        response = requests.post(req_url, data={'byPlateno': user_input.strip(), 't': 2})
    else:
        response = requests.post(req_url, data={'vinnum': user_input.strip(), 't': 2})
    soup = BeautifulSoup(response.content, "html.parser")
    s = soup.find('td', attrs={'valign': 'top'})
    dt = {'plate_num': s.findAll('td')[2].findAll('b')[1].get_text().strip()
          ,'aral_dugaar': s.findAll('td')[5].find('b').get_text().strip()
          ,'guilt': s.findAll('td')[6].get_text().strip().split('(')[1].split(')')[0]
          ,'guilt_ognoo': s.findAll('td')[6].get_text().strip()[-9:]
          ,'angilal': s.findAll('td')[8].findAll('b')[1].get_text().strip()
          ,'torol': s.findAll('td')[8].findAll('b')[3].get_text().strip()
          ,'suudliin_too': s.findAll('td')[8].findAll('b')[5].get_text().strip()
          ,'mark': s.findAll('td')[9].findAll('b')[1].get_text().strip()
          ,'motor': s.findAll('td')[9].findAll('b')[3].get_text().strip()
          ,'uildverlesen_on': s.findAll('td')[10].findAll('b')[1].get_text().strip()
          ,'orj_irsen_on': s.findAll('td')[10].findAll('b')[3].get_text().strip()
          ,'ungu': s.findAll('td')[11].findAll('b')[1].get_text().strip()
          ,'jin': s.findAll('td')[11].findAll('b')[3].get_text().strip()
          ,'uildverlesen_uls': s.findAll('td')[12].findAll('b')[1].get_text().strip()
          ,'joloonii_hurd': s.findAll('td')[13].findAll('b')[1].get_text().strip()
          ,'hurdnii_hairtsag': s.findAll('td')[13].findAll('b')[3].get_text().strip()}
    return dt
