# from django.conf.urls import url
#
# def index(request):
#     print ("8"*100)
#     print ("8"*100)
#     print ("bananapeel")
#     print ("8"*100)
#     print ("8"*100)
#
# urlpatterns = [
#     url(r'^$', index)
# ]

# from django.conf.urls import url
# def method_to_run(request):
#         print "Whatever route that was hit by an HTTP request (by the way) decided to invoke me!"
#         print "By the way, here's the request object that Django automatically passes us:", request
#         print "By the by, we still aren't delivering anything to the browser, so you should see 'ValueError at /'"
#
# urlpatterns = [
#     url(r'^$', method_to_run)
#   ]

# from django.conf.urls import url
# from . import views
# urlpatterns = [
#         url(r'^$', views.index)
#   ]

from django.conf.urls import url
from . import views

#Models -- views - TEMPLATES

urlpatterns = [
    url(r'^', views.index)
]
