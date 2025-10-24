import requests
from .models import Article
from .utils import extract_article_text
from django.contrib.auth.models import User

def getArticles():
    url = 'https://newsdata.io/api/1/news?apikey=pub_2caddf667d6f4605be59fee98689f132&country=us&category=technology&language=en'
    response = requests.get(url)
    data = response.json()

    articles = []

     
    category = 'technology'
    for article in data.get('results', []):
        articles.append({
            'title': article.get('title'),
            'description': article.get('description'),
            'keywords': article.get('keywords'),
            'pubDate': article.get('pubDate'),
            'category': category,
            'link': article.get('link'),
            'creator': article.get('creator', ['Unknown'])[0] if article.get('creator') else 'Unknown',

            'source': article.get('source_id'),
            'image_url': article.get('image_url'),
            'link': article.get('link'),
        })

        title = article.get('title')
        author_name = article.get('creator', ['Unknown'])[0] if article.get('creator') else 'Unknown'
        image = article.get('image_url')
        pubDate = article.get('pubDate')
        link = article.get('link')

        full_content = extract_article_text(link) if link else article.get('description', '')

        # save to DB if new
        user, _ = User.objects.get_or_create(username=author_name)

        if not Article.objects.filter(title=title).exists():
            Article.objects.create(
                title=title,
                content=full_content,
                author=user,
                image_url=image,
                pub_date=pubDate,
            )



    return articles

# url = 'https://newsdata.io/api/1/news?apikey=pub_2caddf667d6f4605be59fee98689f132&country=us&category=technology&language=en'
# response = requests.get(url)
# data = response.json()
# for article in data['results']:
#     print(article['link'])



