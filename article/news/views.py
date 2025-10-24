from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import signupForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import requests
from django.contrib.auth.models import User
from .api import getArticles
# from newspaper import Article
import requests
import random
from .models import Article,Bookmark
from .utils import extract_article_text

@login_required(login_url='login')
def bookmark(request, id):
    # Only allow POST requests (from the form)
    if request.method == 'POST':
        book = Article.objects.get(id=id)
        bookmarked, created = Bookmark.objects.get_or_create(article=book, user=request.user)

        if not created:
            bookmarked.delete()
            # messages.info(request, f"Removed bookmark: {book.title}")
        # else:
        #     messages.success(request, f"Bookmarked: {book.title}")

    # Redirect back to home or article page after toggling
    return redirect('home')




@login_required(login_url='login')
def view_bookmarks(request):
    bookmarks = Bookmark.objects.filter(user=request.user)
    

    return render(request, 'bookmark.html', {'bookmarks': bookmarks})


@login_required(login_url='login')
def fetch_new_articles(request):
    getArticles()  # Run your scraper function
    messages.success(request, "✅ New articles fetched successfully!")
    return redirect('home')  # Redirect to homepage after fetching


@login_required(login_url='login')
def home(request):
    # article = getArticles()
    articles = (
        Article.objects
        .exclude(content__isnull=True)                 # remove empty content
        .exclude(content__exact='')                    # remove blank content
        .exclude(image_url__isnull=True)               # remove missing images
        .exclude(image_url__exact='')                  # remove empty image URLs
        .order_by('-id')                              # newest first
    )

    # Optional: filter out short content (less than 50 words)
    filtered_articles = [a for a in articles if len(a.content.split()) >= 50]
    return render(request, 'project.html', {'article': filtered_articles}) 



@login_required(login_url='login')
def blog(request, id):
    # articles = getArticles()
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        article = None

    
    # title = article['title']
    # author = article['creator']
    # image = article['image_url']
    # pubDate = article['pubDate']

    # author_name, created = User.objects.get_or_create(username=author)

   
    # random.shuffle(articles)
    # url_main = articles[index]['link'] if index < len(articles) else None

    # full_content = extract_article_text(url_main) if url_main else "No link available."
    # if not Article.objects.filter(title=title).exists():
    #     Article.objects.create(
    #     title=title,
    #     content=full_content,
    #     author=author_name,
    #     image_url = image,
    #     pub_date = pubDate
    # )

    # if id < len(article):
    #     articles = article[id]
    # else:
    #     articles = None
    

    # url = "https://article-extractor2.p.rapidapi.com/article/proxy/parse"

    # querystring = {"url":url_main}

    # headers = {
    #     "x-rapidapi-key": "82aab3a533msh9c0c90306211689p170617jsn8c1c931367ef",
    #     "x-rapidapi-host": "article-extractor2.p.rapidapi.com"
    # }

    # response = requests.get(url, headers=headers, params=querystring)

  
    # summary = response.json()
    # content = summary['data']['content']
    return render(request, 'blog.html', {'article': article})  

@login_required(login_url='login')
def author(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        article = None

    # user = User.objects.filter(username=author).first()

    # Get their posts if the user exists
    # posts = Article.objects.filter(author=user) if user else []
    return render(request, 'author.html', {'article': article})  

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')
        return render(request, 'login.html')  

def logoutUser(request):
    logout(request)
    return redirect('login')

def register(request):
    form = signupForm()

    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Welcome ' + user)
            return redirect('login')
    return render(request, 'register.html', {'form': form}) 

def community(request):
    return render(request, 'community.html')  


# working prototype

# ----------------------------------


# for extracting the content

# from bs4 import BeautifulSoup

# def extract_full_article(url):
#     try:
#         response = requests.get(url, timeout=10)
#         response.raise_for_status()  # raise error if failed

#         soup = BeautifulSoup(response.text, 'html.parser')

#         # Extract all text from <p> tags (basic method)
#         paragraphs = [p.get_text() for p in soup.find_all('p')]
#         full_content = " ".join(paragraphs)

#         # Optional: Clean very short paragraphs (like headers/ads)
#         full_content = " ".join([p for p in paragraphs if len(p) > 50])
#         return full_content.strip() or "No readable content found."
#     except Exception as e:
#         return f"Error fetching article: {e}" 