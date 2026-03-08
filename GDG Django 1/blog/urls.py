from django.urls import path
from .views import WelcomeView
from .views import hello_blog
from .views import post_titles
urlpatterns = [
    path('', hello_blog, name='home'),          
    path('home/', hello_blog, name='home2'),    
    path('welcome/', WelcomeView.as_view(), name='welcome'),
    path('posts/', post_titles, name='post_titles'),
]
