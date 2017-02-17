from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0

    return render(request, 'survey/index.html')

def process(request):
    print "hi1"
    print request.POST['name']
    print "end of hi"
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['langugage'] = request.POST['language']
        request.session['comments'] = request.POST['comments']
        request.session['count'] += 1
        return redirect('/result')

def result(request):
        print "testtesttest"
        return render(request, 'survey/result.html')

def back(request):
        return redirect ('/')

# Create your views here.
