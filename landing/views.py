from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context_dict = {}
    return render(request, 'landing/index.html', context=context_dict)
