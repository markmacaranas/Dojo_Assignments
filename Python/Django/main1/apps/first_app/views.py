from django.shortcuts import render, HttpResponse
# Create your views here.
# def index(request):
#         response = "Hello, I am your first request!"
#         return HttpResponse(response)

def index(request):
	print "*"*50
	return render(request, 'first_app/index.html')
