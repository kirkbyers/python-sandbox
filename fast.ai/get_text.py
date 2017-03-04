import bs4 as bs
import requests
import numpy as np

response = requests.get('http://www.hplovecraft.com/writings/texts/fiction/cc.aspx')
soup = bs.BeautifulSoup(response.text, 'html5lib')
text = soup.findAll(align="justify")[0]

with open ("The_Call_of_Cthulhu.txt", 'wb') as f:
    f.write(text.find(align="justify").get_text(strip=True).encode("utf8"))
