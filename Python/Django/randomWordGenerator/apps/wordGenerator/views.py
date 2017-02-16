from django.shortcuts import render

def index(request):
    return render(request, 'wordGenerator/index.html')
# Create your views here.
