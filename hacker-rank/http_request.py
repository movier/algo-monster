def getMovieTitles(substr):
    import requests
    url = "https://jsonmock.hackerrank.com/api/movies/search/?Title="

    response = requests.get(url)
    data = response.json()

    total_page = data['total_pages']
    per_page = data['per_page'] 
    titles = []

    for page in range(1, total_page + 1):
        content = requests.get("https://jsonmock.hackerrank.com/api/movies/search/?Title={}&amp;page={}".format(substr,page)).json()
        for per_p in range(per_page):
            titles.append(content['data'][per_p]['Title'])

    return sorted(titles)

print(getMovieTitles("spiderman"))