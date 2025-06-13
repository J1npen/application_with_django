from django.shortcuts import render

from .models import Topic

def index(request):
    """The home page for Learning Log."""
    return render(request, 'index.html')

def base(request):
    """The base page for Learning Log."""
    return render(request, 'base.html')

def topics(request):
    """The topics page for Learning Log."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'topics.html', context)