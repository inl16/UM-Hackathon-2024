import requests

# Replace 'YOUR_API_KEY' here with your actual News API key
api_key = ''
query = 'Boeing'
url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'

response = requests.get(url)

if response.status_code == 200:
    # If the request was successful, process the response
    data = response.json()  # Convert response to JSON
    articles = data.get('articles', [])
    for article in articles:
        # For each article, print the title and URL (or any other information you need)
        print(f"Title: {article['title']}")
        print(f"URL: {article['url']}\n")
else:
    print(f"Failed to fetch data, status code: {response.status_code}")
