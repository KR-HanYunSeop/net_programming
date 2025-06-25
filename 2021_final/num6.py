import requests

# apikey 삽입
api_key = '' 
url = 'https://dapi.kakao.com/v2/vision/adult/detect'

# 이미지 파일 경로 설정
image_path = 'iot.png'

# API 호출
headers = {'Authorization': 'KakaoAK {}'.format(api_key)}
files = {'image': open(image_path, 'rb')}
response = requests.post(url, headers=headers, files=files)

# 응답 결과 확인
result = response.json()
print('normal : ' , result['result']['normal'])
print('soft : ' , result['result']['soft'])
print('adult : ' , result['result']['adult'])