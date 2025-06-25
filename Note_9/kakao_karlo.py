import requests, json, io, base64
from PIL import Image

REST_API_KEY = 'e7c359e1445b8848424daa1c765a3fdf'

def t2i(text, batch_size=1): # 이미지 생성하기 요청
    r = requests.post(
        'https://api.kakaobrain.com/v1/inference/karlo/t2i',
        json = {
'prompt': {
'text': text,
'batch_size': batch_size
}
},
headers = {
'Authorization': f'KakaoAK {REST_API_KEY}',
'Content-Type': 'application/json'
}
)
    
    response = json.loads(r.content)
    return response

# Base64 디코딩 및 변환
def stringToImage(base64_string, mode='RGBA'):
    imgdata = base64.b64decode(str(base64_string))
    img = Image.open(io.BytesIO(imgdata)).convert(mode)
    return img
text = "A lake, alpine, vivid" # 프롬프트에 사용할 제시어

response = t2i(text, 1) # 이미지 생성하기 REST API 호출
# 응답의 첫 번째 이미지 생성 결과 출력하기
result = stringToImage(response.get("images")[0].get("image"), mode='RGB')
result.show()