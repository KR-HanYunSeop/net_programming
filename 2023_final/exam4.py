import re
import requests

url = "https://en.wikipedia.org/wiki/Internet_of_things"

# 웹 페이지 요청
response = requests.get(url)

# HTML 추출
if response.status_code == 200:
    html_content = response.text

    # 정규식 패턴
    pattern = r'\b[iI][oO][tT]\w{1,}\b'

    iots = re.findall(pattern, html_content)

    print(iots)

    
    