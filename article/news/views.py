from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import signupForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import requests
from django.contrib.auth.models import User
from .api import getArticles
from . import api
# from newspaper import Article
import requests
import random
from .models import Article,Bookmark
from .utils import extract_article_text
from  django.db.models import Q                                                  
# from googletrans import Translator
# translator = Translator()

# country = 'us'
# language = 'en'

# @login_required(login_url='login')
def search(request):  
    try:
        if request.method == 'GET':
            search = request.GET.get('search')
            search_result = Article.objects.filter(
                Q(title__icontains=search) | Q(content__icontains=search)| Q(author__username__icontains=search)
            )
            if search_result:
                
                print(f"{search_result}")
               
            else:
                print("not working")
        else:
            pass     
    except: 
        search_result='feedline'   
    return render(request, 'search.html', {'search': search, 'search_result': search_result})

@login_required(login_url='login')
def change_country(request):
    if request.method == 'POST':
        country = request.POST.get('country')
        api.country =  country
        getArticles(request)
        request.session['country'] = country
    return redirect('home')

@login_required(login_url='login')
def clear_translations(request):
    # Allow only admin users for safety
    if not request.user.is_superuser:
        messages.error(request, "❌ Only admins can clear translations.")
        return redirect('home')

    for article in Article.objects.all():
        article.translations = {}
        article.save()

    messages.success(request, "✅ All translations cleared successfully!")
    return redirect('home')

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
    getArticles(request)  # Run your scraper function
    messages.success(request, "✅ New articles fetched successfully!")
    return redirect('home')  # Redirect to homepage after fetching

from deep_translator import GoogleTranslator

def translate_large_text(text, target_lang):
    max_length = 5000
    chunks = [text[i:i + max_length] for i in range(0, len(text), max_length)]
    translated_chunks = []

    for chunk in chunks:
        translated_chunk = GoogleTranslator(source='auto', target=target_lang).translate(chunk)
        translated_chunks.append(translated_chunk)

    return " ".join(translated_chunks)

@login_required(login_url='login')
def home(request):
    #search
    
     
    # logged in user can create post
    if request.method == 'POST' and 'title' in request.POST:
        post_title = request.POST.get('title')
        post_image = request.FILES.get('image')
        post_content = request.POST.get('content')
        

        Article.objects.create(
            title = post_title,
            content = post_content,
            image_post = post_image
        )

        return redirect('home')
        

    

    # Handle language form
    if request.method == 'POST' and 'language' in request.POST:
        selected_lang = request.POST.get('language')
        if selected_lang:
            request.session['language'] = selected_lang

    language = request.session.get('language', 'en')

    articles = (
        Article.objects
        .exclude(content__isnull=True)
        .exclude(content__exact='')
        # .exclude(image_url__isnull=True)
        # .exclude(image_url__exact='')
        # .exclude(image_post__isnull=True)
        .order_by('-id')
    )

    bookmarks = Bookmark.objects.filter(user=request.user)
    book = bookmarks.count()
    filtered_articles = [a for a in articles if len(a.content.split()) >= 50]

    if language != 'en':
        for article in filtered_articles:
            # Make sure the article has a translations dict
            if not hasattr(article, 'translations') or not isinstance(article.translations, dict):
                article.translations = {}

            # Only translate if not already stored
            if language not in article.translations:
                print(f"Translating article {article.id} to {language}...")

                translated_title = translate_large_text(article.title, language)
                translated_content = translate_large_text(article.content[:1000], language)

                # Save both translations
                article.translations[language] = {
                    'title': translated_title,
                    'content': translated_content
                }
                article.save()
            else:
                print(f"Using cached translation for article {article.id}")

            # Replace for display
            # Handle old string-based translation format
            translation_data = article.translations.get(language)

            if isinstance(translation_data, str):
                # Old format (string) — just use it for content
                article.content = translation_data
            else:
                # New format (dict)
                article.title = translation_data.get('title', article.title)
                article.content = translation_data.get('content', article.content)


    return render(request, 'project.html', {'article': filtered_articles, 'book': book})



# @login_required(login_url='login')
# def changeLang(request):
#         if request.method == 'POST':
#             selected_lang = request.POST.get('name')
#             request.session['language'] = selected_lang
#             # getArticles(request)
#         return redirect('home')

@login_required(login_url='login')
def blog(request, id):
    # articles = getArticles()

    articles = (
    Article.objects
    .exclude(content__isnull=True)
    .exclude(content__exact='')
    # .exclude(image_url__isnull=True)
    # .exclude(image_url__exact='')
    # .exclude(image_post__isnull=True)
    .order_by('-id')
    )
    filtered_articles = [a for a in articles if len(a.content.split()) >= 50] 
    language = request.session.get('language', 'en')

    if language == 'en':
        try:
            article = Article.objects.get(id=id)
        except Article.DoesNotExist:
            article = None
    
    
        # if language is not english 
    else:
        try:
            article = Article.objects.get(id=id)
        except Article.DoesNotExist:
            article = None

       

        if language not in article.translations:
            translated_title = translate_large_text(article.title, language)
            translated_content = translate_large_text(article.content, language)

            article.translations[language] = {
                'title': translated_title,
                'content': translated_content
            }
            article.save()

        translation_data = article.translations.get(language)
        if isinstance(translation_data, dict):
            article.title = translation_data['title']
            article.content = translation_data['content']
            
    

    return render(request, 'blog.html', {'article': article, 'articles': filtered_articles})  

@login_required(login_url='login')
def author(request, id):
    try:
        # Get the article that was clicked
        article = Article.objects.get(id=id)
        # Get the author of that article
        author = article.author  
        # Get all posts by that author
        posts = Article.objects.filter(author=author).order_by('-id')  # optional ordering
    except Article.DoesNotExist:
        article = None
        posts = []

    return render(request, 'author.html', {
        'article': article,   # the post that was clicked
        'posts': posts,       # all posts by this author
        'author': author if article else None
    })


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