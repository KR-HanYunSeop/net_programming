import re
import requests

url = "https://www.plabfootball.com/"

# 웹 페이지 요청
response = requests.get(url)

# 요청이 성공한 경우 HTML 추출
if response.status_code == 200:
    html_content = response.text

    # 이메일 주소를 추출하기 위한 정규식 패턴
    email_pattern = r'\b[A-Za-z0-9._]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

    # 추출된 이메일 주소를 저장할 리스트
    emails = re.findall(email_pattern, html_content)

    # 추출된 이메일 주소 출력
    for email in emails:
        print(email)
