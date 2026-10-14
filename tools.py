import requests, json
from secret import API_KEY

BASE_URL = ("https://www.kobis.or.kr/kobisopenapi/webservice/rest/"
        "boxoffice/searchDailyBoxOfficeList.json")

def get_movie_audience(date:str, movie_name:str):
    """
        그 날자의 영화 제목에 대한 일일 관객수를 알려준다.

        받는 것 : date (문자열), movie_name (문자열) - 8자리 날짜, 예 : "20260824", 영화 제목, 예 : "오디세이"
        돌려주는 것 : (문자열) 관객 수. 예 : "186,587명"
        오류 처리 : 없는 영화 시
            - "'없는 영화' 은(는) {date} 순위에 없습니다."

        예시(Example)    
        print(tools.get_movie_audience("20260824", "오디세이"))
        # output : 186,587명

        print(tools.get_movie_audience("20260824", "호프"))
        # output : 3,026명

        print(tools.get_movie_audience("20260824", "없는영화"))
        # output : '없는영화' 은(는) 20260824 순위에 없습니다.
    """
    try:
        data = requests.get(BASE_URL, 
                            params={"key" : API_KEY, "targetDt": date}, 
                            timeout=10).json()
    except:
        print("[E0] 네트워크 API 요청에 실패하였습니다.")
    
    try:
        data = data['boxOfficeResult']['dailyBoxOfficeList']
    except KeyError:
        print("[E1] API에서 받은 결과를 파싱할 수 없습니다.\n없는 값 : ['boxOfficeResult']['dailyBoxOfficeList2']")
        return None
    
    try:
        for i in data:
            if i['movieNm'] == movie_name:
                return f"{int(i['audiCnt']):,}명"
        return f"'{movie_name}' 은(는) {date} 순위에 없습니다."
    except:
        print("[E2] 영화 비교 중 문제가 발생하였습니다.")

def get_boxoffice_rank_1(date):
    """
        그 날자의 박스오피스 1위 영화 제목을 알려준다.

        받는 것: date (문자열) - 8자리 날짜, 예 : "20260824
        돌려주는 것 : (문자열) 1위 영화 제목. 예 : "오디세이"
    """

    params = {"key" : API_KEY, "targetDt": date}
    response = requests.get(BASE_URL, params=params, timeout=10)
    data = response.json()
    movies = data['boxOfficeResult']['dailyBoxOfficeList']
    return movies[0]['movieNm']

if __name__ == "__main__":
    pass
    # print(get_boxoffice_rank_1("20260826"))
    # print(get_movie_audience("20260824", "오디세이"))
    # # output : 186,587명

    # print(get_movie_audience("20260824", "호프"))
    # # output : 3,026명

    # print(get_movie_audience("20260824", "없는영화"))
    # # output : '없는영화' 은(는) 20260824 순위에 없습니다.