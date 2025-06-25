
import requests
import re

url = 'http://localhost:8080'
rsp = requests.get(url)

html = rsp.text
stock_results = re.findall(r'[a-zA-Z0-9_.]+@.+\.[a-z]{2,3}', html) # <dl class>~</dl> 정보를 추출
print(html)
print(stock_results, '\n')

# samsung_stock = stock_results[0] # HTML 내에 2개의 <dl class>~</dl> 부분이 존재. 첫 번째 것을 선택
# samsung_index = samsung_stock[1] # <dl class>~</dl> 사이의 정보만 추출

# # 주식 정보(<dd>~</dd>)를 추출
# index_list = re.findall(r'(<dd>)([\s\S]+?)(<\/dd>)', samsung_index)
# print(index_list , '\n')
for a in stock_results:
    print(a)