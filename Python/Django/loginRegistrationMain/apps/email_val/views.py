from django.shortcuts import render, redirect
from .models import Email
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
    'emails': Email.objects.all()
    }
    return render(request, "email_val/index.html", context)

def validate(req):
    email_check = Email.objects.validate(req.POST['email'])
    if email_check == False:
        messages.error(req, 'Invalid Email')
    else:
        messages.success(req, 'Valid Email!')

    return redirect('/')

def remove(req, id):
    Email.objects.filter(id=id).delete()
    return redirect('/')
