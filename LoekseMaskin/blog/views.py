from django.shortcuts import render
from blog.models import blog

def index(request):
    blog_list = blog.objects.get(pk=blog.number)
    context = {'blog_list' : blog_list}
    return render(request, 'blogg.html', context)
