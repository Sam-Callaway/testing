import newspaper
import json

url = 'https://www.dailymail.co.uk/news/article-11862841/Childcare-pension-tax-breaks-Hunts-work-Budget.html'
  
article = newspaper.Article(url=url, language='en')
article.download()
article.parse()

article ={
    "title": str(article.title),
    "text": str(article.text),
    "authors": article.authors,
    "published_date": str(article.publish_date),
    "top_image": str(article.top_image),
    "videos": article.movies,
    "keywords": article.keywords,
    "summary": str(article.summary)
}


print(article["text"])