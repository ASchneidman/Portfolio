from django.shortcuts import render

def classoutside(request):
    context_dict = {}
    return render(request, 'ClassOutside/classoutside.html', context=context_dict)
