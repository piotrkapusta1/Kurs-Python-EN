import requests

api_key = "3d7407d176d948ab99287ac3fbc017bc"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-06-17&sortBy=publishedAt&apiKey=3d7407d176d948ab99287ac3fbc017bc"

request = requests.get(url)

content = request.json()
for article in content["articles"]:
    print(article["title"])
