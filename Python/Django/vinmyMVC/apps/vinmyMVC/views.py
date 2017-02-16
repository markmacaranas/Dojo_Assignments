from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'vinmyMVC/index.html')

def show(request):
    print return.method
    return return render(request, 'vinmyMVC/show_users.index.html')
