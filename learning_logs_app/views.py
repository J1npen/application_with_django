from django.shortcuts import render

def index(request):
    """The home page for Learning Log."""
    return render(request, 'index.html')

def base(request):
    """The base page for Learning Log."""
    return render(request, 'base.html')