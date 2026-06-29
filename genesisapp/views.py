from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json

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

@require_POST
def contact(request):
    name = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip()
    subject = request.POST.get('subject', '').strip()
    message = request.POST.get('message', '').strip()

    errors = []
    if not name:
        errors.append('Name is required.')
    if not email:
        errors.append('Email is required.')
    if not message:
        errors.append('Message is required.')

    if errors:
        return JsonResponse({'status': 'error', 'message': ' '.join(errors)}, status=400)

    # TODO: send email via Django's send_mail or save to DB
    # For now, just acknowledge receipt
    return JsonResponse({'status': 'ok', 'message': 'Your message has been sent. Thank you!'})

@require_POST
def newsletter(request):
    email = request.POST.get('email', '').strip()
    if not email:
        return JsonResponse({'status': 'error', 'message': 'Email is required.'}, status=400)

    # TODO: save subscriber to DB or integrate with email service
    return JsonResponse({'status': 'ok', 'message': "You've been subscribed. Thank you!"})
