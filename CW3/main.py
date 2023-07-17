import requests

api_key = ""
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-06-17&sortBy=publishedAt&apiKey="

request = requests.get(url)

content = request.json()
for article in content["articles"]:
    print(article["title"])
