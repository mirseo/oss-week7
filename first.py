import requests, json
from secret import API_KEY

def get_movies(date):
    print(date)

url = ("https://www.kobis.or.kr/kobisopenapi/webservice/rest/"
        "boxoffice/searchDailyBoxOfficeList.json")
params = {"key" : API_KEY, "targetDt": "20260826"}

response = requests.get(url, params= params, timeout = 10)
print(response.status_code)

data = response.json()
result = data['boxOfficeResult']
print(data.keys())

movies = result['dailyBoxOfficeList']

for movie in movies[:5]:
    rank = movie['rank']
    name = movie['movieNm']
    audi = int(movie['audiCnt'])
    print(f"{rank}위 {name} {audi:,} 명")


