from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.

def home(request):
    newsapi = NewsApiClient(api_key="92bfa5b740c3487390408cb5721efd7f")
    
    topheadlines = newsapi.get_top_headlines()
    
    
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
    post = []

    for i in range(len(articles)):
        myarticles = articles[i]
        img.append(myarticles['urlToImage'])
        news.append(myarticles['title'])
        desc.append(myarticles['content'])
        post.append(myarticles['publishedAt'])
    
    mylist = zip(news, desc, img , post)

    print(topheadlines)

    return render(request, 'home.html', context={"mylist":mylist})
  
#sports

def  sports (request):
    newsapi = NewsApiClient(api_key="92bfa5b740c3487390408cb5721efd7f")
    
    topheadlines = newsapi.get_everything(q="sports",language='en',qintitle='player')
    
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
    post = []

    for i in range(len(articles)):
        myarticles = articles[i]
        img.append(myarticles['urlToImage'])
        news.append(myarticles['title'])
        desc.append(myarticles['content'])
        post.append(myarticles['publishedAt'])
    
    mylist = zip(news, desc, img , post)

    print(topheadlines)

    return render(request, 'sport.html', context={"mylist":mylist})
 
#entertainment
def  entertainment (request):
    newsapi = NewsApiClient(api_key="92bfa5b740c3487390408cb5721efd7f")
    
    topheadlines = newsapi.get_everything(q="entertainment",language='en',qintitle='hollywood')
    
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
    post = []

    for i in range(len(articles)):
        myarticles = articles[i]
        img.append(myarticles['urlToImage'])
        news.append(myarticles['title'])
        desc.append(myarticles['content'])
        post.append(myarticles['publishedAt'])
    
    mylist = zip(news, desc, img , post)

    print(topheadlines)

    return render(request, 'entertainment.html', context={"mylist":mylist})
 
#health
def  health (request):
    newsapi = NewsApiClient(api_key="92bfa5b740c3487390408cb5721efd7f")
    
    topheadlines = newsapi.get_everything(q="health",language='en',qintitle='hospital',page=2)
    
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
    post = []

    for i in range(len(articles)):
        myarticles = articles[i]
        img.append(myarticles['urlToImage'])
        news.append(myarticles['title'])
        desc.append(myarticles['content'])
        post.append(myarticles['publishedAt'])
    
    mylist = zip(news, desc, img , post)

    print(topheadlines)

    return render(request, 'health.html', context={"mylist":mylist})


#technology
def  technology (request):
    newsapi = NewsApiClient(api_key="92bfa5b740c3487390408cb5721efd7f")
    
    topheadlines = newsapi.get_everything(q="technology",language='en',qintitle='technology',page=2)
    
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
    post = []

    for i in range(len(articles)):
        myarticles = articles[i]
        img.append(myarticles['urlToImage'])
        news.append(myarticles['title'])
        desc.append(myarticles['content'])
        post.append(myarticles['publishedAt'])
    
    mylist = zip(news, desc, img , post)

    print(topheadlines)

    return render(request, 'technology.html', context={"mylist":mylist})


#business
def  business (request):
    newsapi = NewsApiClient(api_key="92bfa5b740c3487390408cb5721efd7f")
    
    topheadlines = newsapi.get_everything(q="business",language='en',qintitle='trade',page=2)
    
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
    post = []

    for i in range(len(articles)):
        myarticles = articles[i]
        img.append(myarticles['urlToImage'])
        news.append(myarticles['title'])
        desc.append(myarticles['content'])
        post.append(myarticles['publishedAt'])
    
    mylist = zip(news, desc, img , post)

    print(topheadlines)

    return render(request, 'health.html', context={"mylist":mylist})


#POLITICS
def politics(request):
    newsapi = NewsApiClient(api_key="92bfa5b740c3487390408cb5721efd7f")
    
    topheadlines = newsapi.get_everything(q="politics",language='en',page=3)
    
    
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
    post = []

    for i in range(len(articles)):
        myarticles = articles[i]
        img.append(myarticles['urlToImage'])
        news.append(myarticles['title'])
        desc.append(myarticles['content'])
        post.append(myarticles['publishedAt'])
    
    mylist = zip(news, desc, img , post)

    print(topheadlines)

    return render(request, 'politics.html', context={"mylist":mylist})


#literature
def literature(request):
    newsapi = NewsApiClient(api_key="92bfa5b740c3487390408cb5721efd7f")
    
    topheadlines = newsapi.get_everything(q="literature",language='en',page=4, qintitle='literature' )
    
    
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
    post = []

    for i in range(len(articles)):
        myarticles = articles[i]
        img.append(myarticles['urlToImage'])
        news.append(myarticles['title'])
        desc.append(myarticles['content'])
        post.append(myarticles['publishedAt'])
    
    mylist = zip(news, desc, img , post)

    print(topheadlines)

    return render(request, 'literature.html', context={"mylist":mylist})


#CORONA VIRUS
def corona(request):
    newsapi = NewsApiClient(api_key="92bfa5b740c3487390408cb5721efd7f")
    
    topheadlines = newsapi.get_everything(q="corona",language='en',page=2, qintitle='corona' )
    
    
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
    post = []

    for i in range(len(articles)):
        myarticles = articles[i]
        img.append(myarticles['urlToImage'])
        news.append(myarticles['title'])
        desc.append(myarticles['content'])
        post.append(myarticles['publishedAt'])
    
    mylist = zip(news, desc, img , post)

    print(topheadlines)

    return render(request, 'corona.html', context={"mylist":mylist})

#about 
def about(request):
    
    return render(request , 'about.html')


#sensex
def sensex(request):
    newsapi = NewsApiClient(api_key="92bfa5b740c3487390408cb5721efd7f")
    
    topheadlines = newsapi.get_everything(q="sensex",language='en',page=1, qintitle='sensex' )
    
    
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
    post = []

    for i in range(len(articles)):
        myarticles = articles[i]
        img.append(myarticles['urlToImage'])
        news.append(myarticles['title'])
        desc.append(myarticles['content'])
        post.append(myarticles['publishedAt'])
    
    mylist = zip(news, desc, img , post)

    print(topheadlines)

    return render(request, 'sensex.html', context={"mylist":mylist})