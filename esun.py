import requests
from bs4 import BeautifulSoup
response = requests.get(
    "https://accessible.esunbank.com.tw/Accessibility/ForeignExchangeRate")
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())  #輸出排版後的HTML內容

# result = soup.find("tbody")
# print(result)

# tbody = soup.find('tbody tr')
# print(tbody)
def find_one(enter_value): #找出user輸入的外幣買進&賣出價格
    result2=soup.find_all('td', attrs={'scope': 'row'})
    print(result2)
    
    if '澳' in enter_value:
        soup_search = '澳幣(AUD)'
    if '紐' in enter_value:
        soup_search = '紐西蘭幣(NZD)'
    if '美' in enter_value:
        soup_search = '美元(USD)'
    if '歐' in enter_value:
        soup_search = '歐元(EUR)'
    if '瑞' in enter_value:
        soup_search = '瑞士法郎(CHF)'
    if '英' in enter_value:
        soup_search = '英鎊(GBP)'
    if '日' in enter_value:
        soup_search = '日圓(JPY)'
    if '南' in enter_value:
        soup_search = '南非幣(ZAR)'
    if '新' in enter_value:
        soup_search = '新加坡幣(SGD)'
    if '墨' in enter_value or '披' in enter_value:
        soup_search='墨西哥披索(MXN)'    

    td_tag = soup.find('td', string=soup_search)

    if td_tag:
        # 获取对应的<tr>标签
        tr_tag = td_tag.parent
        # 获取<tr>标签下的所有<td align="right">标签
        align_right_td_tags = tr_tag.find_all('td', align='right')
        print('align_right_td_tags',align_right_td_tags)
        # 提取两个<td align="right">标签的内容
        data = [td.text.strip() for td in align_right_td_tags]
        # print("两个数据分别为:", data)
        print(f"{soup_search}價格為，賣出:{data[0]}、買入:{data[1]}")
    else:
        print("未找到对应的货币名称。")
    return f"{soup_search}價格為，賣出:{data[0]}、買入:{data[1]}"

find_one('美元')