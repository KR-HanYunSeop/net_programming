#['apple', 'banana', 'grape', 'orange']
#string.split(',', maxsplit=2)
#['apple', 'banana', 'grape,orange']


str = 'https://search.naver.com/search.naver?where=nexearch&ie=utf8&query=iot'

str = str.split('?')[1]
print(str)

str = str.split('&')
print(str)

str_dict = {}
for query in str:
  key, value = query.split('=')
  str_dict[key] = value
  
print(str_dict)