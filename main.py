import tools
print(tools.get_boxoffice_rank_1("20260824"))

print(tools.get_movie_audience("20260824", "오디세이"))
# output : 186,587명

print(tools.get_movie_audience("20260824", "호프"))
# output : 3,026명

print(tools.get_movie_audience("20260824", "없는영화"))
# output : '없는영화' 은(는) 20260824 순위에 없습니다.