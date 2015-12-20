from django.http import HttpResponse
from django.utils.html import escape
def hello(request):
    data = "Hello, world!!! </br>"
    get = request.GET
    post = request.POST
    html = data + "</br>Your GET data:</br>" +  get.urlencode() + "</br>Your POST data:</br>"  + post.urlencode()
    return HttpResponse((html))
