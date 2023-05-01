str = "https://search.naver.com/search.naver?where=nexearch&ie=utf8&query=iot"

query_string = str.split('?')[1]

dict = {}

for query in query_string.split('&'):
    key, value = query.split('=')
    dict[key] = value

print(dict)


