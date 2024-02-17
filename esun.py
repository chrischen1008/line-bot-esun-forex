import requests
from bs4 import BeautifulSoup
response = requests.get(
    "https://accessible.esunbank.com.tw/Accessibility/ForeignExchangeRate")
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())  #輸出排版後的HTML內容

result = soup.find("tbody")
print(result)