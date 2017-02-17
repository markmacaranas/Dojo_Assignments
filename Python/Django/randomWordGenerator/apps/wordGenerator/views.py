from django.shortcuts import render, redirect
from random import choice
from string import ascii_uppercase

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0


    return render(request, 'wordGenerator/index.html')
# Create your views here.

def logic(request):
    if request.method == "GET":
        if request.GET['submit'] == "RESET":
            request.session.clear()
        if request.GET['submit'] == "Generate":
            request.session['random_word'] = ''.join(choice(ascii_uppercase) for i in range (14))
            request.session['count'] += 1

        return redirect('/')
