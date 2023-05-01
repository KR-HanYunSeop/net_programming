str = "https://search.daum.net/search?w=tot&q=bigdata"

query_string = str.split('?')[1]

dict = {}

for query in query_string.split('&'):
    key, value = query.split('=')
    dict[key] = value

print(dict)

dict['q'] = 'iot'
print(dict)


