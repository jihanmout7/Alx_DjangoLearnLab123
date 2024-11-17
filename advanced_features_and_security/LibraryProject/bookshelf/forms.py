from django.shortcuts import render
from .models import Book
from .forms import SearchForm

def ExempleForm(request):
    form = SearchForm(request.GET)
    results = []

    if form.is_valid():  # Only proceed if the form data is valid
        query = form.cleaned_data['search_term']
        results = Book.objects.filter(title__icontains=query)

    return render(request, 'search_results.html', {'form': form, 'results': results})
