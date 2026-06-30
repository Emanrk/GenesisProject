from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def details(request):
    return render(request, 'details.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def services(request):
    return render(request, 'services.html')

def starter(request):
    return render(request, 'starter-page.html')

def custom_404(request, exception=None):
    return render(request, '404.html', status=404)