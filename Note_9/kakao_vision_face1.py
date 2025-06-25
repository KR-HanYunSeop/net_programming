import requests

API_URL = 'https://dapi.kakao.com/v2/vision/face/detect'
REST_API_KEY = 'e7c359e1445b8848424daa1c765a3fdf'

# app_key와 이미지 파일을 POST로 전송하여 얼굴 검출을 수행
headers = {'Authorization' : 'KakaoAK {}'.format(REST_API_KEY)}
files = {'image' : open('myphoto.jpg', 'rb')}
rsp = requests.post(API_URL, headers=headers, files=files)
print(rsp.json()) # 검출 결과를 딕셔너리로 변환하여 출력