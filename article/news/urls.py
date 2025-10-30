from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<int:id>/', views.blog, name='blog'),
    path('author/<int:id>/', views.author, name='author'),
    path('bookmarks/', views.view_bookmarks, name='view_bookmarks'),
    path('bookmark/<int:id>/', views.bookmark, name='bookmark'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name='register'),
    path('community/', views.community, name='community'),
    path('fetch/', views.fetch_new_articles, name='fetch_new_articles'),
    # path('change/', views.changeLang, name='changeLang'),  
    path('clear-translations/', views.clear_translations, name='clear_translations'),

  
]