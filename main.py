from bs4 import BeautifulSoup
import requests
import pandas as pd

print("start")

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0', 'Host':'www.tokopedia.com', 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 'Accept-Language':'id,en-US;q=0.7,en;q=0.3', 'Accept-Encoding':'gzip, deflate, br', 'Connection': 'keep-alive'}
page = requests.get("https://www.tokopedia.com/search?st=product&q=eiger&srp_component_id=02.01.00.00&navsource=home", headers=header)
soup = BeautifulSoup(page.content, 'html.parser')

productNameWrappter = soup.findAll('div', {'class': 'css-12fc2sy'})
productPriceWrappter = soup.findAll('div', {'class': 'css-a94u6c'})
datas = []

for item in range(len(productNameWrappter)) :
    prodItem = {
        "productName": productNameWrappter[item].getText(),
        "price": productPriceWrappter[item].getText()
    }
    datas.append(prodItem)

df = pd.DataFrame(datas)
print(df)