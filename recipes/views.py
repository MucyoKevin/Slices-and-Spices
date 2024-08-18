from django.shortcuts import render
from django.http import JsonResponse
from .models import Recipe, Feedback
from .forms import FeedbackForm # type: ignore

def home(request):
    return render(request, 'home.html')

def cuisine_page(request, cuisine):
    recipes = Recipe.objects.filter(cuisine=cuisine)
    return render(request, f'{cuisine}.html', {'recipes': recipes})

def feedback(request):
    form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Feedback submitted successfully!'})
    return JsonResponse({'message': 'Invalid form submission.'}, status=400)