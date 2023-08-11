import requests
from bs4 import BeautifulSoup
from send_me_email import sendMeEmail

URL = 'https://www.amazon.fr/Tristar-Fondue-Raclette-Multifonction-1300W/dp/B014J7P4KU/ref=sr_1_6?keywords=machine%2Braclette&qid=1691653525&sprefix=machine%2Bra%2Caps%2C149&sr=8-6&th=1'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15'
}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find(id = 'productTitle').get_text()
price = soup.find("span", class_ = "a-price-whole").get_text()
image = soup.find("img", id = "magnifierLens")
convertedPrice = float(price.replace(",", ""))
myBudget = 35 ##Eur
if(convertedPrice <= myBudget):
    print("The price of the product has become suitable for your budget")
    htmlContent = """"\
        <html>
        <body>
        <h3>{0}</h3>
        <br/>
        {1}
        <br/>
        <p>Link of produnct {2}</p>
        </body> 
        </html>
        """.format(title, image, URL)
    sendMeEmail("youradress@gmail.com", "Price dropping📉", htmlContent)
print(convertedPrice)
