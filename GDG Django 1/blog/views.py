from django.http import HttpResponse
from django.views import View   # MUST be here
from .models import Post

# Question 2: Function-Based View
def hello_blog(request):
    return HttpResponse("Hello Blog")

# Question 4: Class-Based View
class WelcomeView(View):
    def get(self, request):
        return HttpResponse("Welcome to Django CBV")

# Question 5: Function-Based View to show all post titles
def post_titles(request):
    posts = Post.objects.all()
    titles = ", ".join(post.title for post in posts)
    return HttpResponse(titles)
