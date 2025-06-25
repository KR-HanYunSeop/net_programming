from urllib import parse
from urllib import request
import ssl

url = 'https://search.naver.com/search.naver?query=iot'

parsed_url = parse.urlparse(url)
print(parsed_url)

print(parsed_url.scheme + '://' + parsed_url.netloc + parsed_url.path)

context = ssl._create_default_https_context()
rsp = request.urlopen('https://search.naver.com/search.naver?query=iot',context=context)

print('HTTP Response:', rsp) 
print('URL:', rsp.geturl()) 
print('Status:', rsp.getcode())
headers = rsp.info() 
print(headers)



